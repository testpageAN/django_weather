from django.shortcuts import render


def home(request):
    import json
    import requests

    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=BCCECF5B-A827-4931-8E0D-AA3DDF3A7273")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})