from grafos import Accion
from grafos import Estado
from grafos import Nodo
from grafos import Problema
import heapq

class BusquedaAStar:
    def __init__(self, problema):
        self.problema = problema

    def a_estrella(self):
        # La cola de prioridad para A*, que contiene nodos ordenados por el valor f = coste + heurística
        open_list = []
        # Diccionario de nodos ya visitados
        closed_list = {}

        # Crear el nodo inicial
        nodo_inicial = Nodo(self.problema.estado_inicial, None, self.problema.acciones[self.problema.estado_inicial.nombre], None)
        nodo_inicial.coste = 0
        nodo_inicial.heuristicas = self.problema.heuristicas[nodo_inicial.estado.nombre]
        nodo_inicial.valores = {estado: heuristica + nodo_inicial.coste
                                for estado, heuristica in nodo_inicial.heuristicas.items()}
        
        # Insertar el nodo inicial en la lista abierta (priority queue)
        heapq.heappush(open_list, (nodo_inicial.valores[self.problema.estados_objetivos[0].nombre], nodo_inicial))

        while open_list:
            # Sacar el nodo con el menor valor f = coste + heurística
            _, nodo_actual = heapq.heappop(open_list)
            
            # Si llegamos a un estado objetivo, retornamos el camino
            if self.problema.es_objetivo(nodo_actual.estado):
                return self.reconstruir_camino(nodo_actual)
            
            # Añadir el nodo actual a la lista cerrada (visited nodes)
            closed_list[nodo_actual.estado.nombre] = nodo_actual

            # Expandir los nodos hijos
            hijos = nodo_actual.expandir(self.problema)

            for hijo in hijos:
                if hijo.estado.nombre in closed_list:
                    continue  # Ignorar nodos ya visitados
                
                # Calcular el valor de f = coste + heurística
                hijo.valores = {estado: heuristica + hijo.coste for estado, heuristica in hijo.heuristicas.items()}
                
                # Si el hijo no está en la lista abierta o tiene un valor menor, agregarlo
                if not any(hijo.estado.nombre == node[1].estado.nombre for node in open_list):
                    heapq.heappush(open_list, (hijo.valores[self.problema.estados_objetivos[0].nombre], hijo))
        
        return None  # Si no se encuentra solución

    def reconstruir_camino(self, nodo):
        camino = []
        while nodo:
            camino.append(nodo.estado.nombre)
            nodo = nodo.padre
        return camino[::-1]  # Invertir para mostrar el camino desde el inicio al objetivo

