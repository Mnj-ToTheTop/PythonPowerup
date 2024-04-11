# Weather application
import requests
API_key = "984b8ea9e4c3426e9a660604242303"
city_name = "Vellore"

jarvis.say("Hello! Would you like to check the weather?")
jarvis.runAndWait()
url = "http://api.weatherapi.com/v1/current.json?key=984b8ea9e4c3426e9a660604242303&q=Vellore&aqi=no"

response = requests.get(url).json()    #json format to get readable use json()

temp = response['current']['temp_c']
humidity = response['current']['humidity']
condi = response['current']['condition']['text']

jarvis.say(f"The weather in {city_name} is {condi}. The temperture is {temp} degree celsius and humidity is {humidity} percent.")
jarvis.runAndWait()
