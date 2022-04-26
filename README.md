# WifionIce-Analyse

Für eine Hausarbeit im Fach Informatik an der Hochschule Karlsruhe hat meine Gruppe sich dazu entschieden eine Auswertung der Daten zu WifionIce der Deutschen Bahn anzufertigen.

Benötigte Python-Moduls: pandas, matplotlib

Link zu den Daten: https://data.deutschebahn.com/dataset/wifi-on-ice.html

Link zu einem Backup der Datei: https://t1p.de/wifionice

Link zu den Daten in einer Parquet-Datei der Daten: https://t1p.de/woiparquet

Desweiteren gibt es eine Parquet-Datei, die nur lon und lat enthält. Upload auf Nachfrage an mich.

Bedeutung der Spaltenbezeichnungen:
  - SID
  - GPS_Laenge
  - GPS_Breite
  - GPS_Hoehe
  - GPS_V = Velocity(Geschwindigkeit)
  - sat = Anzahl der Satelliten in Sicht bei Messung
  - gps_richtung = Richtung als 360° Angabe
  - pax_auth = Anzahl der Geräte mit Zugang zum Internet
  - pax_total = Anzahl der Geräte im Netzwerk
  - tprx = Downloadgeschwindigkeit
  - tptx = Uploadgeschwindigkeit
  - link_gw_conn = Aktive Gateway-Verbindung
  - link_id = ID Accesspoint (6 Router pro Zug)
  - link_ping = Ping

Fragen:
  - ICE-Geschwindigkeit korrelliert mit Downloadgeschwindigkeit?
  - "GSP_Hoehe"-Errors vom Zug oder der geografischen Position abhängig?
  - Bedeutung SID
  - Wie kommt GPS_Richtung zu stande?
  - gps_v = Max-Wert ist Error?
  - Einzelnen Zug herausgreifen

Auswertungen für Präsentation:
  - Erklärung Datensatz (Erklärung Errors)
  - Downloadgeschwindigkeit von Zuggeschwindigkeit abhängig?

  - Koordinaten mit Ping, Download, GPS_V verknüpfen
  - Einzelnen Zug exemplarisch zeigen

ToDo:
- herausfinden, wie ein "Data Science"-Projekt durchgeführt wird
- PPP erstellen
