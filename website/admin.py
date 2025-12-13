from django.contrib import admin
from .models import (
    Header,
    NavigationItem,
    HeroSection,
    AboutSection,
    Service,
    Fact,
    Product,
    Footer,
)


class NavigationItemInline(admin.TabularInline):
    model = NavigationItem
    extra = 1
    fields = ("label", "url", "order", "is_active")


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ("logo_text", "is_active", "created_at", "updated_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("logo_text",)
    inlines = [NavigationItemInline]
    fieldsets = (("Header Settings", {"fields": ("logo", "logo_text", "is_active")}),)


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at", "updated_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("title", "subtitle")
    fieldsets = (
        ("Content", {"fields": ("title", "subtitle", "background_image")}),
        ("Call to Action", {"fields": ("cta_text", "cta_url")}),
        ("Settings", {"fields": ("is_active",)}),
    )


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at", "updated_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("title", "content")
    fieldsets = (("Content", {"fields": ("title", "content", "image", "is_active")}),)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("title", "description")
    list_editable = ("order", "is_active")
    fieldsets = (
        (
            "Service Information",
            {"fields": ("title", "description", "image", "icon_class")},
        ),
        ("Display Settings", {"fields": ("order", "is_active")}),
    )


@admin.register(Fact)
class FactAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at", "updated_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("title", "content")
    fieldsets = (("Content", {"fields": ("title", "content", "image", "is_active")}),)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("name", "description")
    list_editable = ("is_active",)
    fieldsets = (
        (
            "Product Information",
            {"fields": ("name", "description", "image", "icon_class")},
        ),
        ("Links", {"fields": ("link",)}),
        ("Settings", {"fields": ("is_active",)}),
    )


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ("company_name", "phone", "email", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("company_name", "email", "phone")
    fieldsets = (
        (
            "Company Information",
            {"fields": ("company_name", "address", "phone", "email", "website")},
        ),
        ("Copyright", {"fields": ("copyright_text",)}),
        ("Settings", {"fields": ("is_active",)}),
    )
