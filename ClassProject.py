'''
This program connects to openweathermap API to allow the user to input city or zip code to get current weather data for that location
Author: Jacob Cook
Written: 10/13/2020
'''
import requests
import json
APIID = "c98593e412245c9ce904a86281016ff1"

def inputData():
    print("Please enter a zip code or city name: ")
    return input()

def determineType(l): #use a try catch to check if input is zip or City
    try:
        l = int(l)      
        return "zip"
    except ValueError:
        return "city"

def cityAPICall(l):     #copied partly from https://knasmueller.net/using-the-open-weather-map-api-with-python
    url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=imperial" % (l,APIID)
    print("Connecting to Open Weather API...")
    response = requests.get(url).json()
    if response["cod"] == 200:
        print("Connection Successful!")
        return response
    else:
        return "error"    

def zipAPICall(l):      #copied from https://knasmueller.net/using-the-open-weather-map-api-with-python
    url = "https://api.openweathermap.org/data/2.5/weather?zip=%s&appid=%s&units=imperial" % (l,APIID)
    print("Connecting to Open Weather API...")
    response = requests.get(url).json()
    if response["cod"] == 200:
        print("Connection Successful!")
        return response
    else:
        return "error"    

def formatAndDisplay(rawData):
    print("City:", rawData["name"])
    print("Temp:", rawData["main"]["temp"], "F°")
    print("Feels Like: ", rawData["main"]["feels_like"], "F°")
    print("Air Pressure: ", rawData["main"]["pressure"], "hPa")
    print("Humidity:", rawData["main"]["humidity"], "%")
    print("Wind Speed:", rawData["wind"]["speed"])


def main():
    loopAgain = "yes"
    while loopAgain == "yes":
        location = inputData()
        locType = determineType(location)
        if locType == "city":
            rawData = cityAPICall(location)
        else:
            rawData = zipAPICall(location)

        if rawData == "error": 
            print("Error, invalid input.")
        else:
            formatAndDisplay(rawData)
        print("Would you like to enter another? [yes or no]")
        loopAgain = input()
    print("Thanks for using Jacob's Weather App! Brought to you by OpenWeatherMap")
    print("Learn more about this API at: https://openweathermap.org/")

main()
