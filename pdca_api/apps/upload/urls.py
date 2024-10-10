from django.urls import path, re_path

from apps.upload import views

upload_file_urls = [
    path("api/v1/upload/file/check", views.UploadFileCheckView.as_view()),
    path("api/v1/upload/file/slice", views.UploadFileSliceView.as_view()),
    path("api/v1/upload/file/merge", views.UploadFileMergeView.as_view()),
    re_path(r'^api/v1/download/(?P<md5>.*)$', views.DownloadView.as_view()),
]
