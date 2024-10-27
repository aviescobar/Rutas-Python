import requests
import folium

def obtener_ruta(partida, destino, paradas, api_key):
  origin = partida.replace(" ", "+")
  destination = destino.replace(" ", "+")
