import tsplib95
from dataOperation import create_instance, total_distance
import population
import Experimental.crossovermutationtypeevalutation as comte


def main():
    initial = tsplib95.load("Documents/kroA100.tsp")
    cxs = ["PMX", "OX"]
    mts = ["SM", "IM", "IVM"]
    results = comte.evaluate_all(initial, cxs, mts, iteration_count=100, generation_count=20000)
    individuals = []
    for _ in range(50):
        instance = create_instance(initial, 0)
        individuals.append(instance)
    gen = population.Population(individuals)
    print(len(individuals))
    print(gen.strong()[1].distance)
    print(gen.weak()[1].distance)
    print(gen.tournament(5)[1].distance)
    print(gen.rand()[1].distance)

if __name__ == '__main__':
    main()

