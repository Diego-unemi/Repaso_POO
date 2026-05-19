#MRO

class A:
    def hablar(self):
        print("Hola desde A")


class B(A):
    def hablar(self):
        print("Hola desde B")

class C(A):
    def hablar(self):
        print("Hola desde C")


class D(B, C):
    def hablar(self):
        print("Hola desde D")

d = D()
d.hablar() #Hola desde D, el metodo hablar de la clase D se ejecuta primero, luego el metodo hablar de la clase B, luego el metodo hablar de la clase C y por ultimo el metodo hablar de la clase A, esto se debe a que el orden de resolucion de metodos (MRO) es D -> B -> C -> A

#Otro Ejemplo
class A:
    def hablar(self):
        print("Hola desde A")

class F:
    def hablar(self):
        print("Hola desde F")

class B(A):
    def hablar(self):
        print("Hola desde B")

class C(F):
    def hablar(self):
        print("Hola desde C")


class D(B, C):
    def hablar(self):
        print("Hola desde D")

d = D()
print(D.mro()) #El metodo mro() se utiliza para mostrar el orden de resolucion de metodos (MRO) de la clase D, en este caso, el orden es D -> B -> C -> F -> A, esto se debe a que el metodo hablar de la clase D se ejecuta primero, luego el metodo hablar de la clase B, luego el metodo hablar de la clase C, luego el metodo hablar de la clase F y por ultimo el metodo hablar de la clase A