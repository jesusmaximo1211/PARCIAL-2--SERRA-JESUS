class Pokemon:
    def __init__(self, nombre, numero, tipos):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos

    def __str__(self):
        tipos_str = ", ".join(self.tipos)
        return f"Nombre: {self.nombre}, Número: {self.numero}, Tipos: {tipos_str}"


class BSTNode:
    def __init__(self, key, value, other_value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.other_value = other_value 

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value, other_value=None):
        self.root = self._insert_recursive(self.root, key, value, other_value)

    def _insert_recursive(self, node, key, value, other_value=None):
        if not node:
            return BSTNode(key, value, other_value)
        elif key < node.key:
            node.left = self._insert_recursive(node.left, key, value, other_value)
        else:
            node.right = self._insert_recursive(node.right, key, value, other_value)
        return node

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if not node or node.key == key:
            return node
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)


nombre_tree = BinarySearchTree()
numero_tree = BinarySearchTree()
tipo_tree = BinarySearchTree()

pokemones = [
    Pokemon("Bulbasaur", 1, ["planta", "veneno"]),
    Pokemon("Ivysaur", 2, ["planta", "veneno"]),
    Pokemon("Venusaur", 3, ["planta", "veneno"]),
    Pokemon("Charmander", 4, ["fuego"]),
    Pokemon("Charmeleon", 5, ["fuego"]),
    Pokemon("Charizard", 6, ["fuego", "volador"]),
    Pokemon("Squirtle", 7, ["agua"]),
    Pokemon("Wartortle", 8, ["agua"]),
    Pokemon("Blastoise", 9, ["agua"]),
    Pokemon("Pikachu", 25, ["eléctrico"]),
    Pokemon("Raichu", 26, ["eléctrico"]),
    Pokemon("Jolteon", 135, ["eléctrico"]),
    Pokemon("Flareon", 136, ["fuego"]),
    Pokemon("Vaporeon", 134, ["agua"]),
    Pokemon("Espeon", 196, ["psíquico"]),
    Pokemon("Umbreon", 197, ["siniestro"]),
    Pokemon("Leafeon", 470, ["planta"]),
    Pokemon("Glaceon", 471, ["hielo"]),
    Pokemon("Sylveon", 700, ["hada"]),
    Pokemon("Eevee", 133, ["normal"]),
    Pokemon("Mewtwo", 150, ["psíquico"]),
    Pokemon("Mew", 151, ["psíquico"]),
    Pokemon("Lugia", 249, ["psíquico", "volador"]),
    Pokemon("Ho-oh", 250, ["fuego", "volador"]),
    Pokemon("Rayquaza", 384, ["dragón", "volador"]),
    Pokemon("Dialga", 483, ["acero", "dragón"]),
    Pokemon("Palkia", 484, ["agua", "dragón"]),
    Pokemon("Giratina", 487, ["fantasma", "dragón"]),
    Pokemon("Arceus", 493, ["normal"]),
    Pokemon("Zekrom", 644, ["dragón", "eléctrico"]),
    Pokemon("Reshiram", 643, ["dragón", "fuego"]),
    Pokemon("Kyogre", 382, ["agua"]),
    Pokemon("Groudon", 383, ["tierra"]),
    Pokemon("Tyrantrum", 697, ["roca", "dragón"]),
    Pokemon("Lycanroc", 745, ["roca"]),
    Pokemon("Incineroar", 727, ["fuego", "siniestro"]),
    Pokemon("Primarina", 730, ["agua", "hada"]),
    Pokemon("Decidueye", 724, ["planta", "fantasma"]),
    Pokemon("Zacian", 888, ["hada"]),
    Pokemon("Zamazenta", 889, ["lucha", "acero"]),
    Pokemon("Eternatus", 890, ["veneno", "dragón"])
]

# a)
for poke in pokemones:
    nombre_tree.insert(poke.nombre, poke)
    numero_tree.insert(poke.numero, poke)
    for tipo in poke.tipos:
        tipo_tree.insert(tipo, poke)

