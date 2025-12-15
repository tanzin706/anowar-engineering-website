"""
Django management command to export the website to static HTML files.
This generates a static version of the site that can be hosted on GitHub Pages, Netlify, etc.
"""

import os
import shutil
from pathlib import Path
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django.conf import settings
from website.models import (
    Header,
    HeroSection,
    AboutSection,
    Service,
    Fact,
    Product,
    Footer,
)


class Command(BaseCommand):
    help = "Export the Django website to static HTML files"

    def add_arguments(self, parser):
        parser.add_argument(
            "--output-dir",
            type=str,
            default="static_site",
            help="Output directory for static files (default: static_site)",
        )

    def handle(self, *args, **options):
        output_dir = Path(options["output_dir"])

        self.stdout.write(
            self.style.SUCCESS(f"Starting static site export to {output_dir}...")
        )

        # Create output directory
        output_dir.mkdir(exist_ok=True)

        # Create media directory in output
        media_dir = output_dir / "media"
        media_dir.mkdir(exist_ok=True)

        # Copy media files
        self.stdout.write("Copying media files...")
        source_media = Path(settings.MEDIA_ROOT)
        if source_media.exists():
            for root, dirs, files in os.walk(source_media):
                for file in files:
                    src = Path(root) / file
                    rel_path = src.relative_to(source_media)
                    dst = media_dir / rel_path
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dst)

        # Get data from database
        header = Header.objects.filter(is_active=True).first()
        heroes = HeroSection.objects.filter(is_active=True).order_by("-created_at")
        about = AboutSection.objects.filter(is_active=True).first()
        services = Service.objects.filter(is_active=True).order_by("order")
        facts = Fact.objects.filter(is_active=True).first()
        products = Product.objects.filter(is_active=True)
        footer = Footer.objects.filter(is_active=True).first()

        # Prepare context
        context = {
            "header": header,
            "heroes": heroes,
            "about": about,
            "services": services,
            "facts": facts,
            "products": products,
            "footer": footer,
        }

        # Render the full page using Django templates
        self.stdout.write("Generating HTML files...")
        html_content = render_to_string("website/home.html", context)

        # Replace Django media URLs with relative paths
        html_content = html_content.replace("/media/", "media/")

        # Write index.html
        index_file = output_dir / "index.html"
        with open(index_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        self.stdout.write(self.style.SUCCESS(f"Generated {index_file}"))
        self.stdout.write(
            self.style.SUCCESS(f"\nStatic site exported successfully to {output_dir}/")
        )
        self.stdout.write(
            self.style.SUCCESS(
                "You can now commit this directory to GitHub for GitHub Pages deployment."
            )
        )
