#Imagina que estas modelando animales en un zoologico. Crear tres clases: "Animal", "mamifero" y
# "Ave". La clase "Animal" debe tener un metodo llamado "comer". La clase "Mamifero" debe tener un
# metodo llamado "amamantar" y la clase "Ave" un metodo llamado "volar"
#
# Ahora, crea una clase llamada "Murcielago" y "Ave", en ese orden, y por lo tanto
# debe ser capaz de "amamantar" y "volar, ademas de "comer".
#
#Finalmente, juega con el orden de herencia de la clase "Murcielago" y observa como cambia el
# MRO y el comportamiento de los metodos al usar super().


class Animal:
    def __init__(self, nombre, alimentacion, habitat):
        self.nombre = nombre
        self.alimentacion = alimentacion
        self.habitat = habitat

    def comer(self):
        print("El animal esta comiendo")

class Mamimefero(Animal):
    def __init__(self, nombre, alimentacion, habitat, modo_caminar ):
        Animal.__init__(self,nombre, alimentacion, habitat )
        self.modo_caminar = modo_caminar

    def amamantar(self):
        print("El mamifero esta amamantando")

class Ave(Animal):
    def __init__(self, nombre, alimentacion, habitat, tipo_ave ):
        Animal.__init__(self,nombre, alimentacion, habitat )
        self.tipo_ave = tipo_ave

    def volar(self):
        print("El ave esta volando")


class Murcielago(Mamimefero,Ave):
    def __init__(self, nombre, alimentacion, habitat, modo_caminar, tipo_ave, reproduccion):
        Mamimefero.__init__(self, nombre, alimentacion, habitat, modo_caminar)
        Ave.__init__(self,nombre, alimentacion, habitat, tipo_ave)
        self.reproduccion = reproduccion

    
murcielago = Murcielago("murcielago de la fruta","hervivoro","selva","bipedo","terrestre","sexual")

murcielago.comer()
murcielago.amamantar()
murcielago.volar()

print(Murcielago.mro())