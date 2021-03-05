from laberinto import laberinto
from individuo import individuo
from poblacion import poblacion
from algoritmoGenetico import algoritmo_genetico
from maze import Maze

def main():
    labe = laberinto()
    #pormutacion, tamanoPoblacion, numeroGeneracion, porcentajePoblacionE, porcentajeCruce, laberinto
    ag = algoritmo_genetico(30, 2000, 100, 70, 90, labe)
    m = Maze(labe.lab)
    m.Visualize()
    m.RunMaze(ag.evolucion())
    salir = input("ENTER para salir.")
    

main()