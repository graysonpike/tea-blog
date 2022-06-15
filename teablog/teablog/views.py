from django.shortcuts import render
from .models import PageView


BASE_META_KEYWORDS = "nyc, tea, blog, reviews, matcha, green tea"


def record_pageview(request):
    ip_from_proxy = request.META.get('REMOTE_ADDR')
    http_x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    PageView.objects.create(
        ip_from_proxy=ip_from_proxy,
        http_x_forwarded_for=http_x_forwarded_for,
        path=request.path
    )


def landing(request):
    record_pageview(request)
    return render(request, 'teablog/landing.html', {
        "title": "NYC Tea Blog",
        "meta_description": "A blog exploring the tea houses of New York City",
        "meta_keywords": BASE_META_KEYWORDS
    })