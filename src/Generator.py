from distutils.log import error


def main():
    
    results = []
    for id in getPlaylistIds():
        results.append(request(id))

    print(results)

def getPlaylistIds():
    import json

    with open("Appsettings.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    return jsonObject['playlists']

def setPlaylistIds(ids):
    dostuff

def request(id):
    import requests

    url = "https://spotify23.p.rapidapi.com/playlist_tracks/"
    querystring = {"id":id,"offset":"0","limit":"100"}
    headers = {
        "X-RapidAPI-Key": "9d0c09ff94mshc55e308457b1585p16dde8jsn0c00cd06b91b",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }
    
    return requests.request("GET", url, headers=headers, params=querystring)

main()