
"""Validaciones del Sistema de Registro de Estudiantes."""


def validar_nombre(nombre):
    if not nombre.strip():
        return False, "El nombre no puede estar vacio."

    if len(nombre.strip()) < 3:
        return False, "El nombre debe tener al menos 3 caracteres."

    return True, "Nombre valido."


def validar_codigo(codigo):
    if not codigo.strip():
        return False, "El codigo es obligatorio."

    if not codigo.isdigit():
        return False, "El codigo solo debe contener numeros."

    return True, "Codigo valido."


def validar_carrera(carrera):
    if not carrera.strip():
        return False, "La carrera no puede estar vacia."

    return True, "Carrera valida."
