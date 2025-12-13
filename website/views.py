from django.shortcuts import render
from .models import Header, HeroSection, AboutSection, Service, Fact, Product, Footer


def home(request):
    """Home page view"""
    # Get active sections
    header = Header.objects.filter(is_active=True).first()
    heroes = HeroSection.objects.filter(is_active=True).order_by("-created_at")
    about = AboutSection.objects.filter(is_active=True).first()
    services = Service.objects.filter(is_active=True).order_by("order")
    facts = Fact.objects.filter(is_active=True).first()
    products = Product.objects.filter(is_active=True)
    footer = Footer.objects.filter(is_active=True).first()

    context = {
        "header": header,
        "heroes": heroes,
        "about": about,
        "services": services,
        "facts": facts,
        "products": products,
        "footer": footer,
    }

    return render(request, "website/home.html", context)
