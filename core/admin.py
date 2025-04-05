from django.contrib import admin
from .models import Patient, Doctor, Appointment, MedicalRecord

# The `PatientAdmin` class defines the display fields for the admin interface of a patient model.
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'insurance_number', 'created_at')

# The `DoctorAdmin` class defines a Django admin model with fields for user, specialization, available
# from, and available to.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'available_from', 'available_to')

# The `AppointmentAdmin` class defines a Django admin model with specified fields for displaying
# appointment information.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_time', 'status')

# The `MedicalRecordAdmin` class defines a Django admin interface with specified fields for displaying
# patient medical records.
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'appointment', 'notes', 'created_at')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(MedicalRecord, MedicalRecordAdmin)
