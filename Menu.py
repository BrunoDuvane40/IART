import random
import package as pkg
import graph as gr

stream = pkg.generate_package_stream(10, 50)

graph = gr.generate_graph(stream)

initial_solution = list(graph.vertices.keys())

print("Graph:")
for vertex_id, vertex_data in graph.vertices.items():
    print("Vertex ID:", vertex_id)
    print("PAckage Data", vertex_data)
    print()

simmulated_annealing_result = gr.simmulated_annealing(graph, 100, 0.01, 1000)

hill_climbing_result = gr.hill_Climbing(graph, initial_solution, 10)

genetic_algorithm_result = gr.genetic_algorithm(graph, 100, 2)

print("Simmulated Annealing Result:", simmulated_annealing_result)
print()
print("Hill Climbing Result:", hill_climbing_result)

simmulated_annealing_result_with_timeDistance = gr.attach_current_distanceAndTime_traveled(graph,simmulated_annealing_result)

hill_climbing_result_with_timeDistance = gr.attach_current_distanceAndTime_traveled(graph, hill_climbing_result)

genetic_algorithm_result_with_timeDistance = gr.attach_current_distanceAndTime_traveled(graph, genetic_algorithm_result)

print("Simmulated Annealing Result with Time and Distance:", simmulated_annealing_result_with_timeDistance)
print()
print()

print("Hill Climbing Result with Time and Distance:", hill_climbing_result_with_timeDistance)
print()
print()

print("Genetic algorithm result:", genetic_algorithm_result)
print()
print()

print("Genetic algorithm result with time and distance:", genetic_algorithm_result_with_timeDistance)
print()
print()

print("Genetic algorithm result cost:", gr.evaluation_function(graph, genetic_algorithm_result, genetic_algorithm_result_with_timeDistance)) 
print()
print()

print("Simmulated Annealing Result Cost:", gr.evaluation_function(graph, simmulated_annealing_result, simmulated_annealing_result_with_timeDistance))
print()
print()

print("Hill Climbing Result Cost:", gr.evaluation_function(graph, hill_climbing_result, hill_climbing_result_with_timeDistance))
print()
print()

