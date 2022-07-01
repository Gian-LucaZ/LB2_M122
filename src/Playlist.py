class Playlist:

    def __init__(self, playlist: dict):
        self.name: str = playlist["name"]
        self.url: str = playlist["external_urls"]["spotify"]
        self.followers: int = playlist["followers"]["total"]
        self.image: str = playlist["images"][0]["url"]

        owner_data: dict = playlist["owner"]
        self.owner: dict = {"name": owner_data["display_name"],
                            "url": owner_data["external_urls"]["spotify"]}

        self.tracks: list = []
        for track in playlist["tracks"]["items"]:
            self.tracks.append(Track(track["track"]))


class Track:

    def __init__(self, track: dict):
        self.name: str = track["name"]
        self.url: str = track["external_urls"]["spotify"]

        album: dict = track["album"]
        self.album_image: str = album["images"][0]["url"]

        artists: list = album["artists"]
        self.artist_names: list = []
        for artist in artists:
            self.artist_names.append(artist["name"])

