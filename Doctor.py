# Clases hijas
from Persona import Persona
from Personal import Personal
class Doctor(Persona, Personal):
    def __init__(self, nombre, edad, id_personal, especialidad):
        Persona.__init__(self, nombre, edad)
        Personal.__init__(self, id_personal, "Doctora")
        self.especialidad = especialidad

    def mostrar_info_doctor(self):
        self.mostrar_info()
        self.mostrar_rol()
        print(f"Especialidad: {self.especialidad}")




