from Pickledb import db
from Cola import Queue
from Solicitud import Solicitud
from Pruebas import Pruebas


class GUI:

    def gui_crear_solicitud(self, cola):
        nombre_cliente = input("Ingrese nombre: ")
        descripcion = input("Ingrese descripcion de su problema: ")
        while True:
            try:
                nivel_urgencia = int(
                    input(f"De 1 a {len(cola.lotes)}, ¿qué número considera como su nivel de urgencia? "))
                if 1 <= nivel_urgencia <= len(cola.lotes):
                    break
                else:
                    print(f"Ingrese un número entre 1 y {len(cola.lotes)}.")
            except ValueError:
                print("Ingrese un número válido.")
        # le mandamos un None como numero de solicitud ya que la propia clase cola se encarga de modificar ese valor
        # para poder utilizar ese mismo metodo añadir solicitud con la lectura de archivos que si poseen numero de
        # solicitud
        nueva_solicitud = Solicitud(None, nombre_cliente, descripcion, int(nivel_urgencia))
        cola.Agregar_solicitud(nueva_solicitud)
        self.serializar(cola)
        # ademas metemos la solicitud en la cola que tiene su lote

    def obtener_posicion_a_consultar(self):
        while True:
            try:
                posicion = int(input("Ingrese la posición que desea consultar: "))
                if posicion > 0:
                    return posicion
                else:
                    print("Ingrese un número positivo.")
            except ValueError:
                print("Ingrese un número válido.")

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
            print("Presione 9 para consultar información por posición en los lotes.")
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
                cola = prueba.probar(cola)
            elif decision == "7":
                while True:
                    try:
                        numero = int(input("Ingrese el número de urgencia que desea atender: "))
                        if 1 <= numero <= len(cola.lotes):
                            break
                        else:
                            print(f"Ingrese un número entre 1 y {len(cola.lotes)}.")
                    except ValueError:
                        print("Ingrese un número válido.")
                cola.atender_lote(numero)

            elif decision == "8":
                while True:
                    try:
                        numero = int(input("Ingrese el número de lote que desea ver: "))
                        if 1 <= numero <= len(cola.lotes):
                            break
                        else:
                            print(f"Ingrese un número entre 1 y {len(cola.lotes)}.")
                    except ValueError:
                        print("Ingrese un número válido.")
                cola.ver_lote(numero)

            elif decision == "9":
                posicion = self.obtener_posicion_a_consultar()
                info_lotes = cola.obtener_info_por_posicion(posicion)
                for numero_lote, info in info_lotes.items():
                    print(f'Lote {numero_lote}: {info}')
            else:
                print("Elección no válida. Por favor, seleccione una opción válida.")

    def actualizar_cola(self):
        try:
            cola = Queue()
            cola = db.deserializar(cola.nombre_db)
            return cola
        except:
            while True:
                try:
                    cantidad_lotes = int(input("Ingrese la cantidad de lotes que desea crear: "))
                    if cantidad_lotes > 0:
                        cola.añadir_lotes_al_diccionario(cantidad_lotes)
                        return cola
                    else:
                        print("Ingrese un número positivo.")
                except ValueError:
                    print("Ingrese un número válido.")

    def serializar(self, cola):
        db.serializar(cola.nombre_db, cola)
