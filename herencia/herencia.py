
#Este ejemplo de clase, se llama clases jerarquica, ya que depende de una clase padre
class Persona:
    def __init__(self, nombre, edad , nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años") #La ventaja que tenemos es que el metodo se puede utilizar para todas las clases que hereden de la clase persona

class Empleado(Persona): #la clase empleado hereda de la clase persona, es decir, la clase empleado es una subclase de la clase persona, por lo tanto, la clase empleado tiene todos los atributos y metodos de la clase persona
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad) #super() se utiliza para llamar al constructor de la clase padre, es decir, de la clase persona
        self.trabajo = trabajo
        self.salario = salario

class Estudiante(Persona): #la clase estudiante hereda de la clase persona 
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad


diego = Empleado("Diego", 23, "Ecuatoriana", "Programador", 1000)

print(diego.trabajo)

diego.hablar() 


# Ejemplo de herencia multiple, es decir, una clase que hereda de dos clases padre

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")


class EmpleadoArtista(Empleado, Artista):
    def __init__(self, nombre, edad , nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad , nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad} y trabajo en {self.empresa} con un salario de {self.salario}"

    def presentarse(self):                      #self se usa para llamar al metodo mostrar_habilidad de la clase hija (EmpleadoArtista)
        #return f"{super().mostrar_habilidad()}" #super() se usa para llamar al metodo mostrar_habilidad de la clase padre (Artista)
        print( f'Hola, soy: {self.mostrar_habilidad()} y trabajo en {self.empresa}')

Julio = EmpleadoArtista("Julio", 23, "Ecuatoriana","cantar", 1000, "Google")
Julio.presentarse() 


herencia = issubclass( EmpleadoArtista, Artista) #issubclass() se utiliza para verificar si una clase es una subclase de otra clase, en este caso, verificamos si la clase EmpleadoArtista es una subclase de la clase Empleado
print(herencia)


herencia2 = issubclass(Artista, Persona) #verificamos si la clase EmpleadoArtista es una subclase de la clase Empleado
print(herencia2)


instancia = isinstance(Julio, EmpleadoArtista)

print(instancia)    