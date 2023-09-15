import pickle

class db:
    
    @classmethod
    def serializar(cls, nombre_archivo, objeto):
        with open(nombre_archivo, 'wb') as archivo:
            pickle.dump(objeto, archivo)

    @classmethod
    def deserializar(cls, nombre_archivo):
        with open(nombre_archivo, 'rb') as archivo: 
            objeto = pickle.load(archivo)
            return objeto