# b) Buscar Pokémon por proximidad en el nombre
def buscar_pokemon_por_numero(tree, numero):
    nodo = tree.search(numero)
    if nodo:
        print(nodo.value)
    else:
        print(f"No se encontró Pokémon con número: {numero}")

def buscar_pokemon_por_nombre_proximidad(tree, subcadena):
    def buscar_recursivo(node, subcadena):
        if node:
            if subcadena.lower() in node.value.nombre.lower():
                print(node.value)
            buscar_recursivo(node.left, subcadena)
            buscar_recursivo(node.right, subcadena)

    print(f"Buscando Pokémon con nombres que contengan '{subcadena}':")
    buscar_recursivo(tree.root, subcadena)

numero_a_buscar = 1 
buscar_pokemon_por_numero(numero_tree, numero_a_buscar)
subcadena_a_buscar = "bul" 
buscar_pokemon_por_nombre_proximidad(nombre_tree, subcadena_a_buscar)

# c) Mostrar todos los nombres de Pokémon de un determinado tipo
def mostrar_pokemons_por_tipo(tree, tipo):
    def buscar_por_tipo(node, tipo):
        if node:
            if tipo in node.value.tipos:
                print(node.value.nombre)
            buscar_por_tipo(node.left, tipo)
            buscar_por_tipo(node.right, tipo)

    print(f"Pokémon de tipo {tipo}:")
    buscar_por_tipo(tree.root, tipo)

tipos_a_buscar = ["agua", "fuego", "planta", "eléctrico"]
for tipo in tipos_a_buscar:
    mostrar_pokemons_por_tipo(tipo_tree, tipo)

# d) Listado en orden ascendente por número y nombre
def inorden(node):
    if node:
        inorden(node.left)
        print(node.value)  
        inorden(node.right)

def inorden_por_nombre(node):
    if node:
        inorden_por_nombre(node.left)
        print(node.value) 
        inorden_por_nombre(node.right)

from collections import deque

def recorrer_por_nivel(root):
    if not root:
        return

    queue = deque([root])
    while queue:
        current = queue.popleft()
        print(current.value.nombre) 
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

print("Listado en orden ascendente por número:")
inorden(numero_tree.root)

print("\nListado en orden ascendente por nombre:")
inorden_por_nombre(nombre_tree.root)

print("\nListado por nivel por nombre:")
recorrer_por_nivel(nombre_tree.root)

# e) Mostrar todos los datos de Pokémon específicos
def mostrar_datos_pokemons_especificos(tree, nombres):
    for nombre in nombres:
        nodo_pokemon = tree.search(nombre)
        if nodo_pokemon:
            print(nodo_pokemon.value)
        else:
            print(f"No se encontró Pokémon con nombre: {nombre}")

pokemones_a_mostrar = ["Jolteon", "Lycanroc", "Tyrantrum"]
print("Datos de Jolteon, Lycanroc y Tyrantrum:")
mostrar_datos_pokemons_especificos(nombre_tree, pokemones_a_mostrar)

# f) Contar cuántos Pokémon hay de tipo eléctrico y acero
def contar_pokemons_por_tipo(tree, tipo):
    count = 0
    
    def contar_recursivo(node, tipo):
        nonlocal count
        if node:
            if tipo in node.value.tipos:
                count += 1
            contar_recursivo(node.left, tipo)
            contar_recursivo(node.right, tipo)

    contar_recursivo(tree.root, tipo)
    return count

cantidad_electricos = contar_pokemons_por_tipo(tipo_tree, "eléctrico")
cantidad_acero = contar_pokemons_por_tipo(tipo_tree, "acero")

print(f"Cantidad de Pokémon de tipo eléctrico: {cantidad_electricos}")
print(f"Cantidad de Pokémon de tipo acero: {cantidad_acero}")
