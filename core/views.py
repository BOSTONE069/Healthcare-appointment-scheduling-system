from rest_framework import viewsets
from .models import Patient, Doctor, Appointment, MedicalRecord
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer, MedicalRecordSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Appointment
from .serializers import AppointmentSerializer
from .tasks import send_appointment_email

# Patient ViewSet
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

# Doctor ViewSet
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

# Appointment ViewSet
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

# Medical Record ViewSet
class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticated]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ref_name = "UserSerializerViews"
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def book_appointment(request):
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        appointment = serializer.save(patient=request.user)

        # Trigger Celery Task
        send_appointment_email.delay(
            request.user.email,
            appointment.doctor.user.username,
            appointment.appointment_time
        )

        return Response({"message": "Appointment booked successfully!"}, status=201)
    return Response(serializer.errors, status=400)