
from abc import ABC, abstractmethod

class Mujer(ABC):
    def __init__(self, nombre, edad, nivel_puteria):
        self.nombre = nombre
        self.edad = edad
        self.nivel_puteria = nivel_puteria
    
    @abstractmethod
    def ser_puta(self):
        return self.nivel_puteria > 1

    