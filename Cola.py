from Excepciones import FullQueue, EmptyQueue


class Queue:
  cont_urgencias = 0
  def __init__(self):
    self.queue = []
    self.nombre_db = "db cola prioridad"

  def Agregar_solicitud(self, solicitud): #metodo formal donde se llaman a todos los metodos que se necesitan para agregar una solicitud
    self.agregar_numero_solicitud(solicitud) 
    self.encolar(solicitud)
    self.ordenamiento()

  def agregar_numero_solicitud(self, solicitud): #agrega el numero de solicitud de la persona en funcion de llegada de solicitudes historica
    Queue.cont_urgencias += 1
    solicitud.numero_solicitud = Queue.cont_urgencias

  def encolar(self, solicitud): #metodo que pega la solicitud
    self.queue.append(solicitud)

  def ordenamiento(self): #utilizamos el metodo sort para ordenar la cola en funcion de su numero de urgencia
    self.queue.sort(key=lambda x: x.nivel_urgencia)

      
  def dequeue(self):
    if(self.count == 0):
      raise EmptyQueue
    first = self.queue[0]
    for i in range(self.size-1):
      self.queue[i] = self.queue[i+1]
    self.queue[-1] = None
    self.count -= 1
    return first

  def first(self):
    if(self.count == 0):
      raise EmptyQueue
    first = self.queue[0]
    return first
  

  def atender_solicitud(self):
    pass
  
  def visualisar_solicitudes(self):
    pass

  def actualizar_urgencia(self):
    pass

  def ver_cola(self):
    for cosas in self.queue:
      print(cosas)

