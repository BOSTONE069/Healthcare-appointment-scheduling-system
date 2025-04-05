# Healthcare Appointment Scheduling System

![Healthcare Appointment System](https://img.shields.io/badge/Healthcare-Scheduling-blue)
![Django REST Framework](https://img.shields.io/badge/Backend-Django%20REST%20Framework-red)
![React.js](https://img.shields.io/badge/Frontend-React.js-9cf)

A **full-stack web application** built with **Django REST Framework (DRF)** and **React.js** to modernize medical appointment management. Designed for **patients, doctors, and administrators**, it simplifies booking, scheduling, and tracking healthcare visits.

---

## ✨ **Features**

### **For Patients**
- ✅ User registration & secure authentication (JWT).
- ✅ Search/filter doctors by specialty, availability, or location.
- ✅ Book, reschedule, or cancel appointments.
- ✅ Receive email/SMS notifications for confirmations & reminders.

### **For Doctors**
- ⚕️ Dashboard to manage appointments & availability.
- ⚕️ View patient history and appointment details.
- ⚕️ Set working hours and leave days.

### **For Admins**
- 🔒 Manage users (patients, doctors) and roles.
- 📊 Generate reports (appointments, revenue, etc.).
- 🛠️ Oversee system settings and troubleshoot issues.

---

## 🛠️ **Tech Stack**

| **Category**       | **Technologies**                          |
|--------------------|-------------------------------------------|
| **Backend**        | Django, Django REST Framework (DRF)       |
| **Database**       | PostgreSQL                                |
| **Frontend**       | React.js, Redux (or Context API)          |
| **Auth**           | JWT (JSON Web Tokens)                     |
| **API Docs**       | Swagger/OpenAPI (`drf-yasg`)              |
| **Styling**        | CSS3, Material-UI/Tailwind (optional)     |
| **Deployment**     | Docker, AWS/Heroku                        |

---

## 🚀 **Setup & Installation**

### Prerequisites
- Python 3.9+
- Node.js 16+
- PostgreSQL 13+
- Redis (optional for caching)

### **Backend (Django)**
1. Clone the repo:
   ```sh
   git clone https://github.com/your-repo/Healthcare-appointment-scheduling-system.git
   cd Healthcare-appointment-scheduling-system
   ```
2. Create and activate virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. Navigate to the project directory:
   ```bash
   cd Healthcare-appointment-scheduling-system
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up the environment variables in a `.env` file.
6. Run the migrations:
   ```bash
   python manage.py migrate
   ```
7. Create superuser
    ```bash
    python manage.py createsuperuser
    ```

8. Start the development server:
   ```bash
   python manage.py runserver

9. Start Celery worker:
    ```bash
    celery -A healthcare_system worker -l info
    ```

### **Front End (React)**

1. Navigate to the project directory:
    ```bash
    cd healthcare-frontend
    ```

2. Install dependencies
    ```bash
    npm install
    ```
3. Start development server
    ```bash
    npm start
    ```

## API Documentation
- API documentation is available via Swagger UI:
    ```bash
    http://127.0.0.1:8000/swagger/
    ```

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

- As shown in the screenshot below
<p style="align:center">
    <img src="apis.PNG">
</p>

## Database Schema Diagram
- A diagram that illustrates the database schema, showing the relationships between different models.
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

<p style="align:center">
    <img src="DATABASE SCHEMA 2.png">
</p>

## Sequence Diagram
- A sequence diagram that outlines the interactions between different components of the system.
<p style="align:center">
    <img src="out/work/Healthcare Appointment System Architecture.png">
</p>
## ⚙️ Configuration

### Environment Variables

Create a `.env` file in your backend directory with the following variables:

```ini
# Django Settings
DEBUG=True
SECRET_KEY=your-django-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration (PostgreSQL)
DATABASE_URL=postgres://username:password@localhost:5432/healthcare_db

# Email Settings (for notifications)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=Healthcare System <noreply@healthcare.com>

# JWT Authentication
JWT_SECRET_KEY=your-jwt-secret-key
ACCESS_TOKEN_LIFETIME=14400  # 4 hours
REFRESH_TOKEN_LIFETIME=2592000  # 30 days

# Frontend URL (for CORS)
FRONTEND_URL=http://localhost:3000

# Celery (for async tasks)
CELERY_BROKER_URL=redis://localhost:6379/0

#Email Configurations
EMAIL_HOST_USER=your email
EMAIL_HOST_PASSWORD=your password
```

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

## 🤝 Contributing

1. Fork the project
2. Create your feature branch
   ```sh
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes
   ```sh
   git commit -m 'Add some AmazingFeature'
   ```
4. Push to the branch
   ```sh
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📧 Contact

**OCHIENG BOSTONE**

Project Link: [https://github.com/BOSTONE069/Healthcare-appointment-scheduling-system](https://github.com/BOSTONE069/Healthcare-appointment-scheduling-system)