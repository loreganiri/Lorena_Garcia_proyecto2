
class CatalogoPelicula:
   def __init__(self, ruta, nombre):
    self.ruta = ruta # Atributo instancia
    self.nombre = nombre  # Atributo de instancia

def guardar(): 
    with open (Catalogo, 'a') as archivo:
      print("Escribe el nombre de la pelicula a registrar")
      nombre = input()
      print("Escribe el genero de la pelicula a registrar")
      genero = input()
      print("Escribe el año de la pelicula a registrar")
      anio = input()
      print("Escribe el director de la pelicula a registrar")
      director = input() 
      print("Escribe la duracion de la pelicula a registrar")
      duracion = input ()
      archivo.write(nombre)
      archivo.write(",")
      archivo.write(genero)
      archivo.write(",")
      archivo.write(anio)
      archivo.write(",")
      archivo.write(director)
      archivo.write(",")
      archivo.write(duracion)
      archivo.write("\n")
      
    return print("Pelicula guardada")

def listar():
  with open (Catalogo, 'r') as archivo:
   linea = archivo.readline()
   while linea:
       print(linea.strip())
       linea = archivo.readline()
  
def empezar():
  with open (Catalogo, 'w') as archivo:
      print("Escribe el nombre de la pelicula a registrar")
      nombre = input()
      print("Escribe el genero de la pelicula a registrar")
      genero = input()
      print("Escribe el año de la pelicula a registrar")
      anio = input()
      print("Escribe el director de la pelicula a registrar")
      director = input() 
      print("Escribe la duracion de la pelicula a registrar")
      duracion = input ()
      archivo.write(nombre)
      archivo.write("/ ")
      archivo.write(genero)
      archivo.write("/ ")
      archivo.write(anio)
      archivo.write("/ ")
      archivo.write(director)
      archivo.write("/ ")
      archivo.write(duracion)
      archivo.write(" ")        
        
class Pelicula:
  def __init__(self, id, nombre, genero, anio, director, duracion):
    self.__id = id # Atributo privado
    self.nombre = nombre  # Atributo de instancia
    self.genero = genero  # Atributo de instancia
    self.anio = anio  # Atributo de instancia
    self.director = director  # Atributo de instancia
    self.duracion = duracion  # Atributo de instancia
       
import os   
print("Hola Bienvenido a Pelimovie")

print("Dame el nombre del Catalogo a crear")
Catalogo = input()
Catalogo = Catalogo + ".txt"
print(Catalogo)

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
          from pathlib import Path
          print("Escogio la 1")   

          try:           
            with open(Catalogo) as w:     
             print("El archivo existe")
             
          except FileNotFoundError:
                print("El archivo {Catalogo} aun no existe, generando... ", Catalogo)
                empezar()
          
          print("¿Deseas agregar otra pelicula? SI/NO")
          otra = input()
          if otra.lower()in ["si"]:
              guardar()
          else: 
              otra.lower() in ["no"]
              print("Ok, gracias, adiosito!")

        elif choose == 2:
           try: 
               with open(Catalogo) as f:      
                print("Mostrar peliculas existentes en el catalogo")
                listar()
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