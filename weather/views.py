from django.shortcuts import render
import requests
# Create your views here.
def home(request):

    url= 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=f6a2db50ce45d87de65cf404b5b8983e'
    city= 'China'

    # request the json data and convert it into Python data_types
    city_weather=requests.get(url.format(city)).json()

    # Dictionary for getting api objects
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }


    context = {'weather' : weather}
    return render(request,"home.html", context)
