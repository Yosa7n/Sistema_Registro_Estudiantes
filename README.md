
# Sistema de Registro de Estudiantes

## Laboratorio N.º 05-B
**Asignatura:** Construcción de Software

### Integrantes
- Yosa7n - Integrante A
- Adriana Roque Quispe (its-aroque) - Integrante B

## Descripción del proyecto

Sistema de Registro de Estudiantes desarrollado en Python como parte del Laboratorio N.º 05-B.

El proyecto permite aplicar el trabajo colaborativo mediante Git y GitHub, utilizando ramas de funcionalidad, commits descriptivos, Pull Requests y resolución de conflictos de fusión.

## Funcionalidades implementadas

### 1. Registrar estudiantes
Permite ingresar:
- Nombre completo.
- Código universitario.
- Carrera profesional.

### 2. Listar estudiantes
Muestra los estudiantes registrados durante la ejecución del programa.

### 3. Buscar estudiantes
Permite buscar estudiantes mediante su código universitario.

Si el estudiante existe, muestra su información. Si no existe, presenta un mensaje informativo.

### 4. Validaciones
El sistema comprueba:
- Que el nombre tenga al menos 3 caracteres.
- Que el código universitario contenga solamente números.
- Que la carrera profesional no esté vacía.

## Estructura del proyecto

- main.py: Menú principal y funciones del sistema.
- validaciones.py: Validaciones de los datos.
- README.md: Documentación del proyecto.
- .gitignore: Exclusión de archivos temporales.

## Tecnologías utilizadas

- Python 3.x
- Visual Studio Code
- Git
- GitHub

## Ejecución

Abrir una terminal en la carpeta del proyecto y ejecutar:

    python main.py

Los registros se almacenan temporalmente en memoria mientras el programa está en funcionamiento.

## Trabajo colaborativo

Durante el laboratorio se desarrollaron funcionalidades utilizando ramas independientes.

Se realizaron Pull Requests para integrar los cambios en la rama main.

Adicionalmente, se provocó un Merge Conflict al modificar la misma línea de código desde dos ramas diferentes.

El conflicto se resolvió utilizando Visual Studio Code, conservando los aportes de ambos integrantes.

## Conclusión

El laboratorio permitió comprender la importancia del control de versiones distribuido y el trabajo colaborativo.

Git y GitHub facilitaron el seguimiento de cambios, la integración de funcionalidades y la resolución de conflictos de código.
