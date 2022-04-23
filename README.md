# WifionIce-Analyse

Für eine Hausarbeit im Fach Informatik an der Hochschule Karlsruhe hat meine Gruppe sich dazu entschieden eine Auswertung der Daten zu WifionIce der Deutschen Bahn anzufertigen.


Link zu den Daten: https://data.deutschebahn.com/dataset/wifi-on-ice.html

Link zu einem Backup der Datei: https://t1p.de/wifionice

Link zu den Daten in einer Parquet-Datei der Daten: https://t1p.de/woiparquet

Desweiteren gibt es eine Parquet-Datei, die nur lon und lat enthält. Upload auf Nachfrage an mich.

Bedeutung der Spaltenbezeichnungen:
  - SID
  - GPS_Laenge
  - GPS_Breite
  - GPS_Hoehe
  - GPS_V = Vektor oder Velocity(Geschwindigkeit)?
  - sat = Anzahl der Satelliten in Sicht bei Messung
  - gps_richtung = Richtung als 360° Angabe
  - pax_auth 
  - pax_total
  - tprx = Downloadgeschwindigkeit?
  - tptx = Uploadgeschwindigkeit?
  - link_id = ID Accesspoint?
  - link_ping = Ping

Fragen:
  - ICE-Geschwindigkeit korrelliert mit Downloadgeschwindigkeit?
  - "GSP_Hoehe"-Errors vom Zug oder der geografischen Position abhängig?
  - Link_ID Bezeichung für Access-Point im Zug?
  - Bedeutung SID
  - tprx = Download? tptx = Upload?
  - Wie kommt GPS_Richtung zu stande?
  - gps_v = Velocity? Max-Wert ist Error?
  - Einzelnen Zug herausgreifen

Auswertungen für Präsentation:
  - Erklärung Datensatz (Erklärung Errors)
  - Downloadgeschwindigkeit von Zuggeschwindigkeit abhängig?

  - Koordinaten mit Ping, Download, GPS_V verknüpfen
  - Einzelnen Zug exemplarisch zeigen

ToDo:
- herausfinden, wie ein "Data Science"-Projekt durchgeführt wird
- Fragen stellen, die durch die Analyse beantwortet werden sollen
- PPP erstellen
