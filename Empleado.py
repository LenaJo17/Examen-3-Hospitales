#Hereda de Persona y representa al personal
from Persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, genero, id_empleado, salario):
        super().__init__(nombre, edad, genero)
        self._id_empleado = id_empleado
        self._salario = salario

    # Getters and setters
    def get_id_empleado(self):
        return self._id_empleado

    def set_id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        self._salario = salario

