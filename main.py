from Cola import Queue
from Solicitud import Solicitud

cola = Queue(5)
soli1 = Solicitud("pepe", "tengo_frio", )

print(cola.queue)
cola.enqueue(soli1)
print(cola.queue)
cola.atender_solicitud()
