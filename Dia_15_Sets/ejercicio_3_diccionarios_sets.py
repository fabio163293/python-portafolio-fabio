asignaturas = {
    "Matemáticas": {"Ana", "Luis", "Pedro"},
    "Física": {"Luis", "María", "Pedro"},
    "Programación": {"Ana", "Pedro", "Carlos"},
}

comunes = asignaturas["Matemáticas"] & asignaturas["Física"] & asignaturas["Programación"]
print(F"Los o el estudiante de la siguiente lista estan en todas las materias: {comunes}")
comunes = asignaturas["Matemáticas"] & asignaturas["Física"]
print(f"Los o el estudiante en la siguiente lista se encuentra en Matemáticas y Física: {comunes} ")
comunes = asignaturas["Matemáticas"] & asignaturas["Programación"]
print(f"Los o el estudiante en la siguiente lista se encuentra en Matemáticas y Programación: {comunes}")
comunes = asignaturas["Programación"] & asignaturas["Física"]
print(f"Los o el estudiante en la siguiente lista se encuentra en Física y Programación: {comunes}")

solo_matematicas = asignaturas["Matemáticas"] - (asignaturas["Física"] - asignaturas["Programación"])
print(f"Los estudiante en la siguiente lista solo estan en una materia: {solo_matematicas}")

total_alumnos_distintos =  asignaturas["Matemáticas"] | asignaturas["Física"] | asignaturas["Programación"]
print(f"Los Alumnos son: {total_alumnos_distintos} siendo un total de {len(total_alumnos_distintos)}")