from django.shortcuts import render
# from django.shortcuts import HttpResponse
import requests
# gTTS


def index(request):
    return render(request, 'index.html')


def temperature(request):

    city = str(request.GET.get('city'))
    # print(type(request.GET.get('city')))
    api_key = "7e957b297e464cb4ae8ecaaeb63b3b4c"

    # headers = {'Authorization': 'Bearer {}'.format(api_key)}

    search_api_url = 'http://api.weatherbit.io/v2.0/current'
    endpoints = {
        'city': city,
        'key': api_key
    }
    response = requests.get(search_api_url, timeout=5, params=endpoints)

    response_json = response.json()
    print(response_json)
    # print("Response URL", response.url)
    # print("Response status code ", response.status_code)
    # print(response.headers)
    params = {"content": "Temperature in ", "city": city, "temp": response_json['data'][0]['temp'],
              'weather_desc': response_json['data'][0]['weather']['description'], 'day': response_json['data'][0]['pod']}

    return render(request, 'temperature.html', params)
