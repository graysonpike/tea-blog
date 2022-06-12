from django.shortcuts import render


BASE_META_KEYWORDS = "nyc, tea, blog, reviews, matcha, green tea"


def landing(request):
    return render(request, 'teablog/landing.html', {
        "title": "NYC Tea Blog",
        "meta_description": "A blog exploring the tea houses of New York City",
        "meta_keywords": BASE_META_KEYWORDS
    })