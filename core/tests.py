from django.test import TestCase
from .models import Doctor, Appointment, Patient, MedicalRecord
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.db import IntegrityError
import pytest
from datetime import datetime, timedelta

class PatientModelTest(TestCase):
    def test_create_patient_with_valid_data(self):
        # Create a user
        user = User.objects.create_user(
            username='Bostone',
            email='bostone@gmail.com',
            password='password123'
        )

        # Create a patient with valid data
        patient = Patient.objects.create(
            user=user,
            phone='1234567890',
            insurance_number='INS12345'
        )

        # Assert patient was created correctly
        assert patient.user == user
        assert patient.phone == '1234567890'
        assert patient.insurance_number == 'INS12345'
        assert patient.created_at is not None

    def test_create_patient_with_duplicate_phone(self):
        # Create first user and patient
        user1 = User.objects.create_user(
            username='Bostone1',
            email='bostone1@gmail.com',
            password='password123'
        )

        Patient.objects.create(
            user=user1,
            phone='1234567890',
            insurance_number='INS12345'
        )

        # Create second user
        user2 = User.objects.create_user(
            username='Bostone2',
            email='bostone2@gmail.com',
            password='password123'
        )

        # Attempt to create patient with duplicate phone
        with pytest.raises(IntegrityError):
            Patient.objects.create(
                user=user2,
                phone='1234567890',  # Same phone as first patient
                insurance_number='INS67890'
            )

class DoctorModelTest(TestCase):
    def test_create_doctor_with_valid_data(self):
        user = User.objects.create_user(
            username='dr_smith',
            email='dr.smith@gmail.com',
            password='password123'
        )
        doctor = Doctor.objects.create(
            user=user,
            specialization='Cardiology',
            available_from='09:00:00',
            available_to='17:00:00'
        )
        assert doctor.user == user
        assert doctor.specialization == 'Cardiology'
        assert str(doctor.available_from) == '09:00:00'
        assert str(doctor.available_to) == '17:00:00'

class AppointmentModelTest(TestCase):
    def setUp(self):
        self.patient_user = User.objects.create_user(
            username='patient1',
            email='patient1@gmail.com',
            password='password123'
        )
        self.patient = Patient.objects.create(
            user=self.patient_user,
            phone='1234567890',
            insurance_number='INS12345'
        )
        self.doctor_user = User.objects.create_user(
            username='doctor1',
            email='doctor1@gmail.com',
            password='password123'
        )
        self.doctor = Doctor.objects.create(
            user=self.doctor_user,
            specialization='Neurology',
            available_from='09:00:00',
            available_to='17:00:00'
        )

    def test_create_appointment(self):
        appointment_time = datetime.now() + timedelta(days=1)
        appointment = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            appointment_time=appointment_time,
            status='Pending'
        )
        assert appointment.patient == self.patient
        assert appointment.doctor == self.doctor
        assert appointment.status == 'Pending'

class MedicalRecordModelTest(TestCase):
    def setUp(self):
        # Create test data similar to AppointmentModelTest
        self.patient_user = User.objects.create_user(
            username='patient1',
            email='patient1@gmail.com',
            password='password123'
        )
        self.patient = Patient.objects.create(
            user=self.patient_user,
            phone='1234567890',
            insurance_number='INS12345'
        )
        self.doctor_user = User.objects.create_user(
            username='doctor1',
            email='doctor1@gmail.com',
            password='password123'
        )
        self.doctor = Doctor.objects.create(
            user=self.doctor_user,
            specialization='Neurology',
            available_from='09:00:00',
            available_to='17:00:00'
        )
        self.appointment = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            appointment_time=datetime.now() + timedelta(days=1),
            status='Confirmed'
        )

    def test_create_medical_record(self):
        record = MedicalRecord.objects.create(
            patient=self.patient,
            appointment=self.appointment,
            notes='Patient complained of headaches'
        )
        assert record.patient == self.patient
        assert record.appointment == self.appointment
        assert record.notes == 'Patient complained of headaches'

class APITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@gmail.com',
            password='adminpass'
        )
        self.client.force_authenticate(user=self.admin_user)

    def test_patient_api(self):
        url = reverse('patient-list')
        data = {
            'user': {
                'username': 'testpatient',
                'email': 'patient@gmail.com',
                'password': 'testpass123'
            },
            'phone': '9876543210',
            'insurance_number': 'TESTINS123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_doctor_api(self):
        url = reverse('doctor-list')
        data = {
            'user': {
                'username': 'testdoctor',
                'email': 'doctor@gmail.com',
                'password': 'testpass123'
            },
            'specialization': 'Pediatrics',
            'available_from': '08:00:00',
            'available_to': '16:00:00'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify both User and Doctor were created
        self.assertTrue(User.objects.filter(username='testdoctor').exists())
        doctor = Doctor.objects.get(user__username='testdoctor')
        self.assertEqual(doctor.specialization, 'Pediatrics')
        self.assertEqual(str(doctor.available_from), '08:00:00')
        self.assertEqual(str(doctor.available_to), '16:00:00')

    def test_appointment_api(self):
        # Create required patient and doctor first
        patient_user = User.objects.create_user(
            username='aptpatient',
            email='aptpatient@gmail.com',
            password='testpass123'
        )
        patient = Patient.objects.create(
            user=patient_user,
            phone='1112223333',
            insurance_number='APTINS123'
        )
        doctor_user = User.objects.create_user(
            username='aptdoctor',
            email='aptdoctor@gmail.com',
            password='testpass123'
        )
        doctor = Doctor.objects.create(
            user=doctor_user,
            specialization='Oncology',
            available_from='10:00:00',
            available_to='18:00:00'
        )

        url = reverse('appointment-list')
        data = {
            'patient': patient.id,
            'doctor': doctor.id,
            'appointment_time': (datetime.now() + timedelta(days=2)).isoformat(),
            'status': 'Pending'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_book_appointment_endpoint(self):
        # Create test doctor
        doctor_user = User.objects.create_user(
            username='bookdoctor',
            email='bookdoctor@gmail.com',
            password='testpass123'
        )
        doctor = Doctor.objects.create(
            user=doctor_user,
            specialization='Dermatology',
            available_from='09:00:00',
            available_to='17:00:00'
        )

        # Create test patient user and authenticate
        patient_user = User.objects.create_user(
            username='bookpatient',
            email='bookpatient@gmail.com',
            password='testpass123'
        )
        self.client.force_authenticate(user=patient_user)
        patient = Patient.objects.create(
            user=patient_user,
            phone='4445556666',
            insurance_number='BOOKINS123'
        )

        url = reverse('book-appointment')
        data = {
            'doctor': doctor.id,
            'appointment_time': (datetime.now() + timedelta(days=1)).isoformat(),
            'status': 'Pending'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
