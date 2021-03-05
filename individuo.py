from laberinto import laberinto
import random

class individuo():
    def __init__(self, _laberinto, _movimientos):
        self.posiblesMovimientos = ['U', 'D', 'L', 'R']
        for i in range(0, len(_laberinto.lab)):
            if 'S' in _laberinto.lab[i]:
                self.localizacionX = _laberinto.lab[i].index('S') #colomna donde esta el inicio
                self.localizacionY = i #fila donde esta el inicio
        if _movimientos:
            self.movimientos = _movimientos
        else:
            self.movimientos = []
            for i in range(0, _laberinto.cantMov * 2):
                self.movimientos.append(self.posiblesMovimientos[random.randrange(0, 4)])
        self.puntuacionFitness = 0

    def get_movimientos(self):
        return str(''.join(self.movimientos))

    def calcular_fitness(self, _laberinto):
        mov = self.get_movimientos()
        long_filas = len(_laberinto.lab)
        long_columnas = len(_laberinto.lab[0])
        for i in mov:
            if i == 'U' and not self.localizacionY + 1 >= long_filas:
                if _laberinto.lab[self.localizacionY+1][self.localizacionX] == '-':
                    self.puntuacionFitness = self.puntuacionFitness + 1
                    self.localizacionY = self.localizacionY + 1
                elif _laberinto.lab[self.localizacionY + 1][self.localizacionX] == 'O':
                    self.puntuacionFitness = self.puntuacionFitness + 1
                    self.puntuacionFitnessn= self.puntuacionFitness + len(mov)
                elif self.localizacionY + 1 > len(_laberinto.lab):
                    self.puntuacionFitness = self.puntuacionFitness + 0
                else:
                    self.puntuacionFitness = self.puntuacionFitness + 0
            elif i == 'D' and not self.localizacionY -1 < 0:
                if _laberinto.lab[self.localizacionY - 1][self.localizacionX] == '-':
                    self.puntuacionFitness = self.puntuacionFitness + 1
                    self.localizacionY = self.localizacionY - 1
                elif _laberinto.lab[self.localizacionY - 1][self.localizacionX] == 'O':
                    self.puntuacionFitness = self.puntuacionFitness + 1
                    self.puntuacionFitness = self.puntuacionFitness + len(mov)
                elif self.localizacionY - 1 < 0:
                    self.puntuacionFitness = self.puntuacionFitness + 0
                else:
                    self.puntuacionFitness = self.puntuacionFitness + 0
            elif i == 'L' and not self.localizacionX - 1 < 0:
                if self.localizacionX - 1 > len(_laberinto.lab[self.localizacionY]) or self.localizacionX -1 < 0:
                    self.puntuacionFitness = self.puntuacionFitness + 0
                elif _laberinto.lab[self.localizacionY][self.localizacionX-1] == '-':
                    self.puntuacionFitness = self.puntuacionFitness + 1
                    self.localizacionX = self.localizacionX - 1
                elif _laberinto.lab[self.localizacionY][self.localizacionX-1] == 'O':
                    self.puntuacionFitness = self.puntuacionFitness + 1
                    self.puntuacionFitness = self.puntuacionFitness + len(mov)
                elif self.localizacionX + 1 > len(_laberinto.lab[self.localizacionY]):
                    self.puntuacionFitness = self.puntuacionFitness + 0
                else:
                    self.puntuacionFitness = self.puntuacionFitness + 0
            elif i == 'R' and not self.localizacionX + 1 >= long_columnas:
                if _laberinto.lab[self.localizacionY][self.localizacionX+1] == '-':
                    self.puntuacionFitness = self.puntuacionFitness + 1
                    self.localizacionX = self.localizacionX + 1
                elif _laberinto.lab[self.localizacionY][self.localizacionX+1] == 'O':
                    self.puntuacionFitness = self.puntuacionFitness + 1
                    self.puntuacionFitness = self.puntuacionFitness + len(mov)
                elif self.localizacionX - 1 < 0:
                    self.puntuacionFitness = self.puntuacionFitness + 0
                else:
                    self.puntuacionFitness = self.puntuacionFitness + 0
            else:
                self.puntuacionFitness = self.puntuacionFitness + 0
        return self.puntuacionFitness



