class Nivel_urgencia:
    Lista_tipos_urgencias = []

    @classmethod
    def organizar_lista(cls):
        cls.Lista_tipos_urgencias.sort(key=lambda x: x.numero)

    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
        self.ultima_aparicion = 0




