def datos_consola():
    lista_notas = []

    while True:
        try:
            titulo = input("Por favor indique el título, 'continuar' para cargar el archivo y 'salir' para finalizar: ")

            if titulo.lower() == 'salir':
                print("Gracias por el uso del sistema")
                break

            if titulo.lower() != 'continuar':
                descripcion = input("Por favor indique la descripción: ")
                nota = {'titulo': titulo, 'descripcion': descripcion}
                lista_notas.append(nota)
                continue
            else:
                if not lista_notas:
                    print("La lista está vacía.")
                    return None
                return guardar_en_archivo(lista_notas)

        except KeyboardInterrupt:
            print("\nPrograma finalizado por usuario")
            break

def guardar_en_archivo(lista_notas, nombre_archivo="notas.txt"):
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for nota in lista_notas:
                linea = f"Título: {nota['titulo']}\nDescripción: {nota['descripcion']}\n\n"
                archivo.write(linea)
        print(f"Notas guardadas exitosamente en '{nombre_archivo}'.")
        return True

    except PermissionError:
        print(f"Error: No tienes permisos para escribir en el archivo '{nombre_archivo}'.")
        return False
    except Exception as e:
        print(f"Ocurrió un error al guardar las notas: {e}")
        return False
    

datos_consola()    
 

