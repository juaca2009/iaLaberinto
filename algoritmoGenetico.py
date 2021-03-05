from laberinto import laberinto
from individuo import individuo
from poblacion import poblacion
import random

class algoritmo_genetico():
    def __init__(self, _probabilidadMutacion, _tamanoPoblacion, _numeroGeneracion, _porcentajePoblacionE, _porcentajeCruce, _laberinto):
        self.probabilidadMutacion = _probabilidadMutacion
        self.tamanoPoblacion = _tamanoPoblacion
        self.tamanoPoblacionE = int((_porcentajePoblacionE*self.tamanoPoblacion)/100)
        self.numeroGeneraciones = _numeroGeneracion
        self.porcentajeCruce = _porcentajeCruce
        self.laberinto = _laberinto
        self.poblacion = poblacion(_tamanoPoblacion, _laberinto)

    def cruce_unPunto(self, padre1, padre2):
        padre1M = padre1.get_movimientos()
        padre2M = padre2.get_movimientos()
        puntoCorte = random.randint(0, len(padre1M))
        cria1 = individuo(self.laberinto, list((padre1M[0:puntoCorte] + padre2M[puntoCorte:]))) 
        cria2 = individuo(self.laberinto, list((padre2M[0:puntoCorte] + padre1M[puntoCorte:])))
        return cria1, cria2

    def mutacion(self, indv):
        porcentaje = random.randrange(0, 100)
        if porcentaje <= self.probabilidadMutacion:
            indice = random.randrange(0, len(indv.get_movimientos()))
            cambio = indv.posiblesMovimientos[random.randrange(0, len(indv.posiblesMovimientos))]
            indv.movimientos[indice] = cambio
            return indv
        else:
            return indv

    def seleccion(self, _poblacion):
        _poblacion.sort(key=lambda x: x[0])
        seleccionados = _poblacion[len(_poblacion)-self.tamanoPoblacionE :]
        return seleccionados

    def evolucion(self):
        pobla = self.poblacion.get_poblacion()
        for gen in range(0, self.numeroGeneraciones):
            individuosFitness = []
            if gen == 0:
                for i in pobla:
                    individuosFitness.append([i.puntuacionFitness, i])
            else:
                individuosFitness = newGen
            newGen = []
            cantCruce = int((self.porcentajeCruce*len(individuosFitness))/100)
            for i in range(cantCruce):
                padre1 = random.choice(individuosFitness)
                padre2 = random.choice(individuosFitness)
                crias = self.cruce_unPunto(padre1[1], padre2[1])
                cria1 = self.mutacion(crias[0])
                cria2 = self.mutacion(crias[1])
                newGen.append([cria1.calcular_fitness(self.laberinto), cria1])
                newGen.append([cria2.calcular_fitness(self.laberinto), cria2])
            newGen = self.seleccion(newGen)
        print("Final Individual: ", individuosFitness[len(individuosFitness)-1][1].get_movimientos(), " ",  individuosFitness[len(individuosFitness)-1][1].puntuacionFitness)
        return individuosFitness[len(individuosFitness)-1][1].get_movimientos()
                



