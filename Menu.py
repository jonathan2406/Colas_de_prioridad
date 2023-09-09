from Pickledb import db
from Cola import Queue
from Solicitud import Solicitud


class GUI:

    def gui_crear_solicitud(self, cola):
        nombre_cliente = input("Ingrese nombre: ")
        descripcion = input("Ingrese descripcion de su problema: ")
        while True:
            nivel_urgencia = input(
                "De 1 a 5 que que número considera es su urgencia siendo el 1 la mas grave y el 5 la mas leve: ")
            try:
                if int(nivel_urgencia) in [1, 2, 3, 4, 5]:
                    break
                else:
                    print("Ingresa un número valido")
                    continue
            except:
                print("Ingresaste un carácter invalido")
                continue
        nueva_solicitud = Solicitud(nombre_cliente, descripcion, int(nivel_urgencia))
        cola.Agregar_solicitud(nueva_solicitud)
        self.serializar(cola)

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
            else:
                print("Elección no válida. Por favor, seleccione una opción válida.")

    def actualizar_cola(self):
        try:
            cola = Queue()
            cola.queue = db.deserializar(cola.nombre_db)
            return cola
        except:
            return cola

    def serializar(self, cola):
        db.serializar(cola.nombre_db, cola.queue)
