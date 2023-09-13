class Solicitud:

    def __init__(self, numero_solicitud, nombre_cliente, descripcion_problema, nivel_urgencia):
        self.numero_solicitud = numero_solicitud
        self.nombre_cliente = nombre_cliente
        self.descripcion_problema = descripcion_problema
        self.nivel_urgencia = nivel_urgencia

    def __repr__(self):
        return self.nombre_cliente + " " + str(self.nivel_urgencia)
    


