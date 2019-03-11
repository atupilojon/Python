
from personas import *

class Agenda:

    def __init__(self):
        self.personas = []

    def __repr__(self):
        return f"{self.personas}"

    def agregarPersona(self,persona):
        self.personas.append(persona)

    def save(self):
        file = open('agenda.txt', 'w')
        for persona in self.personas:
            file.write(persona.savePersona())
        file.close()

    def load(self):
        file = open('agenda.txt', 'r')
        exec(file.read())
