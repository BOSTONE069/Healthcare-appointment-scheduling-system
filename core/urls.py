from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, DoctorViewSet, AppointmentViewSet, MedicalRecordViewSet, UserViewSet

# The code snippet is setting up a router using the `DefaultRouter` class provided by Django REST
# framework. It then registers different view sets to specific endpoints on the router.
router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'medical-records', MedicalRecordViewSet)
router.register(r'registrations', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
