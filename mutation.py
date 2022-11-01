import random
from dataOperation import total_distance


def get_mutation(name):
    if name == "SM":
        return swap_mutation
    elif name == "IM":
        return insertion_mutation
    elif name == "IVM":
        return inversion_mutation
    else:
        raise Exception("There is not exist this mutation. Name:" + name)


def swap_mutation(initial_data, ind):
    size = len(ind.nodes)
    mp1, mp2 = __get_mutation_points(size)
    ind.nodes[mp1], ind.nodes[mp2] = ind.nodes[mp2], ind.nodes[mp1]
    ind.distance = total_distance(initial_data,ind.nodes)
    return ind


def insertion_mutation(initial_data, ind):
    size = len(ind.nodes)
    mp1, mp2 = __get_mutation_points(size)
    temp = ind.nodes[mp2]
    del ind.nodes[mp2]
    ind.nodes.insert(mp1 + 1, temp)
    ind.distance = total_distance(initial_data,ind.nodes)
    return ind


def inversion_mutation(initial_data, ind):
    size = len(ind.nodes)
    mp1, mp2 = __get_mutation_points(size)
    temp = ind.nodes[mp1:mp2 + 1]
    temp = temp[::-1]
    ind.nodes[mp1:mp2 + 1] = temp
    ind.distance = total_distance(initial_data, ind.nodes)
    return ind


def __get_mutation_points(size):
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


if __name__ == '__main__':
    ind = [9, 3, 7, 8, 2, 6, 5, 1, 4]
    # swap_mutation(ind)
    # insertion_mutation(ind)
    inversion_mutation(ind)
