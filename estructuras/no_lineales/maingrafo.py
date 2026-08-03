from estructuras.no_lineales.graph import Graph

def test_graph():
    graph = Graph()
    graph.agregar_vertice("A")
    graph.agregar_vertice("B")
    graph.agregar_vertice("C")
    graph.agregar_vertice("D")
    
    graph.agregar_arco("A", "B")
    graph.agregar_arco("A", "C")
    graph.agregar_arco("B", "D")
    
    print("Vértices:")
    print(graph.obtener_vertices())
    
    print("\nLista de adyacencia:")
    for vertex in graph.obtener_vertices():
        adjacent_vertices = graph.adj_list.get(vertex, set())
        adjacent_text = ", ".join(sorted(list(adjacent_vertices))) if adjacent_vertices else "Sin conexiones"
        print(f"{vertex}: {adjacent_text}")
        
    print("\nMatriz de adyacencia:")
    vertices, matrix = graph.obtener_matriz_adyacencia()
    print("  " + " ".join(vertices))
    for index, row in enumerate(matrix):
        values = " ".join(str(value) for value in row)
        print(f"{vertices[index]} {values}")
        
    print("\nLista de arcos:")
    for vertex1, vertex2 in graph.obtener_arcos():
        print(f"({vertex1}, {vertex2})")

if __name__ == "__main__":
    test_graph()