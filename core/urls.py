from django.urls import path
from .views import (
    PatientListCreateView, PatientDetailView,
    DoctorListCreateView, DoctorDetailView,
    PatientDoctorMappingListCreateView, PatientDoctorMappingDetailView,
    PatientDoctorsListView
)

urlpatterns = [
    path('patients/', PatientListCreateView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('mappings/', PatientDoctorMappingListCreateView.as_view(), name='mapping-list'),
    path('mappings/<int:pk>/', PatientDoctorMappingDetailView.as_view(), name='mapping-detail'),
    path('mappings/patient/<int:patient_id>/', PatientDoctorsListView.as_view(), name='patient-doctors'),
]