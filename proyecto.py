import requests
import folium

def obtener_ruta(partida, destino, paradas, api_key):
  origin = partida.replace(" ", "+")
  destination = destino.replace(" ", "+")
  waypoints = "|".join(paradas.split(","))

   #Acceso a google Maps
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&waypoints={waypoints}&key={api_key}"

    response = requests.get(url)
    data = response.json()

    if data["status"] == "OK" and "routes" in data and len(data["routes"]) > 0:
