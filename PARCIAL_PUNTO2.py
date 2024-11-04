import heapq

class Grafo:
    def __init__(self):
        self.adjacencia = {}

    def agregar_personaje(self, personaje):
        if personaje not in self.adjacencia:
            self.adjacencia[personaje] = []

    def agregar_relacion(self, personaje1, personaje2, episodios):
        self.agregar_personaje(personaje1)
        self.agregar_personaje(personaje2)
        self.adjacencia[personaje1].append((personaje2, episodios))
        self.adjacencia[personaje2].append((personaje1, episodios))  

def arbol_expansion_minima(grafo):
    start = next(iter(grafo.adjacencia))  
    visited = set()
    min_heap = [(0, start)]
    arbol = []

    while min_heap:
        costo, personaje = heapq.heappop(min_heap)
        if personaje not in visited:
            visited.add(personaje)
            arbol.append((costo, personaje))
            for vecino, peso in grafo.adjacencia[personaje]:
                if vecino not in visited:
                    heapq.heappush(min_heap, (peso, vecino))
    return arbol[1:] 

def contiene_yoda(grafo):
    arbol = arbol_expansion_minima(grafo)
    personajes_en_arbol = {personaje for _, personaje in arbol}
    return "Yoda" in personajes_en_arbol


def maximo_episodios_compartidos(grafo):
    max_episodios = 0
    personajes_max = ("", "")  
    for personaje, relaciones in grafo.adjacencia.items():
        for vecino, episodios in relaciones:
            if episodios > max_episodios:
                max_episodios = episodios
                personajes_max = (personaje, vecino)
    return max_episodios, personajes_max

def mostrar_personajes(grafo):
    return list(grafo.adjacencia.keys())


grafo = Grafo()

personajes = [
    "Luke Skywalker",
    "Darth Vader",
    "Yoda",
    "Boba Fett",
    "C-3PO",
    "Leia Organa",
    "Rey",
    "Kylo Ren",
    "Chewbacca",
    "Han Solo",
    "R2-D2",
    "BB-8"
]

for personaje in personajes:
    grafo.agregar_personaje(personaje)

grafo.agregar_relacion("Luke Skywalker", "Darth Vader", 5)  
grafo.agregar_relacion("Leia Organa", "Han Solo", 4)
grafo.agregar_relacion("Yoda", "Darth Vader", 3)
grafo.agregar_relacion("Rey", "Kylo Ren", 4)
grafo.agregar_relacion("Han Solo", "Chewbacca", 6)
grafo.agregar_relacion("C-3PO", "R2-D2", 7)
grafo.agregar_relacion("BB-8", "Rey", 2)
grafo.agregar_relacion("Boba Fett", "Han Solo", 3)

# A: cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
# B: hallar el árbol de expansión minino y determinar si contiene a Yoda;
arbol = arbol_expansion_minima(grafo)
print("Árbol de expansión mínima:", arbol)

print("Contiene a Yoda:", contiene_yoda(grafo))

# C: Máximo de episodios compartidos entre dos personajes
def maximo_episodios_compartidos(grafo):
    max_episodios = 0
    personajes_max = ("", "")  # Para almacenar los personajes con el máximo
    for personaje, relaciones in grafo.adjacencia.items():
        for vecino, episodios in relaciones:
            if episodios > max_episodios:
                max_episodios = episodios
                personajes_max = (personaje, vecino)  # Guarda los nombres de los personajes
    return max_episodios, personajes_max

# D: Mostrar todos los personajes en el grafo
print("Personajes en el grafo:", mostrar_personajes(grafo))
