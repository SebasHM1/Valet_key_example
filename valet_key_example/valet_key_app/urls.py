from django.urls import path
from . import views

urlpatterns = [
    path('', views.request_key, name='request_key'),
    path('download/<uuid:key>/', views.download_file, name='download_file'),
    path("check_key/<uuid:key>/", views.check_key_status, name="check_key_status"),
]
