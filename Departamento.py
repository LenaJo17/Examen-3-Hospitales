class Departamento:
    def __init__(self, nombre_departamento, jefe_departamento):
        self.nombre_departamento = nombre_departamento
        self.jefe_departamento = jefe_departamento

    def mostrar_info_departamento(self):
        print(f"Departamento: {self.nombre_departamento}, Jefe: {self.jefe_departamento}")




