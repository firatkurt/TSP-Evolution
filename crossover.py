import random
import individual
from dataOperation import total_distance


def get_crossover(name):
    if name == "PMX":
        return partially_match_crossover
    elif name == "OX":
        return order_crossover
    else:
        raise Exception("There is not exist this crossover. Name:" + name)


def partially_match_crossover(initial_data, ind1, ind2):
    nodes1 = ind1.nodes
    nodes2 = ind2.nodes
    size = min(len(nodes1), len(nodes2))
    cx_point1, cx_point2 = __get_cx_points(size)
    offspring1 = __create_pmx_offspring(nodes1, nodes2, cx_point1, cx_point2, size)
    offspring2 = __create_pmx_offspring(nodes2, nodes1, cx_point1, cx_point2, size)
    return individual.Individual(offspring1, total_distance(initial_data, offspring1)), \
           individual.Individual(offspring2, total_distance(initial_data, offspring2))


def order_crossover(initial_data, ind1, ind2):
    nodes1 = ind1.nodes
    nodes2 = ind2.nodes
    size = min(len(nodes1), len(nodes2))
    cx_point1, cx_point2 = __get_cx_points(size)
    offspring1 = __create_order_offspring(nodes1, nodes2, cx_point1, cx_point2, size)
    offspring2 = __create_order_offspring(nodes2, nodes1, cx_point1, cx_point2, size)
    return individual.Individual(offspring1, total_distance(initial_data, offspring1)), \
           individual.Individual(offspring2, total_distance(initial_data, offspring2))


def __create_order_offspring(ind1, ind2, cx_point1, cx_point2, size):
    offspring = [0] * size
    offspring[cx_point1:cx_point2] = ind1[cx_point1:cx_point2]
    index_ind2 = cx_point2 % size
    index_offspring = cx_point2 % size
    while index_offspring != cx_point1:
        if ind2[index_ind2] not in offspring:
            offspring[index_offspring] = ind2[index_ind2]
            index_offspring = (index_offspring + 1) % size
        index_ind2 = (index_ind2 + 1) % size
    return offspring


def __create_pmx_offspring(ind1, ind2, cx_point1, cx_point2, size):
    offspring1, offspring2 = [0] * size, [0] * size
    offspring1[cx_point1:cx_point2] = ind1[cx_point1:cx_point2]
    offspring2[cx_point1:cx_point2] = ind2[cx_point1:cx_point2]

    not_existing_genes = [offspring2[i] for i in range(cx_point1, cx_point2) if offspring2[i] not in offspring1]
    for i in range(len(not_existing_genes)):
        found = False
        searched_gene_index = ind2.index(not_existing_genes[i])
        while not found:
            value_org = ind1[searched_gene_index]
            if value_org not in offspring2:
                found = True
            searched_gene_index = ind2.index(value_org)
        offspring1[searched_gene_index] = not_existing_genes[i]
    for i in range(len(ind1)):
        if offspring1[i] == 0:
            offspring1[i] = ind2[i]
    return offspring1


def __get_cx_points(size):
    cx_point1 = random.randint(0, size)
    cx_point2 = random.randint(0, size - 1)
    if cx_point2 >= cx_point1:
        cx_point2 += 1
    else:
        cx_point1, cx_point2 = cx_point2, cx_point1
    return cx_point1, cx_point2


if __name__ == '__main__':
    individual1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    individual2 = [9, 3, 7, 8, 2, 6, 5, 1, 4]
    # partialy_match_crossover(individual1, individual2)
    order_crossover(individual1, individual2)
