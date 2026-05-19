
# Al no haber herencia seria un caso de polimorfismo para tipado dinamico
class Gato:
    def sonido(self):
        return "Miau"
    
class Perro:
    def sonido(self):
        return "Guau"
    
def hacer_sonido(animal):
    print(animal.sonido())

# Para realizarlo en tipado estatico se requiere heredar 
class Animal:
    pass

class Gato(Animal):
    def sonido(self):
        return "Miau"
    
class Perro(Animal):
    def sonido(self):
        return "Guau"
    
def hacer_sonido(animal):
    print(animal.sonido())

#Creacion de objeto

gato = Gato() 
perro = Perro()

print(gato.sonido()) # Esta dando el mismo mensaje(metodo) solo cambia el objeto
print(perro.sonido()) # aca cambia el objeto para el metodo

hacer_sonido(gato) # Este es otro tipo de polimorfismo, Le pasa la misma funcion solo cambia el paramtro (polimorfismo de funcion)

