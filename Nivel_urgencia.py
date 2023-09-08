class Nivel_urgencia:
    Lista_tipos_urgencias = []
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
        self.ultima_aparicion = None