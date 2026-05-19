#1. Para este ejercicio lo ideal es crear una clase
#estudiante que cuente con los atributos nombre edad y grado además hay que agregar un método que se llame estudiar que imprima el mensaje el estudiante el nombre del estudiante está estudiando para trabajar
#con instancias Estaría bueno que podamos crear una instancia de esta clase y usarlo el método Pero para esto habría que generar una interacción con el
#usuario se tiene que pedir el nombre edad y grado y a continuación instanciar esta clase y mostrar los datos de la clase creada si después de registrar al
#estudiante el usario escribe estudiar poner al estudiante estudiar indistinto de mayúsculas o minúsculas


class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"el estudiente {self.nombre} de edad {self.edad} y grado {self.grado} se encuentra estudiando")


nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
grado = int(input("Ingrese el grado del estudiante: "))

estudiante = Estudiante(nombre, edad, grado)

print(f"""
      Datos del estudiante registrado: \n\n
      Nombre: {estudiante.nombre}\n
      Edad: {estudiante.edad}\n
      Grado: {estudiante.grado}\n
      """)
        

while True:
    estudiar = input()
    if estudiar.lower() == "estudiar":
        estudiante.estudiar()
        break