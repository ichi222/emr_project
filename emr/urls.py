from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('patient/<int:patient_id>/treatments/', views.treatment_list, name='treatment_list'),
    path('patient/<int:patient_id>/treatments/new/', views.treatment_create, name='treatment_create'),
    path('patient/<int:patient_id>/images/', views.medical_image_list, name='medical_image_list'),
    path('patient/<int:patient_id>/images/upload/', views.medical_image_upload, name='medical_image_upload'),
]
