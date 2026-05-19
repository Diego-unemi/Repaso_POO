class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor"# Atributo privado, se puede acceder como publico
        self.__atributo_super_privado = "Valor2" #atributo muy privado

    def _hablar(self): # metodo privado
        print("metodo privado")

    def __hablar(self):
        print("metodo super privado")

objeto = MiClase()

print(objeto._atributo_privado)
objeto._hablar() # se puede acceder


#print(objeto.__atributo_super_privado)
#objeto.__hablar() # no se puede acceder desde afuera


#Getters y Setters

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    def get_nombre(self): # para acceder a un atributo privado o super privado se debe hacer desde dentro de la clase ya sea con setters o getters
        return self._nombre
    
    def set_nombre(self, new_nombre): # para acceder a un atributo privado o super privado se debe hacer desde dentro de la clase ya sea con setters o getters
        self._nombre = new_nombre

diego = Persona("Diego", 23)

print(diego._edad) # No se deberia acceder de esa forma

nombre = diego.get_nombre() #Esta es la manera de acceder a un atributo privado

print(nombre)

diego.set_nombre("Alejandro")

nombre = diego.get_nombre()
print(nombre)