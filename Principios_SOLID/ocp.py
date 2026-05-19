#Open/Closed Principle
# las clases modulos funciones metodos etc.. , deben estar abiertas para la extension pero cerradas para la modificacion
#deberiamos agregar nuevas funcionalidades sin tener que cambiar el codigo fuente de esta clases u otras entidades
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando Email a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}")

class NotificadorWhatsApp(Notificador):
    def Notificar(self):
        print(f"Enviando whatsapp a {self.usuario.whatsapp}")




    