
from agenda import *

class Persona:

    id = 1

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.email = None
        self.telefono = []
        self.id = Persona.id
        Persona.id +=1

    def __repr__(self):
        return f"{self.id} {self.nombre} {self.apellido}"

    def agregarTelefono(self, telefono):
        self.email.append(telefono)

    def agregarEmail(self, email):
        self.email = email

    def savePersona(self):
        return (f"p{self.id} = Persona("
               f"'{self.nombre}','{self.apellido}','{self.email}',{self.telefono},{self.id})"
               )
