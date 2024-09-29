import requests
import json
import os 


city = input("Enter the name of the city ")

url = f"https://api.weatherapi.com/v1/current.json?key=16007f7710454205a5d131453240709&q={city}"

r = requests.get(url)

# print(r.text)
weatherdic = json.loads(r.text)
w = weatherdic["current"]["temp_c"]
print(w)
os.system(f"say 'The current weather in {city} is {w} degree centigrade'")