from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('image_list/', views.image_list, name='image_list'),
    #path('images/<int:image_id>/', views.view_image, name='view_image'),
    path('images/<str:image_filename>/', views.view_image_by_filename, name='view_image_by_filename'),

]
