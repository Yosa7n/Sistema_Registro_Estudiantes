
"""Sistema de Registro de Estudiantes - Laboratorio 05-B."""

from validaciones import validar_nombre, validar_codigo, validar_carrera

MENSAJE_BIENVENIDA = "PLATAFORMA UNIVERSITARIA ACADEMICO DE GESTION ESTUDIANTIL"

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


def buscar_estudiante():
    print("\n--- BUSCAR ESTUDIANTE ---")

    codigo = input("Ingrese el codigo universitario: ").strip()

    if not codigo:
        print("Debe ingresar un codigo.")
        return

    for estudiante in estudiantes:
        if estudiante["codigo"] == codigo:
            print("\nEstudiante encontrado:")
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Codigo: {estudiante['codigo']}")
            print(f"Carrera: {estudiante['carrera']}")
            return

    print("\nNo se encontro un estudiante con ese codigo.")


def main():
    while True:
        print(f"\n===== {MENSAJE_BIENVENIDA} =====")
        print("1. Registrar estudiante")
        print("2. Listar estudiantes")
        print("3. Buscar estudiante por codigo")
        print("4. Salir")

        opcion = input("\nSeleccione una opcion: ").strip()

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            listar_estudiantes()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
