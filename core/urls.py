from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PatientViewSet,
    DoctorViewSet,
    AppointmentViewSet,
    MedicalRecordViewSet,
    UserViewSet,
    book_appointment
)
router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'medical-records', MedicalRecordViewSet)
router.register(r'registrations', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('book-appointment/', book_appointment, name='book-appointment'),
]
