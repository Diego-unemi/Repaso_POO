class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad
    
    @property # Se usa para convertir un metodo en getters (decorador que accede a la propiedad)
    def nombre(self):
        return self.__nombre
    
    @nombre.setter # Se usa para convertir un metodo en setters (decorador que modifica a la propiedad)
    def nombre(self, new_nombre): 
        self.__nombre = new_nombre

    @nombre.deleter # se usa para eliminar la propiedad
    def nombre(self):
        del self.__nombre # del es un operador que elimina valores

diego = Persona("Diego", 23)


nombre = diego.nombre

print(nombre)

diego.nombre = "Alejandro"

nombre = diego.nombre

print(nombre)

del diego.nombre

nombre = diego.nombre

print(nombre)


 