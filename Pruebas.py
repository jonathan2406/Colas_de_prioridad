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

    def probar(self, cola):
        try:
            nombre_archivo = input("Ingrese el nombre del csv: ")
            hora = datetime.datetime.now()
            l = Lectura_archivos()
            l.cargar_archivo(nombre_archivo)
            l.separar_archivo()

            # Creamos lotes basados en los niveles de urgencia presentes en el archivo CSV
            niveles_urgencia = set(int(datos[3]) for datos in l.archivo)
            if cola is None:
                cola = Queue()
                cola.añadir_lotes_al_diccionario(len(niveles_urgencia))
            else:
                # Si ya hay lotes, ajustamos la cantidad de lotes según los niveles de urgencia nuevos
                nuevos_niveles = len(niveles_urgencia) - len(cola.lotes)
                if nuevos_niveles > 0:
                    cola.añadir_lotes_al_diccionario(nuevos_niveles)

            cola = self.inyectar_cola(cola, l.archivo)
            self.atender_cola(cola)
            hora_finalizacion = datetime.datetime.now()
            print(f"La prueba demoró: {hora_finalizacion - hora} en completarse")
            return cola  # Devolvemos la cola actualizada
        except:
            print("Archivo CSV no encontrado")

    def inyectar_cola(self, cola, lista_datos):
        solicitudes = []
        for datos in lista_datos:
            numero_solicitud = datos[0] if datos[0] else None
            nueva_solicitud = Solicitud(numero_solicitud, datos[1], datos[2], int(datos[3]))
            solicitudes.append(nueva_solicitud)
        for solicitud in solicitudes:
            cola.Agregar_solicitud(solicitud)
        return cola
    
    def atender_cola(self, cola):
        for i in range(len(cola.queue)):
            cola.atender_solicitud()

