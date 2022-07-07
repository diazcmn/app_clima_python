from pydoc import ModuleScanner, describe
from tkinter import *
from urllib import response

from requests import request
import requests


def mostrar_respuesta(clima):
    nombre_ciudad = clima["name"]
    desc = clima["weather"][0]["description"]
    temp = clima["main"]["temp"]

    ciudad["text"] = nombre_ciudad
    temperatura["text"] = temp
    descripcion["text"] = desc


def clima_JSON(ciudad):
    API_key = "d23f4bc68a094267b5d8a56644bb1df8"
    # id={city id}&appid={API key
    URL = "https://api.openweathermap.org/data/2.5/weather?}"
    parametros = {"APPID": API_key, "q": ciudad, "units": "metric"}
    response = requests.get(URL, params=parametros)
    clima = response.json()

    print(clima["name"])
    print(clima["weather"][0]["description"])
    print(clima["main"]["temp"])

    mostrar_respuesta(clima)


ventana = Tk()

ventana.geometry("350x550")
texto_ciudad = Entry(ventana, font=("Courier", 20, "normal"), justify="center")
texto_ciudad.pack(padx=30, pady=30)

obtener_clima = Button(ventana, text="Obtener Clima", font=(
    "Courier", 20, "normal"), command=lambda: clima_JSON(texto_ciudad.get()))
obtener_clima.pack()

ciudad = Label(font=("Courier", 20, "normal"))
ciudad.pack(padx=30, pady=10)

temperatura = Label(font=("Courier", 50, "normal"))
temperatura.pack(padx=10, pady=10)

descripcion = Label(font=("Courier", 20, "normal"))
descripcion.pack(padx=30, pady=30)

ventana.mainloop()
