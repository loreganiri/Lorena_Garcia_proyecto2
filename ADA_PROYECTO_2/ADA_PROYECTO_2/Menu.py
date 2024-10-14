
import os   
from pathlib import Path

print("Hola Bienvenido a Pelimovie")
print("Dame el nombre del Catalogo a crear")

Catalogo = input()
Catalogo = Catalogo + ".txt"
print(f"El archivo {Catalogo} ha sido creado")

try:           
     with open(Catalogo) as w:     
         print("Abriendo archivo")
         print ("¿Deseas agregar una pelicula para iniciar el catalogo? Si/No")
         answer = input()
         if answer.lower()in ["si"]:
             from AgregarPeli import empezar
             empezar()
         else: 
            answer.lower() in ["no"]
            print("Ok, gracias, adiosito!")
        
except FileNotFoundError:
        print(f"El archivo {Catalogo} aun no existe, generando... ")
        from AgregarPeli import empezar
        empezar()

print (Catalogo)
print("Ahora escoge que deseas hacer (typea el numero)")
print("1.- Agregar pelicula")
print("2.- Listar peliculas")
print("3.- Eliminar catalogo de peliculas")
print("4.- Salir")
while True:
   print("Dame un numero entre 1 y 4: ")
   choose=int(input())
   if choose not in range(1,5):
       print("Opcion invalida, intenta de nuevo")
   else:

        if choose == 1:
              from AgregarPeli import guardar # esto me causa un error de que repite el menu, pero en todo lo que he investigado dice
              guardar()                       # que asi debo de llamar una funcion en otro modulo, si sigues respondiendo de hecho si lo hace finalmente
              
        elif choose == 2:
           try: 
               with open(Catalogo) as f:   
                from AgregarPeli import listar # esto me causa un error de que repite el menu, pero en todo lo que he investigado dice
                listar()                       # que asi debo de llamar una funcion en otro modulo, si sigues respondiendo de hecho si lo hace finalmente
           
           except FileNotFoundError:
                print("El archivo no existe, por favor registra una pelicula primero.")  
        elif choose == 3:
                print("Eliminacion del Catalogo en proceso")
                import os
                
                file = Catalogo
                if os.path.exists(file): 
                    os.remove(file)
                    print("Este archivo fue eliminado con exito")
                else:
                    print("No se encontro tal archivo")
        else:
          if choose ==4:
                print("Muchas gracias por visitarnos! Adios!")
                exit()