# [Pre : API test](../Day%202.2%20-%20API%20test/readme.md)

---

# [OOPs](https://github.com/akashdip2001/ML-Machine-Learning/tree/main/py#oop)

### How to work with Class ?

### ✅ OOP_YouTube [( video_1, or](https://youtu.be/Rq_3gA2h1RA) [video_2, or](https://youtu.be/70JeRslVOrk) [video_3 )](https://youtu.be/6soT3DMBJGQ)

## ☀️ Check the .py files

```python
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
```
```bash
# Output:
# API is working
Weather report: Mumbai

                Smoke
       .--.     +27(28) °C     
    .-(    ).   ↘ 24 km/h      
   (___.__)__)  3 km
# 

# ┌──────────────────────────────┬───────────────────────┤  Sat 07 Dec ├───────────────────────┬──────────────────────────────┐
# │            Morning           │             Noon      └──────┬──────┘     Evening           │             Night            │
# ├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
# │     \   /     Sunny          │     \   /     Sunny          │     \   /     Clear          │     \   /     Clear          │
# │      .-.      +27(28) °C     │      .-.      +28(29) °C     │      .-.      +27(29) °C     │      .-.      +27(28) °C     │
# │   ― (   ) ―   ↓ 18-25 km/h   │   ― (   ) ―   ↘ 23-33 km/h   │   ― (   ) ―   ↘ 21-35 km/h   │   ― (   ) ―   ↘ 21-32 km/h   │
# │      `-’      10 km          │      `-’      10 km          │      `-’      10 km          │      `-’      10 km          │
# │     /   \     0.0 mm | 0%    │     /   \     0.0 mm | 0%    │     /   \     0.0 mm | 0%    │     /   \     0.0 mm | 0%    │
# └──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
#                                                        ┌─────────────┐
# ┌──────────────────────────────┬───────────────────────┤  Sun 08 Dec ├───────────────────────┬──────────────────────────────┐
# │            Morning           │             Noon      └──────┬──────┘     Evening           │             Night            │
# ├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
# │     \   /     Sunny          │     \   /     Sunny          │     \   /     Clear          │     \   /     Clear          │
# │      .-.      +25(26) °C     │      .-.      27 °C          │      .-.      +26(27) °C     │      .-.      +26(27) °C     │
# │   ― (   ) ―   ↓ 13-18 km/h   │   ― (   ) ―   ↘ 17-23 km/h   │   ― (   ) ―   ↘ 21-31 km/h   │   ― (   ) ―   ↓ 18-27 km/h   │
# │      `-’      10 km          │      `-’      10 km          │      `-’      10 km          │      `-’      10 km          │
# │     /   \     0.0 mm | 0%    │     /   \     0.0 mm | 0%    │     /   \     0.0 mm | 0%    │     /   \     0.0 mm | 0%    │
# └──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
#                                                        ┌─────────────┐
# ┌──────────────────────────────┬───────────────────────┤  Mon 09 Dec ├───────────────────────┬──────────────────────────────┐
# │            Morning           │             Noon      └──────┬──────┘     Evening           │             Night            │
# ├──────────────────────────────┼──────────────────────────────┼─────────────────────────────────────┼──────────────────────────────┤
# │     \   /     Sunny          │     \   /     Sunny          │     \   /     Clear          │     \   /     Clear          │
# │      .-.      +24(25) °C     │      .-.      27 °C          │      .-.      27 °C          │      .-.      +26(27) °C     │
# │   ― (   ) ―   ↓ 15-21 km/h   │   ― (   ) ―   ↓ 15-20 km/h   │   ― (   ) ―   ↘ 31-50 km/h   │   ― (   ) ―   ↓ 21-34 km/h   │
# │      `-’      10 km          │      `-’      10 km          │      `-’      10 km          │      `-’      10 km          │
# │     /   \     0.0 mm | 0%    │     /   \     0.0 mm | 0%    │     /   \     0.0 mm | 0%    │     /   \     0.0 mm | 0%    │
# └──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
# Location: Mumbai, Greater Bombay, Maharashtra, India [18.9321862,72.8308337]               0.0 mm                0.0 mm
```

# DevOps - Terraform 

### [more : gitHub link](https://github.com/LondheShubham153/python-masterclass/blob/master/intermediate/terra_deploy.py)

```python
#### $: kubectl get nodes
#### $: docker ps
#### ⬆️ check with python
#### https://github.com/LondheShubham153/python-masterclass/blob/master/intermediate/terra_deploy.py


import subprocess

def run_command(command):
    subprocess.run(command, shell=True, check=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

```
