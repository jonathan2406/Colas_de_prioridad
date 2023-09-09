import pickle

class db:
    
    @classmethod
    def serializar(cls, nombre_archivo, lista):
        with open(nombre_archivo, 'wb') as archivo:
            pickle.dump(lista, archivo)

    @classmethod
    def deserializar(cls, nombre_archivo):
        with open(nombre_archivo, 'rb') as archivo:
            return pickle.load(archivo)

