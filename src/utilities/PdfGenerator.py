from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas
from src.typedefinitions.Playlist import Playlist, Track
from src.utilities import Logger


class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y


class Rectangle:
    def __init__(self, width: int, height: int, location: Point) -> object:
        self.height = height
        self.width = width
        self.location = location


class Generator:
    _block_padding: int = 5
    _text_size: int = 0

    def set_text_size(self, i: int):
        self._text_size = i
        self.pdf.setFontSize(self._text_size)

    def __init__(self):
        self.pdf: Canvas = None

    def generate(self, playlists: list):
        for playlist in playlists:
            self._generate_content(playlist)

    def _generate_content(self, playlist: Playlist):
        Logger.Information("Now creating report for %s" % playlist.name)
        title: str = "PlaylistFeed-%s.pdf" % (playlist.name + "-" + datetime.now().strftime("%Y-%m-%d"))

        self.pdf = canvas.Canvas(title)
        self._generate_block(playlist)
        self.pdf.save()

        Logger.Information("Finished creating report for %s" % playlist.name)

    def _generate_block(self, playlist: Playlist):
        headerrect = self._generate_block_header(playlist)
        self._generate_block_info(playlist.tracks, "Alle Tracks", headerrect)

    def _generate_block_info(self, tracks: list, topic: str, headerrect: Rectangle):
        block_tl = Point(headerrect.location.X, headerrect.location.Y - self._block_padding)
        block_wdt = headerrect.width

        self.set_text_size(24)
        drawpoint = Point(block_tl.X, block_tl.Y - self._text_size)

        self.pdf.drawString(drawpoint.X, drawpoint.Y, topic)
        drawpoint.Y -= self._text_size

        for track in tracks:
            self.pdf.line(drawpoint.X, drawpoint.Y, drawpoint.X + block_wdt, drawpoint.Y)
            drawpoint.Y -= self._block_padding
            self._generate_block_track(track, drawpoint, block_wdt)
            drawpoint.Y -= self._block_padding

    def _generate_block_track(self, track: Track, drawpoint: Point, wdt: int):
        image_size = 25
        drawpoint.Y -= image_size

        self.pdf.drawImage(track.album_image, drawpoint.X, drawpoint.Y, image_size, image_size)
        self.pdf.linkURL(track.url,
                         (drawpoint.X, drawpoint.Y,
                          drawpoint.X + image_size,
                          drawpoint.Y + image_size))

        self.set_text_size(12)
        self.pdf.drawString(drawpoint.X + image_size + self._block_padding, drawpoint.Y + image_size / 2, track.name)

    def _generate_block_header(self, playlist: Playlist):
        playlist_image = Rectangle(200, 200, Point(100, 650))
        self.pdf.drawImage(playlist.image,
                           playlist_image.location.X,
                           playlist_image.location.Y,
                           playlist_image.width,
                           playlist_image.height)
        self.pdf.linkURL(playlist.url,
                         (playlist_image.location.X,
                          playlist_image.location.Y,
                          playlist_image.location.X + playlist_image.width,
                          playlist_image.location.Y + playlist_image.height))

        self.set_text_size(24)

        playlist_info = Rectangle(playlist_image.width,
                                  playlist_image.height,
                                  Point(playlist_image.location.X + playlist_image.width,
                                        playlist_image.location.Y))
        drawpoint = Point(playlist_info.location.X + self._block_padding,
                          playlist_info.location.Y)

        self.set_text_size(12)
        self.pdf.drawString(drawpoint.X, drawpoint.Y, "Followers: %d" % playlist.followers)

        drawpoint.Y += self._text_size

        name_info: str = "By: %s" % playlist.owner["name"]
        self.pdf.drawString(drawpoint.X, drawpoint.Y, name_info)
        self.pdf.linkURL(playlist.owner["url"],
                         (drawpoint.X,
                          drawpoint.Y,
                          drawpoint.X + self.pdf.stringWidth(name_info, self.pdf._fontname, self._text_size),
                          drawpoint.Y + self._text_size))

        drawpoint.Y += self._text_size + self._block_padding

        self.set_text_size(24)
        self.pdf.drawString(drawpoint.X, drawpoint.Y, playlist.name)

        headersize = Rectangle(playlist_image.width + playlist_info.width,
                               playlist_image.height,
                               Point(playlist_image.location.X,
                                     playlist_image.location.Y))
        return headersize
