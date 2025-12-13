# Quick Start Guide

## Initial Setup (First Time)

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment**:
   - Copy `env.example` to `.env`
   - Edit `.env` and set a secure `SECRET_KEY`
   - You can generate one using: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

3. **Create database and migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create your admin account.

5. **Create directories**:
   ```bash
   mkdir media
   mkdir static
   ```

6. **Run the server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the site**:
   - Website: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## Adding Content

1. Log in to the admin panel at `/admin/`

2. **Create Header**:
   - Go to "Headers" → "Add Header"
   - Upload a logo (optional) or use logo text
   - Set `is_active` to True
   - Save and add navigation items inline

3. **Create Hero Section**:
   - Go to "Hero Sections" → "Add Hero Section"
   - Add title, subtitle, and background image
   - Add CTA button text and URL
   - Set `is_active` to True

4. **Create About Section**:
   - Go to "About Sections" → "Add About Section"
   - Add title, content, and image
   - Set `is_active` to True

5. **Add Services**:
   - Go to "Services" → "Add Service"
   - Add multiple services with titles, descriptions, and images
   - Set `order` to control display order
   - Set `is_active` to True for each service

6. **Create Footer**:
   - Go to "Footers" → "Add Footer"
   - Add company information and contact details
   - Set `is_active` to True

## Tips

- Only one Header, Hero, About, and Footer with `is_active=True` will be displayed
- Multiple Services can be active at once
- Navigation items are added inline when editing a Header
- Use Bootstrap icon classes (e.g., `bi-gear`, `bi-tools`) for service icons
- Images are automatically resized and optimized by Django

