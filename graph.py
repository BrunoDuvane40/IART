import random 

from random import sample, random

from math import exp

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


def simmulated_annealing(graph, initial_temperature, cooling_rate, iterations):
    current_solution = list(graph.vertices.keys())
    best_solution = current_solution
    temperature = initial_temperature

    for i in range(iterations):
        new_solution = current_solution.copy()
        new_solution = swap_vertices(new_solution)
        current_cost = cost(graph, current_solution)
        new_cost = cost(graph, new_solution)
        if new_cost < current_cost:
            current_solution = new_solution
            if new_cost < cost(graph, best_solution):
                best_solution = new_solution
        else:
            if acceptance_probability(current_cost, new_cost, temperature) > random():
                current_solution = new_solution
        temperature *= 1 - cooling_rate
    return best_solution

def swap_vertices(solution):
    i, j = sample(range(len(solution)), 2)
    solution[i], solution[j] = solution[j], solution[i]
    return solution

def cost(graph, solution):
    cost = 0
    for i in range(len(solution) - 1):
        vertex1 = graph.vertices[solution[i]]
        vertex2 = graph.vertices[solution[i + 1]]
        for edge in vertex1['edges']:
            if edge['to'] == solution[i + 1]:
                cost += edge['weight']
    return cost

def acceptance_probability(current_cost, new_cost, temperature):
    if new_cost < current_cost:
        return 1.0
    return exp((current_cost - new_cost) / temperature)


