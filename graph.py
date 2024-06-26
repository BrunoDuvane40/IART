import time 
import random

from math import exp

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex['id'] not in self.vertices:
            if vertex['type'] == 'urgent':
                self.vertices[vertex['id']] = {'type': vertex['type'], 'delivery_time': vertex['delivery_time'], 'edges': []}
            elif vertex['type'] == 'fragile':
                self.vertices[vertex['id']] = {'type': vertex['type'], 'breaking_chance': vertex['breaking_chance'], 'breaking_cost': vertex['breaking_cost'], 'edges': []}
            else:
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
        if(package.package_type == 'urgent'):
            vertex_info = {'id': package.id, 'type': package.package_type, 'delivery_time': package.delivery_time}
            graph.add_vertex(vertex_info)
        
        elif(package.package_type == 'fragile'):
            vertex_info = {'id': package.id, 'type': package.package_type, 'breaking_chance': package.breaking_chance, 'breaking_cost': package.breaking_cost}
            graph.add_vertex(vertex_info)

        else:
            vertex_info = {'id': package.id, 'type': package.package_type}  
            graph.add_vertex(vertex_info)

    for i, package1 in enumerate(package_stream):
        for j, package2 in enumerate(package_stream):
            if i < j:
                distance = distance_between_packages(package1, package2)
                graph.add_edge(package1.id, package2.id, distance)

    return graph


def simulated_annealing(graph, initial_temperature, cooling_rate, iterations, initial_solution):

    time_1 = time.time()   

    current_solution = initial_solution
    best_solution = current_solution
    temperature = initial_temperature
    

    for i in range(iterations):
        new_solution = current_solution.copy()
        new_solution = perturb_solution(new_solution)  
        current_cost = evaluation_function(graph, current_solution, attach_current_distanceAndTime_traveled(graph, current_solution))
        new_cost = evaluation_function(graph, new_solution, attach_current_distanceAndTime_traveled(graph, new_solution))
        
        if(temperature != 0):
            if new_cost < current_cost or random.random() < exp((current_cost - new_cost) / temperature):
                current_solution = new_solution
                if new_cost < evaluation_function(graph, current_solution, attach_current_distanceAndTime_traveled(graph, current_solution)):
                    best_solution = new_solution

            temperature *= cooling_rate  
        
    best_solution = [node for node in best_solution if node != 0]
    

    best_solution.insert(0, 0)

    time_2 = time.time()

    print("Simulated Annealing Finished in ", time_2 - time_1, " seconds")

    return best_solution


def perturb_solution(solution):
    i, j = random.sample(range(len(solution)), 2)
    solution[i], solution[j] = solution[j], solution[i]
    return solution

def swap_vertices(solution):
    i, j = random.sample(range(len(solution)), 2)
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


def hill_Climbing(graph, initial_solution, iterations):

    time_1 = time.time()
    
    current_solution = initial_solution

    best_solution = current_solution

    for j in best_solution:
        if (j==0):
            best_solution.remove(j)
    
    best_solution.insert(0,0)

    print("Starting Hill Climbing with initial solution:", best_solution)
    print("Initial Solution Cost:", evaluation_function(graph, best_solution, attach_current_distanceAndTime_traveled(graph, best_solution)))
    print()
    print()


    best_solution_cost = evaluation_function(graph, best_solution, attach_current_distanceAndTime_traveled(graph, best_solution))

    for i in range(iterations):
        neighbours = generate_neighbours(best_solution)
        found_better_neighbour = False
        
        for neighbour in neighbours:

            for j in neighbour:
                if (j==0):
                    neighbour.remove(j)
            
            neighbour.insert(0,0)

            neighbour_cost = evaluation_function(graph, neighbour, attach_current_distanceAndTime_traveled(graph, neighbour))

            """
            print("Neighbour Cost:", neighbour_cost)
            print("Neighbour Solution:", neighbour)
            print()
            print()
            print("Best Solution Cost:", best_solution_cost)
            print("Best Solution:", best_solution)
            print()
            print()
            """

            if neighbour_cost < best_solution_cost:
                best_solution = neighbour

                """
                print("Best Solution Updated")
                print("New Best Solution:", best_solution)
                print()
                print()
                """

                best_solution_cost = neighbour_cost
                found_better_neighbour = True
                break

        if not found_better_neighbour:
            break

    time_2 = time.time()

    print("Hill Climbing Finished in ", time_2 - time_1, " seconds")

    return best_solution

