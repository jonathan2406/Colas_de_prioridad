from Excepciones import FullQueue, EmptyQueue
from Nivel_urgencia import Nivel_urgencia

class Queue:
  cont_urgencias = 0
  def __init__(self, size):
    self.queue = [None]*size
    self.size = size
    self.count = 0

  def enqueue(self, persona): #agrega
    if(self.count == self.size):
      raise FullQueue
    else:
      Queue.cont_urgencias += 1
      persona.numero_solicitud = Queue.cont_urgencias

  
      
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
  
  def set_size(self, espacios_añadir):
    for i in range(espacios_añadir):
      self.queue.append(None)
    self.size += espacios_añadir

  def __repr__(self):
    return str(self.queue)
  
  def agregar_solicitud(self):
    pass

  def atender_solicitud(self):
    pass
  
  def visualisar_solicitudes(self):
    pass

  def actualizar_urgencia(self):
    pass
  