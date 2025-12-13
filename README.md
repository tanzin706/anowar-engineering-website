# Company Website - Django Project

A clean, content-managed company website built with Django. All content can be managed through the Django admin interface without touching code.

## Features

- **Header/Navigation**: Editable logo and navigation menu items
- **Hero Section**: Customizable hero section with image and call-to-action
- **About Section**: Editable about content with image
- **Services Section**: Multiple service items with titles, descriptions, and images
- **Footer**: Editable contact information and company details
- **Admin Interface**: Full Django admin integration for all content
- **Bootstrap 5**: Modern, responsive design
- **Media Management**: Image uploads for all sections

## Project Structure

```
company_website/
├── company_website/          # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── website/                   # Main app
│   ├── models.py             # Content models
│   ├── admin.py              # Admin configuration
│   ├── views.py              # Views
│   └── templates/            # HTML templates
├── manage.py
├── requirements.txt
└── README.md
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Local Development Setup

1. **Clone or navigate to the project directory**

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies** (IMPORTANT: Do this first):
   ```bash
   pip install -r requirements.txt
   ```
   This installs Django, Pillow (for image handling), and other required packages.

5. **Set up environment variables**:
   - Copy `.env.example` to `.env`:
     ```bash
     copy .env.example .env  # Windows
     # or
     cp .env.example .env    # macOS/Linux
   ```
   - Edit `.env` and set your `SECRET_KEY` (generate one using Django's `get_random_secret_key()` or any secure random string generator)

6. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser** (to access admin):
   ```bash
   python manage.py createsuperuser
   ```

8. **Create media and static directories**:
   ```bash
   mkdir media
   mkdir static
   ```

9. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

10. **Access the site**:
    - Website: http://127.0.0.1:8000/
    - Admin: http://127.0.0.1:8000/admin/

## Using the Admin Interface

1. Log in to the admin panel at `/admin/`
2. Add content for each section:
   - **Header**: Add a header with logo and navigation items
   - **Hero Section**: Create a hero section with title, subtitle, and background image
   - **About Section**: Add about content with image
   - **Services**: Add multiple service items
   - **Footer**: Configure footer with contact information

3. Make sure to set `is_active=True` for the sections you want to display

## Deployment

### PythonAnywhere

1. **Upload your project**:
   - Use the Files tab to upload your project files
   - Or use Git to clone your repository

2. **Set up a virtual environment**:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.11 myenv
   workon myenv
   pip install -r requirements.txt
   ```

3. **Configure the web app**:
   - Go to Web tab
   - Set Source code path to your project directory
   - Set Working directory to your project directory
   - Set WSGI configuration file path

4. **Edit WSGI file**:
   ```python
   import os
   import sys
   
   path = '/home/yourusername/path/to/project'
   if path not in sys.path:
       sys.path.append(path)
   
   os.environ['DJANGO_SETTINGS_MODULE'] = 'company_website.settings'
   
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

5. **Set environment variables**:
   - In the Web tab, add environment variables:
     - `SECRET_KEY=your-secret-key`
     - `DEBUG=False`
     - `ALLOWED_HOSTS=yourusername.pythonanywhere.com`

6. **Run migrations**:
   ```bash
   python manage.py migrate
   python manage.py collectstatic
   ```

7. **Reload the web app**

### Render

1. **Create a new Web Service** on Render

2. **Connect your repository** or upload your code

3. **Configure Build & Start Commands**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn company_website.wsgi:application`

4. **Set Environment Variables**:
   - `SECRET_KEY`: Your Django secret key
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `your-app-name.onrender.com`

5. **Add PostgreSQL Database** (optional, recommended for production):
   - Create a PostgreSQL database
   - Update `settings.py` to use PostgreSQL
   - Add `DATABASE_URL` environment variable

6. **Deploy**

### Heroku

1. **Install Heroku CLI** and login

2. **Create a `Procfile`**:
   ```
   web: gunicorn company_website.wsgi --log-file -
   ```

3. **Create `runtime.txt`** (optional, specify Python version):
   ```
   python-3.11.4
   ```

4. **Initialize Git** (if not already):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

5. **Create Heroku app**:
   ```bash
   heroku create your-app-name
   ```

6. **Set environment variables**:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
   ```

7. **Deploy**:
   ```bash
   git push heroku main
   ```

8. **Run migrations**:
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

## Production Settings

For production, make sure to:

1. Set `DEBUG=False` in your environment variables
2. Set a strong `SECRET_KEY`
3. Configure `ALLOWED_HOSTS` with your domain
4. Use a production database (PostgreSQL recommended)
5. Set up proper static file serving (WhiteNoise is included)
6. Use HTTPS
7. Configure proper security headers

## Static Files

The project uses WhiteNoise for static file serving in production. To collect static files:

```bash
python manage.py collectstatic
```

## Media Files

Media files (uploaded images) are stored in the `media/` directory. For production:

- **PythonAnywhere**: Configure static files mapping in Web tab
- **Render/Heroku**: Consider using cloud storage (AWS S3, Cloudinary, etc.) for media files

## Customization

- **Styling**: Edit `website/templates/website/base.html` to customize CSS
- **Layout**: Modify templates in `website/templates/website/`
- **Models**: Add fields to models in `website/models.py` and run migrations

## Support

For issues or questions, please refer to Django documentation or create an issue in your repository.

## License

This project is open source and available for use.

