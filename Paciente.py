from Persona import Persona

class Paciente(Persona):
    def __init__(self, nombre, edad, nombre_instalacion, ubicacion, enfermedad):
        # Inicializa la clase Persona
        Persona.__init__(self, nombre, edad)
        # Atributos específicos de Paciente
        self.nombre_instalacion = nombre_instalacion
        self.ubicacion = ubicacion
        self.enfermedad = enfermedad

    def mostrar_info_paciente(self):
        self.mostrar_info()  # Mostrar información de la persona
        print(f"Instalación: {self.nombre_instalacion}, Ubicación: {self.ubicacion}")
        print(f"Enfermedad: {self.enfermedad}")
