import json

class PlaylistFeed:

    def __init__(self, playlist, tracks, keys: dict):
        playlist_info = keys["playlist"]
        tracks_info = keys["playlistTracks"]

        self.playlist_info: dict = json.loads(playlist._content.decode("utf-8"))
        self.tracks_info: dict = json.loads(tracks._content.decode("utf-8"))
        self.playlist_status_code: int = playlist.status_code
        self.tracks_status_code: int = playlist.status_code
