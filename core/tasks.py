from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_appointment_email(patient_email, doctor_name, appointment_time):
    subject = "Appointment Confirmation"
    message = f"Dear Patient, your appointment with Dr. {doctor_name} is confirmed for {appointment_time}."
    send_mail(subject, message, "admin@yourclinic.com", [patient_email])
