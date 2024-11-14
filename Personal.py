class Personal:
    def __init__(self, id_personal, rol):
        self.id_personal = id_personal
        self.rol = rol

    def mostrar_rol(self):
        print(f"ID Personal: {self.id_personal}, Rol: {self.rol}")

