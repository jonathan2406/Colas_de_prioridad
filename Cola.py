from Excepciones import FullQueue, EmptyQueue

class Queue:
    cont_urgencias = 0

    def __init__(self):
        self.queue = []
        self.lotes = None
        self.nombre_db = "db cola prioridad"

    def añadir_lotes_al_diccionario(self, N):
        self.lotes = {i: Queue() for i in range(1, N + 1)}

    def Agregar_solicitud(self, solicitud):
        if solicitud.numero_solicitud == None:
            self.agregar_numero_solicitud(solicitud)
        self.encolar(solicitud)
        self.ordenamiento()
        self.lotes[solicitud.nivel_urgencia].Agregar_solicitud_por_nombre(solicitud)

    def Agregar_solicitud_por_nombre(self, solicitud):
        if solicitud.numero_solicitud == None:
            self.agregar_numero_solicitud(solicitud)
        self.encolar(solicitud)
        self.ordenamiento_por_nombre()

    def obtener_info_por_posicion(self, posicion):
        info_por_lote = {}
        for numero_lote, lote in self.lotes.items():
            if len(lote.queue) >= posicion:
                solicitud = lote.queue[posicion - 1]
                info_por_lote[numero_lote] = {
                    'Nombre del Cliente': solicitud.nombre_cliente,
                    'Nivel de Urgencia': solicitud.nivel_urgencia,
                    'Descripción del Problema': solicitud.descripcion_problema
                }
            else:
                info_por_lote[numero_lote] = 'No hay solicitud en esta posición'
        return info_por_lote


    def ordenamiento_por_nombre(self):
        self.queue.sort(key=lambda x: x.nombre_cliente)


    def agregar_numero_solicitud(self, solicitud):  # agrega el numero de solicitud de la persona en funcion de llegada de
        # solicitudes historica
        Queue.cont_urgencias += 1
        solicitud.numero_solicitud = Queue.cont_urgencias

    def encolar(self, solicitud):  # metodo que pega la solicitud
        self.queue.append(solicitud)

    def ordenamiento(self):  # utilizamos el metodo sort para ordenar la cola en funcion de su numero de urgencia
        self.queue.sort(key=lambda x: x.nivel_urgencia)

    def dequeue(self):
        if len(self.queue) == 0:
            raise EmptyQueue
        first = self.queue[0]
        del self.queue[0]  # Elimina el primer elemento en lugar de desplazarlos manualmente
        return first

    def first(self):
        if self.count == 0:
            raise EmptyQueue
        first = self.queue[0]
        return first

    def atender_solicitud(self):
        try:
            solicitud_atendida = self.dequeue()  # Atendemos la solicitud y lo sacamos de la cola.
            print(f"Atendiendo solicitud: {solicitud_atendida}")
        except EmptyQueue:
            print("La cola de solicitudes está vacía. No se puede atender ninguna solicitud.")

    def atender_lote(self, numero):
        while len(self.lotes[numero].queue)>0:
            self.lotes[numero].atender_solicitud()

        for i in range(len(self.queue)):
            if self.queue[i].nivel_urgencia == numero:
                self.queue[i] = None
            
        while None in self.queue:
            self.queue.remove(None)
        
    def visualizar_solicitud(self):
        print("Cola de solicitudes:")
        for solicitud in self.queue:  # Recorremos las solicitudes en la cola y mostramos los pacientes (clientes=
            print(
                f"Solicitud {solicitud.numero_solicitud}: Nombre: {solicitud.nombre_cliente}, Urgencia: "
                f"{solicitud.nivel_urgencia}, razón:{solicitud.descripcion_problema}")

    def actualizar_urgencia(self):
        try:
            numero_solicitud = int(input("Ingrese el número de solicitud que desea actualizar: "))
            for solicitud in self.queue:  # Recorremos la cola
                if solicitud.numero_solicitud == numero_solicitud:
                    # Seleccionamos el número de solicitud del # paciente
                    nuevo_nivel_urgencia = int(
                        input(f"Ingrese el nuevo nivel de urgencia para la solicitud {numero_solicitud}: "))
                    solicitud.nivel_urgencia = nuevo_nivel_urgencia
                    # Se cambia el nivel de urgencia del paciente
                    print(f"Nivel de urgencia actualizado para la solicitud {numero_solicitud}.")
                    self.ordenamiento()  # Reordenar la cola después de la actualización
                    return
            print(f"No se encontró la solicitud con número {numero_solicitud}.")
        except ValueError:
            print("Ingrese un número válido para la solicitud.")

    def ver_cola(self):
        for cosas in self.queue:
            print(cosas)

    def ver_lote(self, numero_lote):
        self.lotes[numero_lote].visualizar_solicitud()



