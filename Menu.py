import random
import package as pkg
import graph as gr
import matplotlib.pyplot as plt

def plot_route(package_stream, route):
    """
    Plot the route on a map.
    """
    # Create a dictionary mapping package IDs to coordinates
    package_coordinates = {package.id: (package.coordinates_x, package.coordinates_y) for package in package_stream}

    # Extract coordinates of packages in the route
    route_coordinates = [package_coordinates[node] for node in route]

    # Extract X and Y coordinates separately
    x = [coord[0] for coord in route_coordinates]
    y = [coord[1] for coord in route_coordinates]

    # Plot the map
    plt.figure(figsize=(8, 8))
    for package_id, (x_coord, y_coord) in package_coordinates.items():
        plt.plot(x_coord, y_coord, 'o', markersize=8, color='blue')  # Plot packages

    # Plot the route
    for i in range(len(route) - 1):
        start_package_coord = package_coordinates[route[i]]
        end_package_coord = package_coordinates[route[i + 1]]
        plt.plot([start_package_coord[0], end_package_coord[0]], [start_package_coord[1], end_package_coord[1]], color='red')  # Plot route segment

    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Route Visualization on Map')
    plt.grid(True)
    plt.show()

def main():

    stream = pkg.generate_package_stream(10, 50)
    graph = gr.generate_graph(stream)
    initial_solution = list(graph.vertices.keys())
    greedy_result = gr.greedy_search(graph)
    initial_solution = greedy_result


    print()
    print("Welcome to another day of work!, choose which algorithm you would like to use to get the best route to deliver the packages.")
    print("Remember, you can choose to see the costs of all the routes to compare, and choose the best one.")
    print("As you know from experience, the best algorithm is not always the same as they depend on the dropoff locations.")
    print()
    stop = False
    while (stop==False):

        print("Please choose an algorithm:")
        print("1. Greedy Search")
        print("2. Hill Climbing")
        print("3. Genetic Algorithm")
        print("4. Tabu Search")
        print("5. Simulated Annealing")
        print("6. Compare all algorithms")
        print("7. Exit")
        print()

        choice = input("Enter your choice: ")

        if choice == '1':
            greedy_result_with_timeDistance = gr.attach_current_distanceAndTime_traveled(graph, greedy_result)
            print("Greedy Result:", greedy_result)
            print()
            print()
            print()
            print("Greedy Result with Time and Distance:", greedy_result_with_timeDistance)
            print()
            print()
            print()
            print("Greedy Result Cost:", gr.evaluation_function(graph, greedy_result, greedy_result_with_timeDistance))
            print()
            print()
            print()
        elif choice == '2':
            hill_climbing_result = gr.hill_Climbing(graph, greedy_result, 10)
            print("Hill Climbing Result:", hill_climbing_result)
            print()
            hill_climbing_result_with_timeDistance = gr.attach_current_distanceAndTime_traveled(graph, hill_climbing_result)
            print("Hill Climbing Result with Time and Distance:", hill_climbing_result_with_timeDistance)
            print()
            print()
            print("Hill Climbing Result Cost:", gr.evaluation_function(graph, hill_climbing_result, hill_climbing_result_with_timeDistance))
            print()
            print()
        
        elif choice == '3':
            genetic_algorithm_result = gr.genetic_algorithm(graph, 10)
            print("Genetic algorithm result:", genetic_algorithm_result)
            print()
            genetic_algorithm_result_with_timeDistance = gr.attach_current_distanceAndTime_traveled(graph, genetic_algorithm_result)
            print("Genetic algorithm result with time and distance:", genetic_algorithm_result_with_timeDistance)
            print()
            print()
            print("Genetic algorithm result cost:", gr.evaluation_function(graph, genetic_algorithm_result, genetic_algorithm_result_with_timeDistance)) 
            print()
            print()
        elif choice == '4':
            tabu_search_result = gr.tabu_search(graph, greedy_result, 10, 10)
            print("Tabu search result:", tabu_search_result)
            tabu_search_result_with_timeDistance = gr.attach_current_distanceAndTime_traveled(graph, tabu_search_result)
            print("Tabu search result with time and distance:", tabu_search_result_with_timeDistance)
            print()
            print()
            print("Tabu Search Result Cost:", gr.evaluation_function(graph, tabu_search_result, tabu_search_result_with_timeDistance))
            print()
            print()
            print() 
        elif choice == '5':
            simmulated_annealing_result = gr.simulated_annealing(graph, 100, 0.01, 100, greedy_result)
            print("Simmulated Annealing Result:", simmulated_annealing_result)
            print()
            simmulated_annealing_result_with_timeDistance = gr.attach_current_distanceAndTime_traveled(graph,simmulated_annealing_result)
            print()
            print("Simmulated Annealing Result with Time and Distance:", simmulated_annealing_result_with_timeDistance)
            print()
            print()
            print("Simmulated Annealing Result Cost:", gr.evaluation_function(graph, simmulated_annealing_result, simmulated_annealing_result_with_timeDistance))
            print()
            print()
            print()
        
        elif choice == '6':
            greedy_result_with_timeDistance = gr.attach_current_distanceAndTime_traveled(graph, greedy_result)
            hill_climbing_result = gr.hill_Climbing(graph, greedy_result, 10)
            hill_climbing_result_with_timeDistance = gr.attach_current_distanceAndTime_traveled(graph, hill_climbing_result)
            genetic_algorithm_result = gr.genetic_algorithm(graph, 10)
            genetic_algorithm_result_with_timeDistance = gr.attach_current_distanceAndTime_traveled(graph, genetic_algorithm_result)
            tabu_search_result = gr.tabu_search(graph, greedy_result, 10, 10)
            tabu_search_result_with_timeDistance = gr.attach_current_distanceAndTime_traveled(graph, tabu_search_result)
            simmulated_annealing_result = gr.simulated_annealing(graph, 100, 0.01, 100, greedy_result)
            simmulated_annealing_result_with_timeDistance = gr.attach_current_distanceAndTime_traveled(graph,simmulated_annealing_result)

            print("Greedy Result:", greedy_result)
            print("Greedy Cost:", gr.evaluation_function(graph, greedy_result, greedy_result_with_timeDistance))
            print()
            print()
            print()
            print("Hill Climbing Result:", hill_climbing_result)
            print("Hill Climbing Cost:", gr.evaluation_function(graph, hill_climbing_result, hill_climbing_result_with_timeDistance))
            print()
            print()
            print()
            print("Genetic algorithm result:", genetic_algorithm_result)
            print("Genetic algorithm cost:", gr.evaluation_function(graph, genetic_algorithm_result, genetic_algorithm_result_with_timeDistance))
            print()
            print()
            print()
            print("Tabu search result:", tabu_search_result)
            print("Tabu search cost:", gr.evaluation_function(graph, tabu_search_result, tabu_search_result_with_timeDistance))
            print()
            print()
            print()
            print("Simmulated Annealing Result:", simmulated_annealing_result)
            print("Simmulated Annealing Cost:", gr.evaluation_function(graph, simmulated_annealing_result, simmulated_annealing_result_with_timeDistance))
            print()
            print()
            print()

            print("1. Greedy Search")
            print("2. Hill Climbing")
            print("3. Genetic Algorithm")
            print("4. Tabu Search")
            print("5. Simulated Annealing")

            choice_to_show = input("So which route are you going to take? Choose a number between 1 and 5: ")
            
            

            if choice_to_show == '1':
                print("Greedy Result:", greedy_result)
                plot_route(stream, greedy_result)
                print()
                continue

            elif choice_to_show == '2':
                print("Hill Climbing Result:", hill_climbing_result)
                plot_route(stream, hill_climbing_result)
                print()
                continue
            elif choice_to_show == '3':
                print("Genetic algorithm result:", genetic_algorithm_result)
                plot_route(stream, genetic_algorithm_result)
                print()
                continue
            elif choice_to_show == '4':
                print("Tabu search result:", tabu_search_result)
                plot_route(stream, tabu_search_result)
                print()
                continue
            elif choice_to_show == '5':
                print("Simmulated Annealing Result:", simmulated_annealing_result)
                plot_route(stream, simmulated_annealing_result)
                print()
                continue
        elif choice == '7':
            stop = True
            print("Goodbye, have a good trip!")
            return
        else:
            print("Invalid choice. Please choose a number between 1 and 7.")
            print()

if __name__ == "__main__":
    main()