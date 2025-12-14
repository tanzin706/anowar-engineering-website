#!/usr/bin/env bash
# Build script for Render deployment

set -o errexit  # Exit on error

echo "Building Django application..."

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Create superuser if it doesn't exist (using environment variables)
python manage.py create_superuser_if_missing

echo "Build completed successfully!"

