# LB2 Report anhand einer API Generieren

## Die API

Die API aufgrund welcher ein Report generiert werden soll ist eine [Spotify-API](https://api.spotify.com/v1/). Auf dieser können wir Beliebeige Daten aus der Spotify-Datenbank erreichen und im Wöchentlichen Report ausgeben.

## Der Report

Beim starten des Mailservices soll es möglich sein den Report zu Parametrieren. Es sollen mehrere Playlists "abonniert" werden können, für welche der Report uns dann auch immer den wöchentlichen Feed ausgeben soll.

Der Report soll für jede Angewählte Playlist einen einzelnen kleinen Feed beinhalten. Dieser Feed enthält mehrere dinge:

1. Vorschläge, in welche Titel wieder einmal reingehört werden Könnte.
2. Er zeigt änderungen an der Playlist im Vergleich zur letzten Woche an.

### Aussehen

Der Report soll folgendermassen aussehen. Das ganze wird in verschiedene Sektionen, nach Playlist aufgeteilt. Jede Sektion ist mit Playlistvorschau unnd Namen versehen.

Vorgeschlagene Tracks werden mit Titel und Vorschaubild angezeigt. Dazu zeigt der Report uns noch die 10 neusten Tracks. Die Playlist, die Tracks und auch der Ersteller der Playlist sind Clickbar und verlinkt.

Funktioniert aber nur für die ersten 100 songs!

Hier Das [Ergebnis](PlaylistFeed-r-2022-07-05.pdf)

## Rückblick und Programmbeschrieb

### Programm

Die gesammte Programm ist über ein Json parametrierbar. Da können wir auch unsere PLaylists angeben. Für jede angegebene Playlist wird ein einzelner Report versendet.

