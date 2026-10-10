
"""Sistema de Registro de Estudiantes - Laboratorio 05-B."""
from validaciones import validar_nombre, validar_codigo, validar_carrera
MENSAJE_BIENVENIDA = "SISTEMA ACADEMICO DE REGISTRO DE ESTUDIANTES"

estudiantes = []


def registrar_estudiante():
    print("\n--- REGISTRAR ESTUDIANTE ---")

    nombre = input("Nombre completo: ").strip()
    codigo = input("Codigo universitario: ").strip()
    carrera = input("Carrera profesional: ").strip()

    # Verificar los datos antes del registro
    for valor, funcion in [
        (nombre, validar_nombre),
        (codigo, validar_codigo),
        (carrera, validar_carrera)
    ]:
        valido, mensaje = funcion(valor)

        if not valido:
            print(f"\nError: {mensaje}")
            return

    estudiante = {
        "nombre": nombre,
        "codigo": codigo,
        "carrera": carrera
    }

    estudiantes.append(estudiante)
    print("\nEstudiante registrado correctamente.")


def listar_estudiantes():
    print("\n--- LISTA DE ESTUDIANTES ---")

    if not estudiantes:
        print("No existen estudiantes registrados.")
        return

    for numero, estudiante in enumerate(estudiantes, 1):
        print(f"\nEstudiante {numero}")
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Codigo: {estudiante['codigo']}")
        print(f"Carrera: {estudiante['carrera']}")


def main():
    while True:
        print(f"\n===== {MENSAJE_BIENVENIDA} =====")
        print("1. Registrar estudiante")
        print("2. Listar estudiantes")
        print("3. Salir")

        opcion = input("\nSeleccione una opcion: ").strip()

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            listar_estudiantes()
        elif opcion == "3":
            print("Programa finalizado.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
