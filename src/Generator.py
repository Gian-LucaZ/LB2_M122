import json
import requests

def main():
    
    results = []
    for id in getAppsettings('playlists'):
        results.append(request(id,
         "https://spotify23.p.rapidapi.com/playlist_tracks/",
          {"id":id,"offset":"0","limit":"100"}))

    print(results)

def getAppsettings(key: str):
    with open("Appsettings.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    return jsonObject[key]

def setAppsettings(key: str, value: str):
    with open("Appsettings.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    jsonObject[key] = value
    etc
    
def request(id: str, url: str, querystring: list):
    headers = {
        "X-RapidAPI-Key": getAppsettings('X-RapidAPI-Key'),
        "X-RapidAPI-Host": getAppsettings('X-RapidAPI-Host')
    }
    
    return requests.request("GET", url, headers=headers, params=querystring)

main()