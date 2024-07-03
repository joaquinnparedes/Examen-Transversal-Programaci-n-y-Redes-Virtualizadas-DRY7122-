import os
import urllib.parse
import requests
import time
geo="https://geocode.maps.co/search?"
hopper="https://graphhopper.com/api/1/route?"
apikeygeo="665635db6fda8179075509fmh73217e"
apikeyruta="52330dd6-e112-4c83-9b8b-9810e56c8388"

opcion=1

print("Comenzamos el script.")
time.sleep(1)
os.system("cls")
print("Comenzamos el script /.")
time.sleep(0.15)
os.system("cls")
print("Comenzamos el script -.")
time.sleep(0.15)
os.system("cls")
print("Comenzamos el script \.")
time.sleep(0.15)
os.system("cls")
print("Comenzamos el script /.")
time.sleep(0.15)
os.system("cls")
print("Comenzamos el script -.")
time.sleep(0.15)
os.system("cls")
print("Comenzamos el script \.")
time.sleep(0.15)
os.system("cls")
  
  
  
  
while opcion==1: 
  print("\b")
  print("Bienvenido a la Perfecta API de Joaquin y Carlos")
  print("A continuacion, ingrese la comuna en la que se ubica:")   
  print("")    
  print("") 
  comuna1=input("COMUNA: ").lower()
  os.system('cls')
  print("//////////////////////////////////////////////////")
  print("Perfecto! ahora la ubicacion a la que quiere ir")
  print("//////////////////////////////////////////////////")
  time.sleep(1)
  print("")
  print("")
  comuna2=input("COMUNA A LA QUE QUIERE IR: ").lower()

  while True:
      os.system('cls')
      print("/.")
      time.sleep(0.15)
      os.system("cls")
      print("-.")
      time.sleep(0.15)
      os.system("cls")
      print("\.")
      time.sleep(0.15)
      os.system("cls")
      print("//////////////////////////////////////////////////")
      print("Perfecto! En que medio de transporte irá?")
      print("//////////////////////////////////////////////////")
      print("1.- A pie")
      print("2.- En Auto")
      seleccion=int(input("Seleccion: "))
      if seleccion==1:
        profile="foot"
        break
      elif seleccion==2:
        profile="car"
        break
      print("Eso no es un numero!")
      time.sleep(1)
      os.system('cls')
  print("/.")
  time.sleep(0.15)
  os.system("cls")
  print("-.")
  time.sleep(0.15)
  os.system("cls")
  print("\.")
  time.sleep(0.15)
  os.system("cls")
  print("/.")
  time.sleep(0.15)
  os.system("cls")
  print("-.")
  time.sleep(0.15)
  os.system("cls")
  print("//////////////////////////////////////////////////")
  print("Ahora le mostraremos la distancia y el resto de ")
  print("informacion util que requiere")
  print("///////////////////////////////////////////////")

  urlgeo1=geo + urllib.parse.urlencode({"q":comuna1,"apikey":apikeygeo})
  urlgeo2=geo + urllib.parse.urlencode({"q":comuna2,"apikey":apikeygeo})

  while True:

    time.sleep(1)
    geo1=requests.get(urlgeo1)
    geocomuna1=geo1.json()
    geo2=requests.get(urlgeo2)
    geocomuna2=geo2.json()

    latitudgeo1=geocomuna1[1]['lat']
    longitudgeo1=geocomuna1[1]['lon']
    infocomuna1=latitudgeo1+","+longitudgeo1

     
    latitudgeo2=geocomuna2[1]['lat']
    longitudgeo2=geocomuna2[1]['lon']
    infocomuna2=latitudgeo2+","+longitudgeo2

    while True:
      true="true"
      json="json"
      
      urlhopper="https://graphhopper.com/api/1/route?"+"point="+infocomuna1+"&point="+infocomuna2+"&vehicle="+profile+"&"+urllib.parse.urlencode({"debug":true,"key":apikeyruta,"type":json})
      hopperlisto=requests.get(urlhopper)
      hopperread=hopperlisto.json()

      tiempooriginal=hopperread["paths"][0]["time"]
      distanciaoriginal=hopperread["paths"][0]["distance"]
      distanciamillas=distanciaoriginal/1600
      distanciakilometros=distanciaoriginal/1000
      tiempofinal=tiempooriginal/60000
      tiempo=tiempofinal/60
      
      
      instruccion1=hopperread["paths"][0]["instructions"][0]["text"]
      instruccion2=hopperread["paths"][0]["instructions"][1]["text"]
      print(round(tiempo, 2) , " Horas")      
      print(round(distanciakilometros, 1) , " Kilometros")      
      print(round(distanciamillas, 1) , " Millas") 
      print("desde ", comuna1, instruccion1)
      print("luego ", instruccion2)
      print("")
      print("")
      print("")
      print("Desea Salir del sistema (s), o quedarse? (n)")
      salir=input("Seleccion: ")
      if salir=="s":
        opcion=2
        break
      elif salir=="n":
        opcion=1
        break
    break
  