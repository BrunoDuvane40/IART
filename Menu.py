import random
import package as pkg
import graph as gr

stream = pkg.generate_package_stream(10, 50)

graph = gr.generate_graph(stream)

initial_solution = list(graph.vertices.keys())

greedy_result = gr.greedy_search(graph, initial_solution)

initial_solution = greedy_result

simmulated_annealing_result = gr.simulated_annealing(graph, 100, 0.01, 100)

hill_climbing_result = gr.hill_Climbing(graph, initial_solution, 10)

genetic_algorithm_result = gr.genetic_algorithm(graph, 10)

tabu_search_result = gr.tabu_search(graph, initial_solution, 10, 10)

print("Simmulated Annealing Result:", simmulated_annealing_result)
print()
print("Hill Climbing Result:", hill_climbing_result)
print()
print("Genetic algorithm result:", genetic_algorithm_result)
print()
print("Tabu search result:", tabu_search_result)

simmulated_annealing_result_with_timeDistance = gr.attach_current_distanceAndTime_traveled(graph,simmulated_annealing_result)

hill_climbing_result_with_timeDistance = gr.attach_current_distanceAndTime_traveled(graph, hill_climbing_result)

genetic_algorithm_result_with_timeDistance = gr.attach_current_distanceAndTime_traveled(graph, genetic_algorithm_result)

tabu_search_result_with_timeDistance = gr.attach_current_distanceAndTime_traveled(graph, tabu_search_result)

print()
print("Simmulated Annealing Result with Time and Distance:", simmulated_annealing_result_with_timeDistance)
print()
print()
print("Hill Climbing Result with Time and Distance:", hill_climbing_result_with_timeDistance)
print()
print()
print("Genetic algorithm result with time and distance:", genetic_algorithm_result_with_timeDistance)
print()
print()
print("Tabu search result with time and distance:", tabu_search_result_with_timeDistance)
print()
print()
print()
greedy_result_with_timeDistance = gr.attach_current_distanceAndTime_traveled(graph, greedy_result)
print("Greedy Result with Time and Distance:", greedy_result_with_timeDistance)
print()
print()
print()
print("Genetic algorithm result cost:", gr.evaluation_function(graph, genetic_algorithm_result, genetic_algorithm_result_with_timeDistance)) 
print()
print()
print()
print("Simmulated Annealing Result Cost:", gr.evaluation_function(graph, simmulated_annealing_result, simmulated_annealing_result_with_timeDistance))
print()
print()
print()
print("Hill Climbing Result Cost:", gr.evaluation_function(graph, hill_climbing_result, hill_climbing_result_with_timeDistance))
print()
print()
print()
print("Tabu Search Result Cost:", gr.evaluation_function(graph, tabu_search_result, tabu_search_result_with_timeDistance))
print()
print()
print()
print("Greedy Result:", greedy_result)
print()
print()
print()
print("Greedy Result Cost:", gr.evaluation_function(graph, greedy_result, greedy_result_with_timeDistance))
print()
print()
print()