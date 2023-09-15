from Pickledb import db
from Cola import Queue
from Solicitud import Solicitud
from Pruebas import Pruebas


class GUI:

    def gui_crear_solicitud(self, cola):
        nombre_cliente = input("Ingrese nombre: ")
        descripcion = input("Ingrese descripcion de su problema: ")
        while True:
            nivel_urgencia = input("De 1 a 5 que que número considera es su urgencia siendo el 1 la mas grave y el 5 la mas leve: ")
            try:
                if int(nivel_urgencia) in [1, 2, 3, 4, 5]:
                    break
                else:
                    print("Ingresa un número valido")
                    continue
            except:
                print("Ingresaste un carácter invalido")
                continue
        #le mandamos un None como numero de solicitud ya que la propia clase cola se encarga de modificar ese valor
        # para poder utilizar ese mismo metodo añadir solicitud con la lectura de archivos que si poseen numero de solicitud
        nueva_solicitud = Solicitud(None,nombre_cliente, descripcion, int(nivel_urgencia))
        cola.Agregar_solicitud(nueva_solicitud)
        self.serializar(cola)
        #ademas metemos la solicitud en la cola que tiene su lote

    def menu(self):
        cola = self.actualizar_cola()
        print("♠️Bienvenido a la sala de urgencias♠️ \n---------------------------------")
        while True:
            print("Presione 1 para agregar una solicitud.")
            print("----------------------------------------------------------")
            print("Presione 2 para ver la cola de solicitudes.")
            print("----------------------------------------------------------")
            print("Presione 3 para atender una solicitud.")
            print("----------------------------------------------------------")
            print("Presione 4 para actualizar la urgencia de una solicitud.")
            print("----------------------------------------------------------")
            print("Presione 5 para salir del programa.")
            print("----------------------------------------------------------")
            print("Presione 6 para pruebas.")
            print("----------------------------------------------------------")
            print("Presione 7 para atender por lotes.")
            print("----------------------------------------------------------")
            print("Presione 8 para ver lote.")
            print("----------------------------------------------------------")
            decision = input("Ingrese su elección: ")

            if decision == "1":
                self.gui_crear_solicitud(cola)
            elif decision == "2":
                cola.visualizar_solicitud()
            elif decision == "3":
                cola.atender_solicitud()
            elif decision == "4":
                cola.actualizar_urgencia()
            elif decision == "5":
                self.serializar(cola)
                print("Programa finalizado.")
                break
            elif decision == "6":
                prueba = Pruebas()
                prueba.probar()

            elif decision =="7":
                while (True):
                    numero = input("ingrese el numero de urgencia que desea atender")
                    if numero not in "12345":
                        continue
                    else:
                        break
                cola.atender_lote(int(numero))

            elif decision == "8":
                while (True):
                    numero = input("ingrese el numero de lote que desea ver")
                    if numero in "12345":
                        break
                    else:
                        continue
                cola.ver_lote(int(numero))
                
            else:
                print("Elección no válida. Por favor, seleccione una opción válida.")

    def actualizar_cola(self):
        try:
            cola = Queue()
            cola = db.deserializar(cola.nombre_db)
            return cola
        except:
            cola.añadir_lotes_al_diccionario()
            return cola


    def serializar(self, cola):
        db.serializar(cola.nombre_db, cola)

