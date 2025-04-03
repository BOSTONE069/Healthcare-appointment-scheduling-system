# Project Title




## API Documentation
- Access the documentation through `http://127.0.0.1:8000/swagger/`

## Database Schema Diagram
- A diagram that illustrates the database schema, showing the relationships between different models.

<p style="align:center">
    <img src="DATABASE SCHEMA.png">
</p>

## Sequence Diagram
- A sequence diagram that outlines the interactions between different components of the system.
<p style="align:center">
    <img src="work/work.png">
</p>

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/BOSTONE069/Healthcare-appointment-scheduling-system
   ```
2. Navigate to the project directory:
   ```bash
   cd Healthcare-appointment-scheduling-system
   ```
3. Install the required packages:
   ```bash
   `pip install virtualenv`
   `myenv\Scripts\activate.bat` or `source myenv/bin/activate`
   `pip install -r requirements.txt`
   ```
4. Set up the environment variables in a `.env` file.
5. Run the migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
