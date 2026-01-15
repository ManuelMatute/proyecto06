from django.shortcuts import render
from firebase_admin import db

LANDING_COLLECTION = "leads"

def index(request):
    data_dict = db.reference(LANDING_COLLECTION).get() or {}

    posts = []
    # Firebase dict: {id: {obj}}
    for key, value in data_dict.items():
        if isinstance(value, dict):
            value["id"] = key
            posts.append(value)

    total_responses = len(posts)
    latest = posts[:5]

    return render(request, "homepage/index.html", {
        "title": "Landing Dashboard",
        "total_responses": total_responses,
        "latest": latest,
    })
