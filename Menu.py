from Pickledb import db
from Cola import Queue
from Solicitud import Solicitud

class Gui:


    def gui_crear_solicitud(self,cola):
        nombre_cliente = input("Ingrese nombre: ")
        descripcion = input("ingrese descripcion de su problema")
        while(True):
            nivel_urgencia = input("de 1 a 5 que que numero considera es su urgencia siendo el 1 la mas grave y el 5 la mas leve")
            try:
                if int(nivel_urgencia) in [1,2,3,4,5]:
                    break
                else:
                    print("Ingresa un numero valido")
                    continue
            except:
                print("Ingresaste un caracter invalido")
                continue
        nueva_solicitud = Solicitud(nombre_cliente, descripcion, int(nivel_urgencia))
        cola.Agregar_solicitud(nueva_solicitud)
        self.serializar(cola)
        


    def menu(self):
        cola = self.actualizar_cola() #cuando inicimaos el menu llamamos a los metodos que se encargan de cargar los objetos serializados en la lista de ejecucin
        print("Bienvenido a la sala de urgencias \n---------------------------------")
        while(True):
            print("presione 1 para agregar una solicitud \npresione 2 para ver la cola: ")
            decision = input()

            if decision == "1":
                self.gui_crear_solicitud(cola)
                print("paso la gui")
                continue

            if decision == "2": #puse este metodo solo para probar si ordenaba bien
                cola.ver_cola()
                continue
            

            
    def actualizar_cola(self):
        try:
            cola = Queue()
            cola.queue = db.deserializar(cola.nombre_db)
            return cola
        except:
            return cola
        
    def serializar(self,cola):
        db.serializar(cola.nombre_db,cola.queue)

                
    