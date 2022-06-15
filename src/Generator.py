import requests
from SettingsManager import SettingsManager
from src.PlaylistFeed import PlaylistFeed

settings_manager = SettingsManager("Appsettings.json")


def main():
    api_data: dict = get_api_data()


def get_api_data() -> dict:
    results: dict = {}
    for playlist in settings_manager.get_appsettings('playlists'):
        playlist_tracks_response: dict = SettingsManager.to_dict(request(settings_manager.get_appsettings("urls")["playlistTracks"],
                                                   {"id": playlist, "offset": "0", "limit": "100"}))
        playlist_response: dict = SettingsManager.to_dict(request(settings_manager.get_appsettings("urls")["playlist"], {"id": playlist}))

        results.update({playlist: SettingsManager.to_dict(PlaylistFeed(playlist_response, playlist_tracks_response))})

    settings_manager.update_appsettings({"lastReq": results})
    return results


def request(url: str, querystring: dict) -> object:
    headers = {
        "X-RapidAPI-Key": settings_manager.get_appsettings('X-RapidAPI-Key'),
        "X-RapidAPI-Host": settings_manager.get_appsettings('X-RapidAPI-Host')
    }

    return requests.request("GET", url, headers=headers, params=querystring)


main()
