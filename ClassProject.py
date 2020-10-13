'''
This program connects to openweathermap API to allow the user to input city or zip code to get current weather data for that location
Author: Jacob Cook
Written: 10/13/2020
'''
import requests
import json
APIID = "c98593e412245c9ce904a86281016ff1"
validLoc = False
def inputData():
    print("Please enter a zip code or city name: ")
    return input()

def determineType(l):
    if l.isalpha:
        locType = "city"
    elif l.isnumeric:
        locType = "zip"
    else:
        locType = "error"

    return locType 

def cityAPICall(l):     #copied from https://knasmueller.net/using-the-open-weather-map-api-with-python
    url = "api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" % (l,APIID)
    response = requests.get(url)
    return json.loads(response.text)

def zipAPICall(l):      #copied from https://knasmueller.net/using-the-open-weather-map-api-with-python
    url = "api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" % (l,APIID)
    response = requests.get(url)
    return json.loads(response.text)

def formatAndDisplay(rawData):
    print(rawData)

def main():
    location = inputData()
    locType = determineType(location)
    if locType == "city":
        rawData = cityAPICall(location)
    elif locType == "zip":
        rawData = zipAPICall(location)
    else:
        validLoc = False
        print("Invalid location. You entered:", location, ". Please Try again.")

    if validLoc == True: 
        formatAndDisplay(rawData)
    else:
        print("Location not found. Please try again.")

main()
    
    
    




