def sacar_siguiente(frontera, metrica='valor', criterio='menor',
                    objetivos=None):
    """Devuelve el siguiente nodo de la frontera según un criterio."""
    if not frontera:
        return None
    mejor = frontera[0]
    for nodo in frontera[1:]:
        for objetivo in objetivos:
            if metrica == 'valor':
                valor_nodo = nodo.valores[objetivo.nombre]
                valor_mejor = mejor.valores[objetivo.nombre]
                if(criterio == 'menor' and
                   valor_nodo < valor_mejor):
                    mejor = nodo
                elif(criterio == 'mayor' and
                     valor_nodo > valor_mejor):
                    mejor = nodo
            elif metrica == 'heuristica':
                heuristica_nodo = nodo.heuristicas[objetivo.nombre]
                heuristica_mejor = mejor.heuristicas[objetivo.nombre]
                if(criterio == 'menor' and
                   heuristica_nodo < heuristica_mejor):
                    mejor = nodo
                elif(criterio == 'mayor' and
                     heuristica_nodo > heuristica_mejor):
                    mejor = nodo
            elif metrica == 'coste':
                if(criterio == 'menor' and
                   nodo.coste_camino < mejor.coste_camino):
                    mejor = nodo
                elif(criterio == 'mayor' and
                     nodo.coste_camino > mejor.coste_camino):
                    mejor = nodo
    frontera.remove(mejor)
    return mejor