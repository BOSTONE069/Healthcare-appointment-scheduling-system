import factory
from django.contrib.auth.models import User
from core.models import Patient, Doctor, Appointment, MedicalRecord
from datetime import datetime, timedelta
import random

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'testpass123')

class PatientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Patient

    user = factory.SubFactory(UserFactory)
    phone = factory.Sequence(lambda n: f'12345678{n:02d}')
    insurance_number = factory.Sequence(lambda n: f'INS{n:04d}')

class DoctorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Doctor

    user = factory.SubFactory(UserFactory, username=factory.Sequence(lambda n: f'dr_smith{n}'))
    specialization = factory.Iterator(['Cardiology', 'Neurology', 'Pediatrics', 'Dermatology', 'Oncology'])
    available_from = '09:00:00'
    available_to = '17:00:00'

class AppointmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Appointment

    patient = factory.SubFactory(PatientFactory)
    doctor = factory.SubFactory(DoctorFactory)
    appointment_time = factory.LazyFunction(lambda: datetime.now() + timedelta(days=random.randint(1, 30)))
    status = factory.Iterator(['Pending', 'Confirmed', 'Cancelled'])

class MedicalRecordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MedicalRecord

    patient = factory.SubFactory(PatientFactory)
    appointment = factory.SubFactory(AppointmentFactory, status='Confirmed')
    notes = factory.Iterator([
        'Regular checkup',
        'Follow-up visit',
        'Initial consultation',
        'Emergency visit',
        'Vaccination'
    ])
