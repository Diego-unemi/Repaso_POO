class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self): #devuelve el valor en forma de texto en cadena
        return f"Persona(nombre={self.nombre}),edad={self.edad}"
    
    def __repr__(self): # se usa para reconstruir un objeto  
        return f'Persona("{self.nombre}", {self.edad})'
    
    def __add__(self, otro): # se usa para sumar objetos
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)


diego = Persona("Diego",23)
alejandro = Persona("alejandro",23)
sofia = Persona("sofia",18)

#__repr__
repre = repr(sofia) # se obtiene una representacion del objeto
resultado_repre = eval(repre) #recostruye el objeto
print(type(resultado_repre))
print(resultado_repre.nombre)

#__add__
resultado = diego + alejandro

nueva_persona = diego + alejandro + sofia

print(resultado)

print(diego)

print(nueva_persona.edad)
print(nueva_persona.nombre)

#Ejercicio
# Crear un juego de fusion

# El juego consite en crear personajes un juego y que esos personajes se puedan fusionar 
# para formar personajes mas poderosos que tengan mas poder...

# Para ello deberemos cambiar el comportamiento del operador  "+" para que cuando los personajes 
# se fusionen, salga un nuevo personaje con habilidades mejoradas.

# una posible formula es: el promedio de las habilidades de ambos, al cuadrado!


# class Personaje:
#     def __init__(self, nombre, fuerza):
#         self.nombre = nombre
#         self.habilidad = fuerza
    
#     def __add__(self, otro):
#         nueva_habilidad = ((self.habilidad + otro.habilidad)/2)
#         return nueva_habilidad**2
    

# personaje_1 = Personaje("Scorpion",5)
# personaje_2 = Personaje("Subzero",20)

# nuevo_personaje = personaje_1 + personaje_2

# print(nuevo_personaje)

class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    def __repr__(self):
        return f"{self.nombre} (Fuerza : {self.fuerza}, Velocidad: {self.velocidad})"
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-"+ otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.velocidad)/2)**1.34)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**1.34)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
    

goku = Personaje("goku",100,100)
vegeta = Personaje("vegeta",99,99)
jiren = Personaje("jiren",130,140)

gogeta = goku + vegeta
jireta = gogeta + jiren

print(jireta)


# #Aritméticos:
# __add__(self, other): #Sobrecarga del operador de suma (+).
# __sub__ (self, other): #Sobrecarga del operador de resta (-).
# __mul__(self, other): #Sobrecarga del operador de multiplicación (").
# __div__ (self, other): #Sobrecarga del operador de división (/).
# __mod__ (self, other): #Sobrecarga del operador de modulo (%).
# __pow__(self, other): #Sobrecarga del operador de exponenciación ("").
# #Comparación:
# __eq__(self, other): #Sobrecarga del operador de igualdad (==).
# __ne__ (self, other): #Sobrecarga del operador de desigualdad (!=).
# __lt__(self, other): #Sobrecarga del operador menor que (<).
# __gt__ (self, other): #Sobrecarga del operador mayor que (>).
# __le__(self, other): #Sobrecarga del operador menor o igual que (<=).
# __ge__ (self, other): #Sobrecarga del operador mayor o igual que (>=).
# #Asignación:
# __iadd__ (self, other): #Sobrecarga del operador de suma en asignación (+=).
# __isub__ (self, other): #Sobrecarga del operador de resta en asignación (=).
# __imul__ (self, other): #Sobrecarga del operador de multiplicación en asignación (*=).
# __idiv__ (self, other): #Sobrecarga del operador de división en asignación (/=).
# __imod__ (self, other): #Sobrecarga del operador de módulo en asignación (%=).
# __ipow__ (self, other): #Sobrecarga del operador de exponenciación en asignación (**=).
# #Otros:
# __str__(self): #Sobrecarga del operador str(). Devuelve una representación legible como cadena del objeto.
# __len__(self): #Sobrecarga del operador len(). Devuelve la longitud del objeto.
# __getitem__(self, index): #Sobrecarga del operador de indexación ([]). Permite acceder a elementos del objeto por indice



