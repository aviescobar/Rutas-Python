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
       # (Mejor ruta)
        route = data["routes"][0]["legs"][0]

        # Extrae la información de la ruta y distancia
        ruta_nombres = [step["html_instructions"] for step in route["steps"]]
        ruta = " → ".join(ruta_nombres)
        distancia = route["distance"]["text"]
        distancia_valor = route["distance"]["value"] / 1000  # Distancia en kilómetros
        return ruta, distancia, distancia_valor, data
    else:
        return None, None, None, None

def obtener_coordenadas(data):
