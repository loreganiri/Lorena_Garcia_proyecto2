
   
class CatalogoPelicula:
   def __init__(self, ruta, nombre, Catalogo):
    self.ruta = ruta # Atributo instancia
    self.nombre = nombre  # Atributo de instancia
    self.Catalogo = Catalogo

def guardar():
    from Menu import Catalogo #Esta linea me corre todo el modulo, 
    #en vez de solo llamar la variable que estoy pidiendo (var Catalogo), no logro encontrar el motivo, 
    # investigando esto se supone que deberia ser correcto asi. Si continuas respondiendo lo que pide finalmente hace lo que deberia hacer a la segunda vez
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
      archivo.write("/ ")
      archivo.write(genero)
      archivo.write("/ ")
      archivo.write(anio)
      archivo.write("/ ")
      archivo.write(director)
      archivo.write("/ ")
      archivo.write(duracion)
      archivo.write("\n")          
      
def listar():
  from Menu import Catalogo #Esta linea me corre todo el modulo, 
    #en vez de solo llamar la variable que estoy pidiendo (var Catalogo), no logro encontrar el motivo, 
    # investigando esto se supone que deberia ser correcto asi. Si continuas respondiendo lo que pide finalmente hace lo que deberia hacer a la segunda vez
  with open (Catalogo, 'r') as archivo:
   linea = archivo.readline()
   while linea:
       print(linea.strip())
       linea = archivo.readline()
  
def empezar():
  from Menu import Catalogo  #Esta linea me corre todo el modulo, 
    #en vez de solo llamar la variable que estoy pidiendo (var Catalogo), no logro encontrar el motivo, 
    # investigando esto se supone que deberia ser correcto asi. Si continuas respondiendo lo que pide finalmente hace lo que deberia hacer a la segunda vez
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
      archivo.write("\n")        
        
class Pelicula:
  def __init__(self, id, nombre, genero, anio, director, duracion):
    self.__id = id # Atributo privado
    self.nombre = nombre  # Atributo de instancia
    self.genero = genero  # Atributo de instancia
    self.anio = anio  # Atributo de instancia
    self.director = director  # Atributo de instancia
    self.duracion = duracion  # Atributo de instancia
       