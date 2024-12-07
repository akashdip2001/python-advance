import requests

class WeatherAPI():
    def api_check(self):
        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url)
        if response.status_code == 200:
            print("API is working")
            return response.json()
        else:
            return "API is down"

    def get_weather(self, city):
        # url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"
        url = f"https://wttr.in/{city}" #?format=j1, j1 for json format
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)
        else:
            return "API is down"
        
api_a = WeatherAPI()
api_a.api_check()
api_a.get_weather("Mumbai")

# Output:
# API is working
# Weather report: Mumbai

#                 Smoke
#        .--.     +27(28) °C     
#     .-(    ).   ↘ 24 km/h      
#    (___.__)__)  3 km
#                 0.0 mm