from Solicitud import Solicitud
from Cola import Queue
import datetime

class Lectura_archivos:
    
    def __init__(self):
        self.archivo = None
    
    def cargar_archivo(self, nombre_archivo):
        with open(f'{nombre_archivo}.csv', 'r') as archivo:
            self.archivo = archivo.readlines()

    def separar_archivo(self):
        lista_final = []
        for linea in self.archivo:
            # Elimina el carácter de salto de línea al final de cada línea
            linea = linea.strip()
            # Divide la línea en valores separados por comas
            valores = linea.split(',')
            # Agrega la lista de valores de esta línea a la lista principal
            lista_final.append(valores)
        self.archivo = lista_final
            
class Pruebas:

    def probar(self):
        try:
            cola = Queue()
            nombre_archivo = input("Ingrese el nombre del csv: ")
            hora = datetime.datetime.now()
            l = Lectura_archivos()
            l.cargar_archivo(nombre_archivo)
            l.separar_archivo()
            self.atender_cola(self.inyectar_cola(cola, l.archivo))
            hora_finalizacion = datetime.datetime.now()
            print(f"La prueba demoro: {hora_finalizacion - hora} en completarse")
        except:
            print("Archivo csv no encontrado")
            
        

    def inyectar_cola(self, cola, lista_datos):
        solicitudes = []
        for i in range(len(lista_datos)):
            nueva_solicitud = Solicitud(lista_datos[i][0],lista_datos[i][1],lista_datos[i][2],lista_datos[i][3])
            solicitudes.append(nueva_solicitud)
        for j in range(len(solicitudes)):
            cola.Agregar_solicitud(solicitudes[j])
        return cola
    
    def atender_cola(self, cola):
        for i in range(len(cola.queue)):
            cola.atender_solicitud()

