import os

from django.conf import settings
from django.http import FileResponse
from rest_framework.fields import CharField

from apps.upload.models import FileInfo
from apps.upload.serials import FileInfoSerial
from common import const
from common.const import UploadFilePath
from common.exceptions import ObjectNotFound
from common.views import PermLessApiView, BaseParam


class UploadFileCheckView(PermLessApiView):
    class CheckParam(BaseParam):
        md5 = CharField(required=True, help_text='md5')

    def get(self, request):
        params = self.valid_param(self.CheckParam(data=request.query_params))
        # 文件已存在，直接返回地址
        file_info = FileInfo.objects.get_or_none(md5=params.md5)
        if file_info:
            return self.success_response(FileInfoSerial(file_info).data)

        # 分片信息
        slice_file_path = os.path.join(settings.FILE_PATH, UploadFilePath.SLICE, params.md5)
        if not os.path.exists(slice_file_path):
            return self.success_response({'slice_file_names': []})
        else:
            slice_files = list()
            for file_name in os.listdir(slice_file_path):
                slice_files.append(int(file_name))
            slice_files.sort()
            return self.success_response({'slice_file_names': slice_files})


class UploadFileSliceView(PermLessApiView):
    class SliceParam(BaseParam):
        md5 = CharField(required=True, help_text='md5')
        index = CharField(required=True, help_text='index')

    def post(self, request):
        params = self.valid_param(self.SliceParam(data=request.data))
        slice_file = request.FILES['file']
        if not slice_file:
            return self.fail_response('文件不能为空')
        slice_file_path = os.path.join(settings.FILE_PATH, UploadFilePath.SLICE, params.md5)
        if not os.path.exists(slice_file_path):
            os.makedirs(slice_file_path)
        slice_file_path = os.path.join(slice_file_path, params.index)
        with open(slice_file_path, 'wb') as f:
            for chunk in slice_file.chunks():
                f.write(chunk)
        return self.success_response()


class UploadFileMergeView(PermLessApiView):
    class MergeParam(BaseParam):
        md5 = CharField(required=True, help_text='md5')
        full_filename = CharField(required=True, help_text='full_filename')

    def post(self, request):
        params = self.valid_param(self.MergeParam(data=request.data))
        # 文件已存在，直接返回地址
        file_info = FileInfo.objects.get_or_none(md5=params.md5)
        if file_info:
            return self.success_response(FileInfoSerial(file_info).data)
        filename, extension = os.path.splitext(params.full_filename)

        slice_file_path = os.path.join(settings.FILE_PATH, UploadFilePath.SLICE, params.md5)
        if not os.path.exists(slice_file_path):
            return self.fail_response('file upload fail!')

        # 文件合并
        slice_files = list()
        for file_name in os.listdir(slice_file_path):
            slice_files.append(int(file_name))
        slice_files.sort()
        complete_file_path = os.path.join(settings.FILE_PATH, UploadFilePath.COMPLETE)
        if not os.path.exists(complete_file_path):
            os.makedirs(complete_file_path)
        file_path = os.path.join(complete_file_path, params.md5 + extension)
        with open(file_path, 'wb') as tf:
            for file_name in slice_files:
                slice_file = os.path.join(slice_file_path, str(file_name))
                with open(slice_file, 'rb') as sf:
                    tf.write(sf.read())
                os.remove(slice_file)
        upload_file = FileInfo(
            full_filename=params.full_filename,
            filename=filename,
            extension=extension,
            md5=params.md5,
            path=os.path.join(file_path),
            size=os.path.getsize(file_path),
            file_type=const.FileType.UPLOAD
        )
        upload_file.save()
        return self.success_response(FileInfoSerial(upload_file).data)


class DownloadView(PermLessApiView):

    def get(self, request, md5):
        file = FileInfo.objects.get_or_none(md5=md5)
        if file is None:
            return self.fail_response('文件不存在')

        # 判断文件是否存在
        if not os.path.exists(file.path):
            raise ObjectNotFound('文件不存在')

        # 只读二进制返回文件流，文件会自动关闭
        return FileResponse(open(file.path, 'rb'), filename=file.full_filename, as_attachment=True)
