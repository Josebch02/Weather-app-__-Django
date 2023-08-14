from django.shortcuts import render
from django.shortcuts import render
import requests
# Create your views here.

# weather_app/views.py

from django.shortcuts import render
import requests

def home(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            # Hacer la solicitud a la API de OpenWeatherMap
            api_key = 'b6caaf31d19731536a2fb13de1ab9d6c'  # Asegúrate de reemplazar con tu API key de OpenWeatherMap
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'  # Units=metric para obtener temperaturas en Celsius
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': data['name'],
                    'main': data['weather'][0]['main'],
                    'temp': data['main']['temp'],
                    'feels': data['main']['feels_like'],
                    'temp_max': data['main']['temp_max'],  # Agregar la temperatura máxima
                    'temp_min': data['main']['temp_min'],  # Agregar la temperatura mínima
                }
                return render(request, 'weather.html', weather_data)
            else:
                error_message = f"Error: Unable to fetch weather data for {city}"
                return render(request, 'index.html', {'error_message': error_message})
        else:
            error_message = "Error: Please enter a city name."
            return render(request, 'index.html', {'error_message': error_message})
    else:
        return render(request, 'index.html', {})
