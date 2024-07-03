#1.	Crear un repositorio público con el nombre de Examen Transversal Programación y Redes Virtualizadas – DRY7122 
#2.	En la descripción deberá colocar Archivos Examen Transversal DRY7122 
#3.	En directorio crear script en Python que se imprima en una lista los nombres y apellidos de los integrantes del grupo. 
#4.	En directorio crear script en Python que al ejecutar el usuario coloque el número de VLAN, y indique en pantalla si corresponde a una VLAN del rango normal o el rango extendido. 
#5.	El directorio debe tener la configuración necesaria para ser iniciado con Git, utilizar Git commit con información a elección y que los scripts desarrollados en Python quede alojado en GitHub. 

import os 
import time

pregunta=1
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

if pregunta==2:
    print("MUCHAS GRACIAS, ADIOS!")
    time.sleep(2)
elif pregunta ==1:
    while True:
        print("||||||||||||||||||||||||||||||||||||||||||")
        print("SCRIPT ITEM NUMERO 1 EXAMEN FINAL")
        print("||||||||||||||||||||||||||||||||||||||||||")
        print("Integrantes:")
        print("1- Carlos Galleguillos")
        print("2- Joaquin Paredes")
        print("||||||||||||||||||||||||||||||||||||||||||")
        os.system("cls")
        while pregunta==1:
            print("||||||||||||||||||||||||||||||||||||||||||")
            print("SCRIPT ITEM NUMERO 1 EXAMEN FINAL")
            print("||||||||||||||||||||||||||||||||||||||||||")
            print("Integrantes:")
            print("1- Carlos Galleguillos")
            print("2- Joaquin Paredes")
            print("||||||||||||||||||||||||||||||||||||||||||")
            print("¿Desea comprobar si la VLAN")
            print("en la que piensa esta en el")
            print("rango de estandares o extendidas?")
            print(" ")
            vlanguess=int(input("VLAN en la que pienso:  "))
            if vlanguess >= 1 and vlanguess <=1005:
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
                while True:
                    print("Esa VLAN es del rango: NORMAL")
                    print("muchas gracias por usar el script")
                    print('\n')
                    print("Si desea salirse, escriba 's'")
                    print("Si desea consultar otra VLAN, escriba '1'")
                    anspregunta=str(input("Seleccion: "))
                    if anspregunta=="s":
                        pregunta=2
                        os.system("cls")
                        break
                    elif anspregunta=="1":
                        pregunta=1
                        os.system("cls")
                        break
                    else:
                        print(" ")
                        print(" ")
                        print(" ")
                        print("Esa seleccion no existe!")
                        time.sleep(1)
                        os.system("cls")  
            elif vlanguess >= 1006 and vlanguess <=3967 or vlanguess >= 4048 and vlanguess <=4093:
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
                while True:
                    print("Esa VLAN es del rango: EXTENDIDA")
                    print("muchas gracias por usar el script")
                    print('\n')
                    print("Si desea salirse, escriba 's'")
                    print("Si desea consultar otra VLAN, escriba '1'")
                    anspregunta=str(input("Seleccion: "))
                    if anspregunta=="s":
                        pregunta=2
                        os.system("cls")
                        break
                    elif anspregunta=="1":
                        pregunta=1
                        os.system("cls")
                        break
                    else:
                        print(" ")
                        print(" ")
                        print(" ")
                        print("Esa seleccion no existe!")
                        time.sleep(1)
                        os.system("cls")  
            elif vlanguess >= 3968 and vlanguess <=4047 or vlanguess == 4049:
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
                while True:
                    print("Esa VLAN es del rango: INTERNAMENTE ALOJADA")
                    print("muchas gracias por usar el script")
                    print('\n')
                    print("Si desea salirse, escriba 's'")
                    print("Si desea consultar otra VLAN, escriba '1'")
                    anspregunta=str(input("Seleccion: "))
                    if anspregunta=="s" or anspregunta=="S":
                        pregunta=2
                        os.system("cls")
                        break
                    elif anspregunta=="1":
                        pregunta=1
                        os.system("cls")
                        break
                    else:
                        print(" ")
                        print(" ")
                        print(" ")
                        print("Esa seleccion no existe!")
                        time.sleep(1)
                        os.system("cls")  
            else:
                print(" ")
                print(" ")
                print(" ")
                print("Ese no esta dentro de ningun rango!")
                time.sleep(1)
                os.system("cls")
        break