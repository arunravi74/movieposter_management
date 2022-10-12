from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('register/', views.sign_up,name="register"),
    path('update-profile/',views.profile,name="update_profile"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('upload-image',views.image_upload,name="upload_image")
]
