"""
Management command to create a superuser if one doesn't exist.
Uses environment variables for credentials.
Safe to run multiple times - won't create duplicate superusers.
"""

import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Creates a superuser if one does not exist (uses environment variables)"

    def handle(self, *args, **options):
        # Check if any superuser exists
        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write(
                self.style.SUCCESS("Superuser already exists. Skipping creation.")
            )
            return

        # Get credentials from environment variables
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if not password:
            self.stdout.write(
                self.style.WARNING(
                    "DJANGO_SUPERUSER_PASSWORD not set. "
                    "Skipping superuser creation. "
                    "You can create one manually later via admin interface."
                )
            )
            return

        # Create superuser
        try:
            User.objects.create_superuser(
                username=username, email=email, password=password
            )
            self.stdout.write(
                self.style.SUCCESS(f"Successfully created superuser: {username}")
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error creating superuser: {str(e)}"))
