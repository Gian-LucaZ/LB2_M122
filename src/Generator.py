import pip._vendor.requests
from SettingsManager import SettingsManager

settingsManager: SettingsManager

def main():
   settingsManager = SettingsManager("Appsettings.json")
   settingsManager.updateAppsettings({"playlists": ["Hallo","Mooin"]})
    

def getApiData():
    results = []
    for id in settingsManager.getAppsettings('playlists'):
        results.append([request(
         "https://spotify23.p.rapidapi.com/playlist_tracks/",
          {"id":id,"offset":"0","limit":"100"}),
          request(
            "https://spotify23.p.rapidapi.com/playlist/",
            {"id":id})])

    return results
    
def request(url: str, querystring: list):
    headers = {
        "X-RapidAPI-Key": settingsManager.getAppsettings('X-RapidAPI-Key'),
        "X-RapidAPI-Host": settingsManager.getAppsettings('X-RapidAPI-Host')
    }
    
    return pip._vendor.requests.request("GET", url, headers=headers, params=querystring)

main()