from django.contrib.auth.models import User
from django.db import models

# The `Patient` class defines a model with fields for user, phone number, insurance number, and
# creation timestamp.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, unique=True)
    insurance_number = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


# The `Doctor` class represents a model for storing information about doctors, including their user
# account, specialization, and availability times.
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    available_from = models.TimeField()
    available_to = models.TimeField()

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} ({self.specialization})"


# The `Appointment` class defines a model with fields for patient, doctor, appointment time, and
# status in a Django application.
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')])

    def __str__(self):
        return f"{self.patient} with {self.doctor} on {self.appointment_time.strftime('%Y-%m-%d %H:%M')}"


# The `MedicalRecord` class represents a medical record associated with a patient's appointment,
# including notes and creation timestamp.
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Record for {self.patient} on {self.appointment.appointment_time.strftime('%Y-%m-%d')}"
