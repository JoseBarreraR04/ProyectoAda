"""
Análisis y Diseño de Algoritmos.
Jose Barrera Ramos - 8967442
Proyecto: A - FujikoMine
"""

from sys import stdin, stdout


# Key = (nodoActual, numInfecciones)
memoriaDP = {}

def aux():
    """
    :arg:
        -
        -
    :return:
        -
    """
    return 0

def optimizarArbol():
    """
    :return:
    """
    return 0

def main():
    """
    :return:
        -
    """
    for entrada in stdin:
        entrada = entrada.strip()

        if entrada:
            #  n            m              q
            numNodos, numTransmision, numConsultas = map(int, stdin.readline().split())

            Grafo = [[] for _ in range(numNodos)]
            for _ in range(numNodos - 1):
                #   u         v      w
                nodoActual, arista, peso = map(int, stdin.readline().split())
                Grafo[nodoActual].append((arista, peso))
                Grafo[arista].append((nodoActual, peso))

            nodosTransmision = list(map(int, stdin.readline().split()))
            queries = list(map(int, stdin.readline().split()))

            solucion = 0
            stdout.write(f"{solucion}\n")

    return 0

main()