if __name__ == '__main__':
    # Ejemplo de ejecución
    accN = Accion('norte')
    accS = Accion('sur')
    accE = Accion('este')
    accO = Accion('oeste')

    coruna = Estado('A Coruña', [accS, accE])
    bilbao = Estado('Bilbao', [accS, accE, accO])
    barcelona = Estado('Barcelona', [accS, accO])
    lisboa = Estado('Lisboa', [accN, accS, accE])
    madrid = Estado('Madrid', [accN, accS, accE, accO])
    valencia = Estado('Valencia', [accN, accS, accO])
    faro = Estado('Faro', [accN, accE])
    sevilla = Estado('Sevilla', [accN, accE, accO])
    granada = Estado('Granada', [accN, accO])

    viajes = {'A Coruña': {'sur': lisboa,
                           'este': bilbao},
              'Bilbao': {'sur': madrid,
                         'este': barcelona,
                         'oeste': coruna},
              'Barcelona': {'sur': valencia,
                            'oeste': bilbao},
              'Lisboa': {'norte': coruna,
                         'sur': faro,
                         'este': madrid},
              'Madrid': {'norte': bilbao,
                         'sur': sevilla,
                         'este': valencia,
                         'oeste': lisboa},
              'Valencia': {'norte': barcelona,
                           'sur': granada,
                           'oeste': madrid},
              'Faro': {'norte': lisboa,
                       'este': sevilla},
              'Sevilla': {'norte': madrid,
                          'este': granada,
                          'oeste': faro},
              'Granada': {'norte': valencia,
                          'oeste': sevilla}}

    kms = {'A Coruña': {'sur': 608,
                        'este': 545},
           'Bilbao': {'sur': 408,
                      'este': 613,
                      'oeste': 545},
           'Barcelona': {'sur': 350,
                         'oeste': 613},
           'Lisboa': {'norte': 608,
                      'sur': 278,
                      'este': 624},
           'Madrid': {'norte': 408,
                      'sur': 534,
                      'este': 357,
                      'oeste': 624},
           'Valencia': {'norte': 350,
                        'sur': 487,
                        'oeste': 357},
           'Faro': {'norte': 278,
                    'este': 200},
           'Sevilla': {'norte': 534,
                       'este': 252,
                       'oeste': 200},
           'Granada': {'norte': 487,
                       'oeste': 252}}

    distancias = {'A Coruña': {'A Coruña': 0,
                               'Bilbao': 443,
                               'Barcelona': 895,
                               'Lisboa': 522,
                               'Madrid': 509,
                               'Valencia': 797,
                               'Faro': 687,
                               'Sevilla': 696,
                               'Granada': 799},
                  'Bilbao': {'A Coruña': 443,
                             'Bilbao': 0,
                             'Barcelona': 468,
                             'Lisboa': 725,
                             'Madrid': 323,
                             'Valencia': 473,
                             'Faro': 807,
                             'Sevilla': 703,
                             'Granada': 678},
                  'Barcelona': {'A Coruña': 895,
                                'Bilbao': 468,
                                'Barcelona': 0,
                                'Lisboa': 1005,
                                'Madrid': 504,
                                'Valencia': 303,
                                'Faro': 1003,
                                'Sevilla': 828,
                                'Granada': 681},
                  'Lisboa': {'A Coruña': 522,
                             'Bilbao': 725,
                             'Barcelona': 1005,
                             'Lisboa': 0,
                             'Madrid': 502,
                             'Valencia': 760,
                             'Faro': 189,
                             'Sevilla': 314,
                             'Granada': 513},
                  'Madrid': {'A Coruña': 509,
                             'Bilbao': 323,
                             'Barcelona': 504,
                             'Lisboa': 502,
                             'Madrid': 0,
                             'Valencia': 303,
                             'Faro': 527,
                             'Sevilla': 390,
                             'Granada': 359},
                  'Valencia': {'A Coruña': 797,
                               'Bilbao': 473,
                               'Barcelona': 303,
                               'Lisboa': 760,
                               'Madrid': 303,
                               'Valencia': 0,
                               'Faro': 725,
                               'Sevilla': 540,
                               'Granada': 379},
                  'Faro': {'A Coruña': 708,
                           'Bilbao': 807,
                           'Barcelona': 1003,
                           'Lisboa': 189,
                           'Madrid': 527,
                           'Valencia': 725,
                           'Faro': 0,
                           'Sevilla': 195,
                           'Granada': 404},
                  'Sevilla': {'A Coruña': 696,
                              'Bilbao': 703,
                              'Barcelona': 828,
                              'Lisboa': 314,
                              'Madrid': 390,
                              'Valencia': 540,
                              'Faro': 195,
                              'Sevilla': 0,
                              'Granada': 210},
                  'Granada': {'A Coruña': 799,
                              'Bilbao': 678,
                              'Barcelona': 681,
                              'Lisboa': 513,
                              'Madrid': 359,
                              'Valencia': 379,
                              'Faro': 404,
                              'Sevilla': 210,
                              'Granada': 0}}

    problema_faro_bcn = Problema('Faro', 'Barcelona', viajes, kms, distancias)
    astar = BusquedaAStar(problema_faro_bcn)
    camino = astar.a_estrella()
    print("Camino encontrado:", camino)