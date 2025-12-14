# 🚀 Quick Start: Deploy to Render (5 Minutes)

## 1. Sign Up
- Go to https://render.com
- Click "Get Started for Free"
- Sign up with GitHub

## 2. Create Web Service
- Click "New +" → "Web Service"
- Select your GitHub repository
- Use these settings:

```
Name: anowar-engineering-website
Build Command: ./build.sh
Start Command: gunicorn company_website.wsgi:application
```

## 3. Add Environment Variables
Click "Advanced" and add:

```
PYTHON_VERSION = 3.11.4
SECRET_KEY = [generate using: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"]
DEBUG = False
ALLOWED_HOSTS = your-app-name.onrender.com
```

## 4. Deploy
- Select "Free" plan
- Click "Create Web Service"
- Wait 5-10 minutes

## 5. Create Admin User
- Go to "Shell" tab in Render dashboard
- Run: `python manage.py createsuperuser`

## ✅ Done!
Your site is live! Every GitHub push = automatic update!

**Full guide**: See `DEPLOYMENT.md` for detailed instructions.

