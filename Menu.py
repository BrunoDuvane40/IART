import random
import package as pkg
import graph as gr

stream = pkg.generate_package_stream(20, 50)

graph = gr.generate_graph(stream)

print("Graph:")
for vertex_id, vertex_data in graph.vertices.items():
    print("Vertex ID:", vertex_id)
    print("PAckage Data", vertex_data)
    print()

result = gr.simmulated_annealing(graph, 100, 0.01, 1000)

for i in result: 
    if (i == 0):
        result.remove(i)

result.insert(0, 0)

def calculate_time(distance):
    return (distance / 60) * 60 #Na verdade esta função é desnecessária, pois a distância por si só já é o tempo em minutos uma vez que a velocidade é 60 km/h e 1Km = 1 minuto
    # Deixemos assim no entanto, para deixar o código mais claro

def attach_current_distanceAndTime_traveled(result):
    result_with_current_distance_traveled = []

    for i in range(len(result)):
        if i == 0:
            result_with_current_distance_traveled.append((result[i], 0))
        else:
            result_with_current_distance_traveled.append((result[i], gr.cost(graph, result[:i+1]), calculate_time(gr.cost(graph, result[:i+1]))))

    return result_with_current_distance_traveled


result_with_current_distanceAndTime_traveled = attach_current_distanceAndTime_traveled(result)

print("Result:")

for vertex in result_with_current_distanceAndTime_traveled:
    print(vertex)

print()
print()

def evaluation_function(graph, result, result_with_current_distanceAndTime_traveled):

    total_delay_minutes = 0 

    for i in range (1, len(result_with_current_distanceAndTime_traveled)):
        if graph.vertices[result_with_current_distanceAndTime_traveled[i][0]]['type'] == 'urgent':
            if(result_with_current_distanceAndTime_traveled[i][2] <= graph.vertices[result_with_current_distanceAndTime_traveled[i][0]]['delivery_time']):
                total_delay_minutes += 0
            else:
                total_delay_minutes += result_with_current_distanceAndTime_traveled[i][2] - graph.vertices[result_with_current_distanceAndTime_traveled[i][0]]['delivery_time']

    print("Total Delay Minutes:", total_delay_minutes)
    print()
    print()

    print("Total Delay Cost:", total_delay_minutes * 0.3)
    print()
    print()

    broken_packages = 0
    broken_packages_additional_cost = 0

    for i in range(1, len(result_with_current_distanceAndTime_traveled)):
        if graph.vertices[result_with_current_distanceAndTime_traveled[i][0]]['type'] == 'fragile':
            distance_covered = result_with_current_distanceAndTime_traveled[i][1]
            chance_of_damage = graph.vertices[result_with_current_distanceAndTime_traveled[i][0]]['breaking_chance']
            p_damage = 1 - ((1 - chance_of_damage) ** distance_covered)
            print("Probability of Damage:", p_damage)
            print()
            print()
            if (random.uniform(0, 1) < p_damage):
                broken_packages += 1
                broken_packages_additional_cost += graph.vertices[result_with_current_distanceAndTime_traveled[i][0]]['breaking_cost']

    print("Broken Packages:", broken_packages)
    print()
    print()

    print("Broken Packages Additional Cost:", broken_packages_additional_cost)
    print()
    print()

    return gr.cost(graph, result) * 0.3 + (total_delay_minutes * 0.3) + broken_packages_additional_cost

print("Evaluation Function:", evaluation_function(graph, result, result_with_current_distanceAndTime_traveled))
