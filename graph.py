class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex['id'] not in self.vertices:
            self.vertices[vertex['id']] = {'type': vertex['type'], 'edges': []}  
    
    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1]['edges'].append({'to': vertex2, 'weight': weight})
            self.vertices[vertex2]['edges'].append({'to': vertex1, 'weight': weight})


def distance_between_packages(package1, package2):
    return ((package1.coordinates_x - package2.coordinates_x)**2 + (package1.coordinates_y - package2.coordinates_y)**2)**0.5

def generate_graph(package_stream):
    graph = Graph()

    for package in package_stream:
        vertex_info = {'id': package.id, 'type': package.package_type}  
        graph.add_vertex(vertex_info)

    for i, package1 in enumerate(package_stream):
        for j, package2 in enumerate(package_stream):
            if i < j:
                distance = distance_between_packages(package1, package2)
                graph.add_edge(package1.id, package2.id, distance)

    return graph


