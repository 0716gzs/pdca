from rest_framework.fields import SerializerMethodField

from apps.upload.models import FileInfo
from common.serials import BaseSerializer


class FileInfoSerial(BaseSerializer):
    url_path = SerializerMethodField(method_name='get_url_path')

    class Meta:
        model = FileInfo
        fields = ('id', 'full_filename', 'filename', 'extension', 'md5', 'size', 'url_path')

    def get_url_path(self, obj):
        return 'pdca/download/' + obj.md5
