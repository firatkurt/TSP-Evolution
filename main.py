import tsplib95
from dataOperation import create_instance, total_distance
import generation

def main():
    initial = tsplib95.load("Documents/kroA100.tsp")
    population = []
    for _ in range(50):
        instance = create_instance(initial, 0)
        population.append(instance)
    gen = generation.Generation(population)
    print(len(population))
    print(gen.strong()[1].distance)
    print(gen.weak()[1].distance)
    print(gen.tournament(5)[1].distance)
    print(gen.rand()[1].distance)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
