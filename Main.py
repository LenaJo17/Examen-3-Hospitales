from Doctor import Doctor
from Enfermera import Enfermera
from Paciente import Paciente

def principal():
    # Crear instancias de Doctor, Enfermera y Paciente
    doctor = Doctor("Dr. Gisela", 54, "D123", "Oncologia")
    enfermera = Enfermera(" Analissa", 34, "N456", "Noche")
    paciente = Paciente("Jose", 60, "Hospital Central", "Sala 101", "Cáncer")

    # Mostrar información de cada instancia
    print("\nInformación del Doctor:")
    doctor.mostrar_info_doctor()

    print("\nInformación de la Enfermera:")
    enfermera.mostrar_info_enfermera()

    print("\nInformación del Paciente:")
    paciente.mostrar_info_paciente()

# Ejecutar la función principal
if __name__ == "__main__":
    principal()