def generate_neighbours(solution, num_neighbours=10):



    #print("Current Solution is" ,solution)
    
    neighbours = []
    count = 0

    for i in range(len(solution)):
        if count >= num_neighbours:
            break
        for j in range(i+1, len(solution)):
            neighbour = solution.copy()
            neighbour[i], neighbour[j] = neighbour[j], neighbour[i]
            neighbours.append(neighbour)
            count += 1
            if count >= num_neighbours:
                break

    return neighbours

def attach_current_distanceAndTime_traveled(graph,result):
    result_with_current_distance_traveled = []

    for i in range(len(result)):
        if i == 0:
            result_with_current_distance_traveled.append((result[i], 0))
        else:
            result_with_current_distance_traveled.append((result[i], cost(graph, result[:i+1]), calculate_time(cost(graph, result[:i+1]))))

    return result_with_current_distance_traveled

def calculate_time(distance):
    return (distance / 60) * 60 #Na verdade esta função é desnecessária, pois a distância por si só já é o tempo em minutos uma vez que a velocidade é 60 km/h e 1Km = 1 minuto
    # Deixemos assim no entanto, para deixar o código mais claro

def evaluation_function(graph, result, result_with_current_distanceAndTime_traveled):

    total_delay_minutes = 0 

    for i in range (1, len(result_with_current_distanceAndTime_traveled)):
        if graph.vertices[result_with_current_distanceAndTime_traveled[i][0]]['type'] == 'urgent':
            if(result_with_current_distanceAndTime_traveled[i][2] <= graph.vertices[result_with_current_distanceAndTime_traveled[i][0]]['delivery_time']):
                total_delay_minutes += 0
            else:
                total_delay_minutes += result_with_current_distanceAndTime_traveled[i][2] - graph.vertices[result_with_current_distanceAndTime_traveled[i][0]]['delivery_time']

    """
    print("Total Delay Minutes:", total_delay_minutes)
    print()
    print()

    print("Total Delay Cost:", total_delay_minutes * 0.3)
    print()
    print()
    """

    broken_packages = 0
    broken_packages_additional_cost = 0

    for i in range(1, len(result_with_current_distanceAndTime_traveled)):
        if graph.vertices[result_with_current_distanceAndTime_traveled[i][0]]['type'] == 'fragile':
            distance_covered = result_with_current_distanceAndTime_traveled[i][1]
            chance_of_damage = graph.vertices[result_with_current_distanceAndTime_traveled[i][0]]['breaking_chance']
            p_damage = 1 - ((1 - chance_of_damage) ** distance_covered)
            """
            print("Probability of Damage:", p_damage)
            print()
            print()
            """
            if (random.uniform(0, 1) < p_damage):
                broken_packages += 1
                broken_packages_additional_cost += graph.vertices[result_with_current_distanceAndTime_traveled[i][0]]['breaking_cost']

    """

    print("Broken Packages:", broken_packages)
    print()
    print()

    print("Broken Packages Additional Cost:", broken_packages_additional_cost)
    print()
    print()

    """

    return cost(graph, result) * 0.3 + (total_delay_minutes * 0.3) + broken_packages_additional_cost


