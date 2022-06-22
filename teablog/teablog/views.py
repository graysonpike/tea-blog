from django.shortcuts import render
from .models import PageView


BASE_META_KEYWORDS = "tea,blog,new york,new york city,nyc,reviews,matcha,green tea,high tea,scones"


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


def alices_tea_cup(request):
    record_pageview(request)
    return render(request, 'teablog/alices_tea_cup.html', {
        "title": "Alice's Tea Cup - NYC Tea Blog",
        "meta_description": "NYC Tea Blog review of Alice's Tea Cup on 102 W 73rd St, Upper West Side",
        "meta_keywords": BASE_META_KEYWORDS + ",alice's tea cup,alices tea cup,upper west side,alice tea cup,wonderland,alice in wonderland"
    })