import requests
from SettingsManager import SettingsManager
import Logger
from src.PlaylistFeed import PlaylistFeed

settings_manager = SettingsManager("Appsettings.json")


def get_api_data() -> dict:
    results: dict = {}
    apis: dict = settings_manager.proxy_get_appsettings("apis")

    for playlist in settings_manager.proxy_get_appsettings('playlists'):
        playlist_tracks_response = request(apis["playlistTracks"], {"id": playlist, "offset": "0", "limit": "100"})
        playlist_response = request(apis["playlist"], {"id": playlist})

        results.update({playlist: SettingsManager.to_dict(PlaylistFeed(playlist_response,
                                                                       playlist_tracks_response,
                                                                       apis))})

    settings_manager.update_appsettings({"lastReq": results})
    return results


def get_access_token(api):
    headers: dict = api["headers"]

    if api["requireSecret"]:
        headers.update(
            {settings_manager.proxy_get_appsettings("id"): settings_manager.proxy_get_appsettings("secret")})

    requests.request(api["method"], api["url"], headers=headers, params=api["body"])


def request(api: dict, querystring: dict) -> object:
    headers = {
        "X-RapidAPI-Key": settings_manager.proxy_get_appsettings('X-RapidAPI-Key'),
        "X-RapidAPI-Host": settings_manager.proxy_get_appsettings('X-RapidAPI-Host')
    }

    Logger.console_log("Requesting API response from (" + api["url"] + ") now!", Logger.LogLevel.Information)
    return requests.request("GET", api["url"], headers=headers, params=querystring)
