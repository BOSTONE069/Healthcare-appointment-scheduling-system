# Healthcare System Backend Documentation

## API Endpoints

### Authentication
- `POST /registrations/` - Register new user
- `POST /api/token/` - Obtain JWT tokens (login)

### Patients
- `GET /patients/` - List all patients
- `POST /patients/` - Create new patient
- `GET /patients/{id}/` - Retrieve patient details
- `PUT /patients/{id}/` - Update patient
- `DELETE /patients/{id}/` - Delete patient

### Doctors
- `GET /doctors/` - List all doctors
- `POST /doctors/` - Create new doctor
- `GET /doctors/{id}/` - Retrieve doctor details
- `PUT /doctors/{id}/` - Update doctor
- `DELETE /doctors/{id}/` - Delete doctor

### Appointments
- `GET /appointments/` - List all appointments
- `POST /appointments/` - Create new appointment
- `POST /book-appointment/` - Special endpoint for booking appointments
- `GET /appointments/{id}/` - Retrieve appointment details
- `PUT /appointments/{id}/` - Update appointment
- `DELETE /appointments/{id}/` - Delete appointment

### Medical Records
- `GET /medical-records/` - List all medical records
- `POST /medical-records/` - Create new record
- `GET /medical-records/{id}/` - Retrieve record details
- `PUT /medical-records/{id}/` - Update record
- `DELETE /medical-records/{id}/` - Delete record

## Data Models

### User
- `username` - Unique identifier
- `email` - Email address
- `password` - Hashed password

### Patient
- `user` - OneToOne to User
- `phone` - Contact number
- `insurance_number` - Insurance identifier
- `created_at` - Timestamp

### Doctor
- `user` - OneToOne to User
- `specialization` - Medical specialty
- `available_from` - Start of availability
- `available_to` - End of availability

### Appointment
- `patient` - ForeignKey to Patient
- `doctor` - ForeignKey to Doctor
- `appointment_time` - Scheduled datetime
- `status` - Pending/Confirmed/Cancelled

### MedicalRecord
- `patient` - ForeignKey to Patient
- `appointment` - ForeignKey to Appointment
- `notes` - Medical notes
- `created_at` - Timestamp

## Authentication Flow
1. User registers via `/registrations/`
2. User logs in via `/api/token/` to get JWT
3. JWT included in Authorization header for protected endpoints
4. Tokens automatically refreshed when expired

## Error Handling
- 400 Bad Request - Invalid input data
- 401 Unauthorized - Missing/invalid credentials
- 403 Forbidden - Insufficient permissions
- 404 Not Found - Resource doesn't exist
- 500 Server Error - Internal server error

## Celery Tasks
- `send_appointment_email` - Sends confirmation email when appointment is booked

## Setup Instructions
1. Install requirements: `pip install -r requirements.txt`
2. Run migrations: `python manage.py migrate`
3. Start server: `python manage.py runserver`
4. Start Celery worker: `celery -A healthcare_system worker -l info`
