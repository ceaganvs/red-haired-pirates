# Red-Haired Pirates

Django website about Shanks from One Piece featuring crew member signup functionality.

## Prerequisites

- Python 3.8 or higher
- Docker and Docker Compose (for Docker deployment)

## Setup and Run Instructions

### Option 1: Using Virtual Environment (venv)

1. **Clone the repository**
   ```bash
   git clone https://github.com/ceaganvs/red-haired-pirates.git
   cd red-haired-pirates
   ```

2. **Create and activate virtual environment**
   
   On Windows:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to project directory**
   ```bash
   cd myproject
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   
   Open your browser and visit: `http://127.0.0.1:8000/`

9. **Deactivate virtual environment (when done)**
   ```bash
   deactivate
   ```

### Option 2: Using Docker

1. **Clone the repository**
   ```bash
   git clone https://github.com/ceaganvs/red-haired-pirates.git
   cd red-haired-pirates
   ```

2. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   
   Open your browser and visit: `http://127.0.0.1:8000/`

4. **Stop the containers**
   ```bash
   docker-compose down
   ```

## Security Notes

**Important:** This project uses Django's built-in SECRET_KEY for demonstration purposes. For production deployment:

1. **Generate a new SECRET_KEY:**
   ```python
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

2. **Set it as an environment variable:**
   
   On Windows:
   ```bash
   set DJANGO_SECRET_KEY=your-generated-secret-key-here
   ```
   
   On macOS/Linux:
   ```bash
   export DJANGO_SECRET_KEY=your-generated-secret-key-here
   ```

3. **Update settings.py** to use the environment variable:
   ```python
   SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'fallback-key-for-dev')
   ```

**Never commit passwords, API keys, or secret keys to public repositories.**

## Features

- Home page with Shanks biography
- About page with character background
- Contact page
- Join Crew - Database-driven signup system
- Crew Members - View all registered crew members

## Technology Stack

- Django 5.0.1
- SQLite3 database
- Bootstrap 5.3.2
- Docker support included
- Contact page
- SQLite3 database integration
- Bootstrap 5 responsive design
- Docker support

## Pages

- Home: `/`
- Biography: `/about/`
- Join Crew: `/join/`
- Crew Members: `/crew/`
- Contact: `/contact/`
- Admin: `/admin/`

## BTW

Bankai
