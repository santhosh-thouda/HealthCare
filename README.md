# Healthcare Backend API

A Django REST Framework API for managing healthcare data including patients, doctors, and their relationships.

## Features

- **User Authentication**: JWT-based authentication with custom User model
- **Patient Management**: CRUD operations for patient records
- **Doctor Management**: CRUD operations for doctor profiles
- **Patient-Doctor Mapping**: Assign doctors to patients with notes
- **RESTful API**: Clean REST API endpoints with proper permissions

## Project Structure

```
healthcare_backend/
├── authentication/          # User authentication app
│   ├── models.py           # Custom User model
│   ├── serializers.py      # User registration/login serializers
│   ├── views.py            # Authentication views
│   └── urls.py             # Authentication URLs
├── core/                   # Main healthcare app
│   ├── models.py           # Patient, Doctor, and mapping models
│   ├── serializers.py      # Data serializers
│   ├── views.py            # API views
│   ├── permissions.py      # Custom permissions
│   └── urls.py             # Core API URLs
├── healthcare/             # Django project settings
│   ├── settings.py         # Project configuration
│   └── urls.py             # Main URL configuration
└── manage.py               # Django management script
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd healthcare_backend
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   
   **Option A: PostgreSQL (Recommended)**
   - Install PostgreSQL from https://www.postgresql.org/download/
   - Create database: `createdb healthcare_db`
   - Update database credentials in `healthcare/settings.py` if needed
   
   **Option B: SQLite (Fallback)**
   - No additional setup required
   - Database will be created automatically

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication

- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/token/refresh/` - Refresh JWT token

### Patients

- `GET /api/patients/` - List all patients (authenticated users only)
- `POST /api/patients/` - Create new patient
- `GET /api/patients/{id}/` - Get patient details
- `PUT /api/patients/{id}/` - Update patient
- `DELETE /api/patients/{id}/` - Delete patient

### Doctors

- `GET /api/doctors/` - List all doctors
- `POST /api/doctors/` - Create new doctor profile
- `GET /api/doctors/{id}/` - Get doctor details
- `PUT /api/doctors/{id}/` - Update doctor
- `DELETE /api/doctors/{id}/` - Delete doctor

### Patient-Doctor Mappings

- `GET /api/mappings/` - List all mappings
- `POST /api/mappings/` - Create new mapping
- `GET /api/mappings/{id}/` - Get mapping details
- `DELETE /api/mappings/{id}/` - Delete mapping
- `GET /api/mappings/patient/{patient_id}/` - Get doctors for specific patient

## Usage Examples

### 1. User Registration

```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "testuser",
    "password": "password123"
  }'
```

### 2. User Login

```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "password123"
  }'
```

### 3. Create Patient (with authentication)

```bash
curl -X POST http://127.0.0.1:8000/api/patients/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "first_name": "John",
    "last_name": "Doe",
    "date_of_birth": "1990-01-01",
    "gender": "M",
    "contact_number": "+1234567890",
    "address": "123 Main St, City, State",
    "medical_history": "No known allergies"
  }'
```

### 4. Create Doctor Profile

```bash
curl -X POST http://127.0.0.1:8000/api/doctors/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "first_name": "Jane",
    "last_name": "Smith",
    "specialization": "CARDIOLOGY",
    "contact_number": "+1234567891",
    "address": "456 Medical Center, City, State",
    "license_number": "MD123456",
    "years_of_experience": 10
  }'
```

### 5. Assign Doctor to Patient

```bash
curl -X POST http://127.0.0.1:8000/api/mappings/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "patient": 1,
    "doctor": 1,
    "notes": "Primary care physician assignment"
  }'
```

## Models

### User Model
- Custom user model with email as username
- Includes all standard Django user fields
- Uses email for authentication

### Patient Model
- Personal information (name, DOB, gender, contact)
- Medical history
- Linked to User model
- Timestamps for creation and updates

### Doctor Model
- Professional information (name, specialization, license)
- Contact details and experience
- Linked to User model
- Specialization choices include various medical fields

### PatientDoctorMapping Model
- Links patients to doctors
- Includes assignment date and notes
- Unique constraint on patient-doctor pairs

## Permissions

- **IsAuthenticated**: Required for all API endpoints
- **IsOwner**: Users can only access their own patients
- **IsOwnerOrReadOnly**: Users can read all doctors but only modify their own

## Testing

Run the test script to verify the API:

```bash
python test_api.py
```

## Admin Interface

Access the Django admin interface at `http://127.0.0.1:8000/admin/` with your superuser credentials.

## Configuration

The project uses SQLite by default. To use PostgreSQL, update the `DATABASES` setting in `healthcare/settings.py` and install `psycopg2-binary`.

## Security Notes

- Change the `SECRET_KEY` in production
- Set `DEBUG = False` in production
- Use environment variables for sensitive data
- Implement proper CORS settings for frontend integration

## Dependencies

- **Django 5.2.6** - Web framework
- **Django REST Framework 3.16.1** - API framework
- **djangorestframework-simplejwt 5.5.1** - JWT authentication
- **psycopg2-binary 2.9.10** - PostgreSQL adapter
- **python-dotenv 1.1.1** - Environment variables
- **django-cors-headers 4.3.1** - CORS support
- **whitenoise 6.6.0** - Static file serving

## License

This project is for educational purposes.
