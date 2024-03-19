import package as pkg
import graph as gr

stream = pkg.generate_package_stream(10, 100)
graph = gr.generate_graph(stream)

for vertex_id, vertex_data in graph.vertices.items():
    print("Vertex ID:", vertex_id)
    print("Package Type:", vertex_data['type'])
    print("Edges:", vertex_data['edges'])
    print()


