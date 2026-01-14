from django.shortcuts import render
from django.conf import settings
import requests

def index(request):
    total_responses = 0
    latest = []

    try:
        resp = requests.get(settings.API_URL, timeout=5)
        data = resp.json() if resp.status_code == 200 else []
        total_responses = len(data)
        latest = data[-5:] if total_responses >= 5 else data
    except Exception:
        total_responses = 0
        latest = []

    return render(request, "homepage/index.html", {
        "title": "Landing Dashboard",
        "total_responses": total_responses,
        "latest": latest,
    })
