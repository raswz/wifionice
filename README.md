# WifionIce-Analyse

Für eine Hausarbeit im Fach Informatik an der Hochschule Karlsruhe hat meine Gruppe sich dazu entschieden eine Auswertung der Daten zu WifionIce der Deutschen Bahn anzufertigen.

Benötigte Python-Moduls: numpy, pandas, matplotlib, plotly

Link zu den Daten: https://data.deutschebahn.com/dataset/wifi-on-ice.html

Link zu einem Backup der Datei: https://t1p.de/wifionice

Link zu den Daten in einer Parquet-Datei der Daten: https://t1p.de/woiparquet

Desweiteren gibt es eine Parquet-Datei, die nur lon und lat enthält. Upload auf Nachfrage an mich.

Bedeutung der Spaltenbezeichnungen:
  - SID
  - Created = Zeitstempel der Messung an den 3 Tagen (08.03.2017 (4.75M Messungen), 01.05.2017(12.2M Messungen), 02.05.2017(6.6M Messungen))
  - GPS_Laenge
  - GPS_Breite
  - GPS_Hoehe masl
  - GPS_V = Velocity(Geschwindigkeit) in m/s
  - sat = Anzahl der Satelliten in Sicht bei Messung
  - gps_richtung = Richtung als 360° Angabe
  - pax_auth = Anzahl der Geräte mit Zugang zum Internet
  - pax_total = Anzahl der Geräte im Netzwerk
  - tprx = Downloadgeschwindigkeit in byte/s
  - tptx = Uploadgeschwindigkeit in byte/s
  - link_gw_conn = Aktive Gateway-Verbindung als Bool
  - link_id = ID Accesspoint (6 Router pro Zug)
  - link_ping = Ping in ms

Fragen:
  - ICE-Geschwindigkeit korrelliert mit Downloadgeschwindigkeit?
  - "GSP_Hoehe"-Errors vom Zug oder der geografischen Position abhängig?
  - Bedeutung SID
  - Wie kommt GPS_Richtung zu stande?
  - Einzelnen Zug herausgreifen

Auswertungen für Präsentation:

Lani:
  - Erklärung Datensatz (Erklärung Errors)
  - Downloadgeschwindigkeit von Zuggeschwindigkeit abhängig?

Scle:
  - Koordinaten mit Ping, Download, GPS_V verknüpfen
  - Einzelnen Zug exemplarisch zeigen

ToDo:
- herausfinden, wie ein "Data Science"-Projekt durchgeführt wird
- PPP erstellen
