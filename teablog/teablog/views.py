from django.shortcuts import render
from .models import PageView


BASE_META_KEYWORDS = "nyc, tea, blog, reviews, matcha, green tea"


def record_pageview(request):
    # Note: HTTP_X_FORWARDED_FOR is not present in headers given by the Django development server
    http_x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    PageView.objects.create(
        ip=http_x_forwarded_for,
        path=request.path
    )


def landing(request):
    record_pageview(request)
    return render(request, 'teablog/landing.html', {
        "title": "NYC Tea Blog",
        "meta_description": "A blog exploring the tea houses of New York City",
        "meta_keywords": BASE_META_KEYWORDS
    })