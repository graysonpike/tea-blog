from django.shortcuts import render
from .models import PageView


BASE_META_KEYWORDS = "nyc, tea, blog, reviews, matcha, green tea"


def record_pageview(request):
    # Note: HTTP_X_FORWARDED_FOR is not present in headers given by the Django development server
    PageView.objects.create(
        ip=request.META.get('HTTP_X_FORWARDED_FOR'),
        user_agent=request.META.get('HTTP_USER_AGENT'),
        path=request.path
    )


def landing(request):
    record_pageview(request)
    return render(request, 'teablog/landing.html', {
        "title": "NYC Tea Blog",
        "meta_description": "A blog exploring the tea houses of New York City",
        "meta_keywords": BASE_META_KEYWORDS
    })