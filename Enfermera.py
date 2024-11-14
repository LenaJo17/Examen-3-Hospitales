# Hereda de Empleado
from Persona import Persona
from Personal import Personal

class Enfermera(Persona, Personal):
    def __init__(self, nombre, edad, id_personal, turno):
        Persona.__init__(self, nombre, edad)
        Personal.__init__(self, id_personal, "Enfermera")
        self.turno = turno

    def mostrar_info_enfermera(self):
        self.mostrar_info()  # Llamada al método mostrar_info() de Persona
        self.mostrar_rol()  # Llamada al método mostrar_rol() de PersonalHospitalario
        print(f"Turno: {self.turno}")