def genetic_algorithm(graph, iterations):

    print()
    print("Which heuristic would you like to use?")
    print("1 - Crossover OX")
    print("2 - Crossover PMX")
    print()
    print("Please enter the number of the heuristic you would like to use:")

    heuristic = int(input())

    print()
    print()

    def generate_random_solution():
        vertices = list(graph.vertices.keys())
        random.shuffle(vertices)
        return vertices
    
    def crossover(parent1, parent2):

        size_to_extract = len(parent1) // 2

        child = parent1[:size_to_extract]

        remaining_vertices = set(parent2)-set(child)
        for vertex in parent2:
            if vertex in remaining_vertices:
                child.append(vertex)
                remaining_vertices.remove(vertex)

        return child
    
    def pmx(parent1, parent2):
        start_index = random.randint(0, len(parent1)-2)
        end_index = random.randint(start_index+1, len(parent1)-1)

        child = [None] * len(parent1)
    
        child[start_index:end_index + 1] = parent1[start_index:end_index + 1]

        for i in range(start_index, end_index + 1):
            if parent2[i] not in child:
                current_index = i
                while parent2[current_index] not in child[start_index:end_index + 1]:
                    current_index = parent1.index(parent2[current_index])
                child[current_index] = parent2[i]
    
        for i in range(len(child)):
            if child[i] is None:
                child[i] = parent2[i]

        return child
 

    if heuristic == 1:
        crossover_function = crossover
    else:
        crossover_function = pmx

    print()
    print("For the genetic algorithm, what population size would you like to use for each generation?")
    print()

    

    population_size = int(input())

    time_1 = time.time()

    population = [generate_random_solution() for _ in range(population_size)]

    for _ in range(iterations):
        
        parent1, parent2 = random.sample(population, 2)

        child = crossover_function(parent1, parent2)
  
        child_cost = evaluation_function(graph, child, attach_current_distanceAndTime_traveled(graph, child))

        worst_index = 0
        for i, solution in enumerate(population):
            curr_cost = evaluation_function(graph, solution, attach_current_distanceAndTime_traveled(graph, solution))
            if curr_cost > evaluation_function(graph, population[worst_index], attach_current_distanceAndTime_traveled(graph, population[worst_index])):
                worst_index = i

        worst_cost = evaluation_function(graph, population[worst_index], attach_current_distanceAndTime_traveled(graph, population[worst_index]))
        
        if child_cost < worst_cost:
            population[worst_index] = child

    best_solution = min(population, key=lambda solution: evaluation_function(graph, solution, attach_current_distanceAndTime_traveled(graph, solution)))

    for j in best_solution:
        if (j==0):
            best_solution.remove(j)
    
    best_solution.insert(0,0)

    time_2 = time.time()

    print("Genetic Algorithm Finished in ", time_2 - time_1, " seconds")

    return best_solution


def tabu_search(graph, initial_solution, tabu_size, max_iterations):

    time_1 = time.time()

    current_solution = initial_solution.copy()
    best_solution = current_solution.copy()
    tabu_list = []
    iteration = 0
    no_improvement_count = 0  

    while iteration < max_iterations and no_improvement_count < 50:
        neighborhood = generate_neighbours(current_solution)
        best_neighbor = None
        best_neighbor_cost = float('inf')

        for neighbor in neighborhood:
            if neighbor not in tabu_list:
                neighbor_cost = evaluation_function(graph, neighbor, attach_current_distanceAndTime_traveled(graph, neighbor))
                if neighbor_cost < best_neighbor_cost:
                    best_neighbor = neighbor
                    best_neighbor_cost = neighbor_cost

        if best_neighbor is None:
            break

        current_solution = best_neighbor
        if best_neighbor_cost < evaluation_function(graph, current_solution, attach_current_distanceAndTime_traveled(graph, current_solution)):
            best_solution = best_neighbor
            no_improvement_count = 0
        else:
            no_improvement_count += 1

        tabu_list.append(best_neighbor)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

        iteration += 1

    for j in best_solution:
        if (j == 0):
            best_solution.remove(j)

    best_solution.insert(0, 0)

    time_2 = time.time()

    print("Tabu Search Finished in ", time_2 - time_1, " seconds")

    return best_solution

def greedy_search(graph):
    time_1 = time.time()

    current_vertex = 0  # Start with the start vertex
    current_solution = [current_vertex]  
    best_solution = current_solution.copy()
    best_cost = evaluation_function(graph, best_solution, attach_current_distanceAndTime_traveled(graph, best_solution))

    visited = [False] * len(graph.vertices.keys())
    visited[current_vertex] = True  # Mark the start vertex as visited

    
    while len(current_solution) < len(graph.vertices.keys()):
        min_cost = float('inf')
        best_vertex = -1

        for neighbor in graph.vertices.keys():
            vertex_id = neighbor
            if not visited[vertex_id]:

                current_solution.append(vertex_id)
                current_cost = evaluation_function(graph, current_solution, attach_current_distanceAndTime_traveled(graph, current_solution))
                current_solution.pop()

                if current_cost < min_cost:
                    min_cost = current_cost
                    best_vertex = vertex_id

        if best_vertex == -1:
            break

        visited[best_vertex] = True
        current_vertex = best_vertex
        current_solution.append(best_vertex)

        if min_cost < best_cost:
            best_solution = current_solution.copy()
            best_cost = min_cost
        
        best_solution = current_solution.copy()
    
    time_2 = time.time()

    print("Greedy Search Finished in ", time_2 - time_1, " seconds")

    return best_solution