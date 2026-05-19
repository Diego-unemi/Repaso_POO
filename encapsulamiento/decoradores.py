def decorador (funcion): # La funcion de decorador es agregarle otra funcionalidad antes o despues de la funcion, esto se puede usar para hacer validaciones
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")
    return funcion_modificada

# def saludo():
#     print("Hola Diego")

# saludo_modificado = decorador(saludo)

# saludo_modificado()

@decorador
def saludo():
    print("Hola Diego como estas")

saludo()