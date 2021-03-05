from laberinto import laberinto
from individuo import individuo

class poblacion():
    def __init__(self, _numPoblacion, _laberinto):
        self.poblacion = []
        self.numPoblacion = _numPoblacion
        for i in range (_numPoblacion):
            temp = individuo(_laberinto, [])
            self.poblacion.append(temp)
    def get_poblacion(self):
        return self.poblacion