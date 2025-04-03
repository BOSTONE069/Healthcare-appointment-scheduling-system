from django.contrib import admin
from .models import Patient, Doctor, Appointment, MedicalRecord

class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'insurance_number', 'created_at')

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'available_from', 'available_to')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_time', 'status')

class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'appointment', 'created_at')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(MedicalRecord, MedicalRecordAdmin)
