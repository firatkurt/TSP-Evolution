from dataOperation import total_distance, create_instance
import random
import population
from copy import deepcopy
from selection import two_opt_selection

def execute(initial_data, ppl, m=1, n=5):
    offsprings = []
    inds = two_opt_selection(ppl, m)
    for ind in inds:
        for i in range(n):
            offspring = deepcopy(ind[1])
            nodes = offspring.nodes
            size = len(nodes)
            mp1, mp2 = __get_two_opt_points(size)
            temp = nodes[mp1:mp2 + 1]
            temp = temp[::-1]
            nodes[mp1:mp2 + 1] = temp
            offspring.distance = total_distance(initial_data, nodes)
            offsprings.append(offspring)
        strong = min(offsprings, key=lambda x: x.distance)
        if strong.distance < ind[1].distance:
            ppl.individuals[ind[0]] = strong

def __get_two_opt_points(size):
    cx_point1 = random.randint(0, size - 1)
    cx_point2 = random.randint(0, size - 3)

    if cx_point2 == cx_point1 - 1:  # it is applied for guarantying to existing of mutation
        if cx_point2 == 0:
            cx_point1 += 1
        else:
            cx_point2 -= 1
    if cx_point2 >= cx_point1:
        cx_point2 += 2
    else:
        cx_point1, cx_point2 = cx_point2, cx_point1
    return cx_point1, cx_point2
