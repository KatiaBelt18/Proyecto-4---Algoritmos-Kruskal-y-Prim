'Clase nodo'

class Nodo:
    def __init__(self, n):
        self.identificador = n
        self.atributos = {}

    def __hash__(self):
        return hash(self.identificador)

    def __eq__(self, other):
        return isinstance(other, Nodo) and self.identificador == other.identificador

    def obtener_valor(self):
        return self.identificador

    def __repr__(self):
        return f"Nodo({self.identificador})"
