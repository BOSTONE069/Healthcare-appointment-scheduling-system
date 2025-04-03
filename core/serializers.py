from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient, Doctor, Appointment, MedicalRecord

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Patient Serializer
class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = '__all__'

    def create(self, validated_data):
        # Extract the user data from the validated data
        user_data = validated_data.pop('user')

        # Create the User object first
        user = User.objects.create(**user_data)

        # Create the Patient object using the newly created user
        patient = Patient.objects.create(user=user, **validated_data)

        return patient


# Doctor Serializer
class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = '__all__'

# Appointment Serializer
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

# Medical Record Serializer
class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'
