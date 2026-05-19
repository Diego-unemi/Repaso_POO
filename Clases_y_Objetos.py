## Clases con atributos estaticos
class Celular(): #() es el constructor de la clase, es decir, es la funcion que se ejecuta cuando se crea un objeto de la clase
    ## atributos estataticos para todos los objetos van a ser iguales
    marca = "Samsung"
    modelo = "S23"
    camara = "64MP"

celular1 = Celular() #instancia del objeto y un objeto es una instancia de una clase, es decir, es un ejemplar de la clase
celular2 = Celular() #creamos tres objetos de la clase celular, cada uno con sus propios atributos pero con los mismos valores porque son atributos estaticos

celular3 = Celular() #celular3 es un objeto de la clase celular
celular3.marca = "Apple" #los atributos estaticos se pueden modificar pero solamente por fuera de la clase, no se pueden modificar por cada objeto
print(celular1.marca)
print(celular3.marca)

## Clases con atributos dinamicos
class Celular2:
    def __init__(self, marca, modelo, camara): #__init__ es el constructor de la clase, es decir, es la funcion que se ejecuta cuando se crea un objeto de la clase
        self.marca = marca #self.marca no es lo mismo que marca, self.marca es un atributo de la clase y marca es un parametro del constructor, el self se utiliza para referirse a los atributos de la clase
        self.modelo = modelo
        self.camara = camara
        
celular1 = Celular2("xiaomi", "note 10 pro", "64MP") #creamos un objeto de la clase celular2 y le pasamos los parametros del constructor
celular2 = Celular2("Apple", "iPhone 14", "48MP") 

print(celular1.marca)


## Clases con metodos
class Celular3:
    def __init__(self, marca, modelo, camara): 
        self.marca = marca 
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self): #definir un metodo es como definir una funcion dentro de una clase, el self se utiliza para referirse a los atributos de la clase, es decir, a los objetos de la clase
        print(f"Estas haciendo una llammada desde un: {self.modelo}") # es importante utilizar el self para referirse a los atributos de la clase, ya que si no se utiliza el self, el metodo no va a funcionar correctamente porque no va a saber a que objeto se esta refiriendo.

    def cortar(self):
        print(f"cortaste la llamada desde tu: {self.modelo}")
        
celular1 = Celular3("xiaomi", "note 10 pro", "64MP") 
celular2 = Celular3("Apple", "iPhone 14", "48MP") 


celular1.llamar()
celular1.cortar()
print(celular1.marca)

