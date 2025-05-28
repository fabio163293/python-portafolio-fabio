from datetime import datetime, timedelta
import os   
import shutil
import utilidades 

#registra los movimientos  y log guarda en un archivo
#Logs the movements and saves the log in a file
def registrar_log(ruta_log, mensaje):
    with open (ruta_log, 'a') as log:
        registro_tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f'{registro_tiempo}, {mensaje}')

#Crea backup de los archivos y tambien lo registra en un log 
#Creates a backup of the files and also logs it in a log file
def backup_archivo(directorio, prefijo, directorio_backup):
    for archivo in os.listdir(directorio):
        if os.path.isfile(archivo):
            shutil.copy2(archivo, directorio_backup)
            nuevo_nombre = f"{prefijo}_{archivo}"
            os.rename(
                os.path.join(directorio_backup, archivo),
                os.path.join(directorio_backup, nuevo_nombre)
            )
            registrar_log('actividad.log',f"El archivo {directorio} se le realizo un respaldo")
            print(f"backup realizado: {archivo} a {nuevo_nombre}")           

#suma o resta dias a la fecha actual y devuelve el resultado 
#Adds or subtracts days from the current date and returns the result
def calcular_dia():
    dia_actual = datetime.now()
    dia_calcular = utilidades.validar_entero("Por favor indique el dia a sumar o restar ")
    return dia_actual - timedelta(days=dia_calcular)


def main():
    #ejemplo de uso
    #Example of use    
    backup_archivo('.','backup', 'actividad.log')
    print(calcular_dia())

if __name__ == '__main__':
   main()

