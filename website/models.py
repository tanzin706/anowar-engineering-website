from django.db import models
from django.core.validators import MinLengthValidator


class Header(models.Model):
    """Header configuration with logo and navigation"""

    logo = models.ImageField(
        upload_to="header/", blank=True, null=True, help_text="Company logo"
    )
    logo_text = models.CharField(
        max_length=100,
        default="Company Name",
        help_text="Text to display if no logo image",
    )
    is_active = models.BooleanField(
        default=True, help_text="Only one active header will be displayed"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Header"
        verbose_name_plural = "Headers"
        ordering = ["-is_active", "-created_at"]

    def __str__(self):
        return f"Header ({'Active' if self.is_active else 'Inactive'})"


class NavigationItem(models.Model):
    """Navigation menu items"""

    header = models.ForeignKey(
        Header, on_delete=models.CASCADE, related_name="nav_items"
    )
    label = models.CharField(max_length=50, help_text="Menu item label")
    url = models.CharField(
        max_length=200, default="#", help_text="URL or anchor (e.g., #about, /page/)"
    )
    order = models.IntegerField(
        default=0, help_text="Display order (lower numbers appear first)"
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Navigation Item"
        verbose_name_plural = "Navigation Items"
        ordering = ["order", "label"]

    def __str__(self):
        return self.label


class HeroSection(models.Model):
    """Hero section with image and text"""

    title = models.CharField(max_length=200, help_text="Main hero title")
    subtitle = models.TextField(blank=True, help_text="Subtitle or description text")
    background_image = models.ImageField(
        upload_to="hero/", blank=True, null=True, help_text="Hero background image"
    )
    cta_text = models.CharField(
        max_length=50, blank=True, help_text="Call-to-action button text"
    )
    cta_url = models.CharField(
        max_length=200, default="#contact", help_text="CTA button URL"
    )
    is_active = models.BooleanField(
        default=True, help_text="Only one active hero will be displayed"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"
        ordering = ["-is_active", "-created_at"]

    def __str__(self):
        return self.title


class AboutSection(models.Model):
    """About section with content and image"""

    title = models.CharField(max_length=200, default="About Us")
    content = models.TextField(help_text="About section content (HTML allowed)")
    image = models.ImageField(
        upload_to="about/", blank=True, null=True, help_text="About section image"
    )
    is_active = models.BooleanField(
        default=True, help_text="Only one active about section will be displayed"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Sections"
        ordering = ["-is_active", "-created_at"]

    def __str__(self):
        return self.title


class Service(models.Model):
    """Service items for the services section"""

    title = models.CharField(max_length=200, help_text="Service title")
    description = models.TextField(help_text="Service description")
    image = models.ImageField(
        upload_to="services/",
        blank=True,
        null=True,
        help_text="Service image (optional)",
    )
    icon_class = models.CharField(
        max_length=100, blank=True, help_text="Bootstrap icon class (e.g., 'bi-gear')"
    )
    order = models.IntegerField(
        default=0, help_text="Display order (lower numbers appear first)"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["order", "title"]

    def __str__(self):
        return self.title


class Fact(models.Model):
    """Facts section with content and image"""

    title = models.CharField(
        max_length=200, default="Our Achievements", help_text="Facts section title"
    )
    content = models.TextField(
        default="", blank=True, help_text="Facts section content (HTML allowed)"
    )
    image = models.ImageField(
        upload_to="facts/",
        blank=True,
        null=True,
        help_text="Facts section image",
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Only one active facts section will be displayed",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Facts Section"
        verbose_name_plural = "Facts Sections"
        ordering = ["-is_active", "-created_at"]

    def __str__(self):
        return self.title


class Product(models.Model):
    """Product items for the products section"""

    name = models.CharField(max_length=200, help_text="Product name")
    description = models.TextField(help_text="Product description")
    image = models.ImageField(
        upload_to="products/", blank=True, null=True, help_text="Product image"
    )
    link = models.URLField(
        blank=True, help_text="Link to product page or details (optional)"
    )
    icon_class = models.CharField(
        max_length=100, blank=True, help_text="Bootstrap icon class (e.g., 'bi-box')"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["created_at", "name"]

    def __str__(self):
        return self.name


class Footer(models.Model):
    """Footer with contact information"""

    company_name = models.CharField(max_length=100, default="Company Name")
    address = models.TextField(blank=True, help_text="Company address")
    phone = models.CharField(max_length=50, blank=True, help_text="Phone number")
    email = models.EmailField(blank=True, help_text="Email address")
    website = models.URLField(blank=True, help_text="Website URL")
    copyright_text = models.CharField(
        max_length=200, default="© 2024 Company Name. All rights reserved."
    )
    is_active = models.BooleanField(
        default=True, help_text="Only one active footer will be displayed"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footers"
        ordering = ["-is_active", "-created_at"]

    def __str__(self):
        return f"Footer - {self.company_name}"
