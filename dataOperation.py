import random
import sys
import individual
import population


def total_distance(data, nodes):
    distance = 0
    for i in range(len(nodes) - 1):
        distance += data.get_weight(nodes[i], nodes[i + 1])
    distance += data.get_weight(nodes[-1], nodes[0])
    return distance


def create_instance(initial, rand_rate=0.8):
    nodes = []
    for i in initial.get_nodes():
        nodes.append(i)
    random.seed()
    random.shuffle(nodes)
    shuffled_nodes = nodes[0:int(len(nodes) * rand_rate)]
    if len(shuffled_nodes) == 0:
        shuffled_nodes.append(nodes[0])

    while len(shuffled_nodes) != len(nodes):
        selected_node = random.sample(shuffled_nodes, 1)[0]
        min_index = None
        min_dist = sys.maxsize
        for i in range(len(nodes)):
            if nodes[i] in shuffled_nodes or selected_node == nodes[i]:
                continue
            current_dist = initial.get_weight(selected_node, nodes[i])
            if current_dist < min_dist:
                min_index = i
                min_dist = current_dist
        if min_index is None:
            raise Exception("Something went wrong")
        shuffled_nodes.append(nodes[min_index])
    result = individual.Individual(shuffled_nodes, total_distance(initial, shuffled_nodes))
    return result


def create_population(initial_data, individual_count=50):
    individuals = []
    for _ in range(individual_count):
        instance = create_instance(initial_data)
        individuals.append(instance)
    return population.Population(individuals)
