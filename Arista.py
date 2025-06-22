from Nodo import *

'Clase Arista'

class Arista:
    def __init__(self, origen, destino, peso=1):
        self.origen = origen          # Espera objetos Nodo ya existentes
        self.destino = destino
        self.peso = peso
        self.atributos = {"peso": peso}

    def obtener_peso(self):
        return self.peso

    def __eq__(self, other):
        return (
            isinstance(other, Arista) and
            self.peso == other.peso and
            ((self.origen == other.origen and self.destino == other.destino) or
             (self.origen == other.destino and self.destino == other.origen))
        )

    def __hash__(self):
        return hash(frozenset([self.origen, self.destino])) ^ hash(self.peso)

    def __repr__(self):
        return f"Arista({self.origen}-{self.destino}, peso={self.peso})"


