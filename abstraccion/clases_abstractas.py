from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, secso, actividad):
        self.nombre = nombre
        self.edad = edad
        self.secso = secso
        self.actividad = actividad

    @abstractmethod #Defines una especie de contrato, ya que toda clase que herede debera tener si o si los metodos definidos como abstractos sino no funcionara
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")


class Estudiante(Persona):

    def __init__(self, nombre, edad, secso, actividad):
        super().__init__(nombre, edad, secso, actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

class Trabajador(Persona):

    def __init__(self, nombre, edad, secso, actividad):
        super().__init__(nombre, edad, secso, actividad)

    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de: {self.actividad}")



diego = Estudiante("Diego", 23, "Masculino", "Programacion")

alejandro = Trabajador("alejandro", 23, "Masculino", "Programacion")

diego.presentarse()
diego.hacer_actividad()

alejandro.presentarse()
alejandro.hacer_actividad()