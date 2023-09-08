from Nivel_urgencia import Nivel_urgencia

class Menu:

    def crear_nivel_urgencia(self, nombre, numero_gravedad):
        nuevo_tipo_urgencia = Nivel_urgencia(nombre, numero_gravedad)
        Nivel_urgencia.Lista_tipos_urgencias.append(nuevo_tipo_urgencia)
        Nivel_urgencia.organizar_lista()

    def gui_crear_nivel_urgencia(self):
        nombre = input("Ingrese el nombre de la urgencia ")
        if len(Nivel_urgencia.Lista_tipos_urgencias) > 0: 
            print("Estas son las urgencias que ya existen: ")
        numeros_existentes = []
        for i in range(len(Nivel_urgencia.Lista_tipos_urgencias)-1):
            numeros_existentes.append(Nivel_urgencia.Lista_tipos_urgencias[i].numero)
            print(f"nombre: {Nivel_urgencia.Lista_tipos_urgencias[i].nombre} \nnumero urgencia: {Nivel_urgencia.Lista_tipos_urgencias[i].numero}")


        while(True):
            try:
                numero = int(input("ingrese el numero que de su urgencia: "))
                if numero in numeros_existentes:
                    print("ese numero ya existe")
                    continue
                elif numero <= 0:
                    print("debe ser un numero mayor o igual a 0")
                    continue
            except:
                print("ingrese un numero valido")
                continue
            break

        self.crear_nivel_urgencia(nombre,numero)
        print("urgencia creada...")


eo = Menu()

eo.gui_crear_nivel_urgencia()