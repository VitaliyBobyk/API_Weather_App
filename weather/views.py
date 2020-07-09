from django.shortcuts import render
import requests
from django.views.generic.base import View


class Test(View):
    def get(self, request):
        try:
            appid = 'd4d6b0bfecbeb4c1467c499c6557acd1'
            city = request.GET.get('city') if request.GET.get('city') != None else 'Mars'
            slug = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}'
            res = requests.get(slug).json()
            print(city)
            context = {
                'city': res['name'],
                'temprature': int(res['main']['temp'] - 273),
                'icon': res['weather'][0]['icon'],
                'humidity': int(res['main']['humidity'])
            }
            return render(request, 'base.html', context)
        except:
            return render(request, 'error.html')
