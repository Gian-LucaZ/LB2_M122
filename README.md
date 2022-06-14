# LB2 Report anhand einer API Generieren

## Die API

Die API aufgrund welcher ein Report generiert werden soll ist eine [Spotify-API](https://rapidapi.com/Glavier/api/spotify23/). Auf dieser können wir Beliebeige Daten aus der Spotify-Datenbank erreichen und im Wöchentlichen Report ausgeben.

## Der Report

Beim starten des Mailservices soll es möglich sein den Report zu Parametrieren. Es sollen mehrere Playlists "abonniert" werden können, für welche der Report uns dann auch immer den wöchentlichen Feed ausgeben soll.

Der Report soll für jede Angewählte Playlist einen einzelnen kleinen Feed beinhalten. Dieser Feed enthält mehrere dinge:

1. Vorschläge, in welche Titel wieder einmal reingehört werden Könnte.
2. Er zeigt änderungen an der Playlist im Vergleich zur letzten Woche an.

### Aussehen

Der Report soll folgendermassen aussehen. Das ganze wird in verschiedene Sektionen, nach Playlist aufgeteilt. Jede Sektion ist mit Playlistvorschau unnd Namen versehen.

Vorgeschlagene Tracks werden mit Titel, Interpret und Vorschaubild angezeigt. Beim Veränderungsfeed ist dazu auch der Benutzer einsehbar, welcher den Track hinzugefügt hat. Wurde nichts verändert, so wird dies mit einem Banner angezeigt.

Hier Das [Mockup](https://Throw_new_NotImplementedError)