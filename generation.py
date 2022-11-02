import crossover
import mutation
import twooptoperator
import random
import selection

from dataOperation import create_population


class GenerationResult:
    def __init__(self, strong, weak, avg):
        self.strong = strong
        self.weak = weak
        self.avg = avg

    def __str__(self):
        return "Best result: {0} Average result: {1}".format(self.strong, self.avg)


def generation(initial_data, cx, mt, two_opt=False, k=20, m=1, n=5, generation_count=20000):
    population = create_population(initial_data)
    crossover_method = crossover.get_crossover(cx)
    mutation_method = mutation.get_mutation(mt)
    result = []
    for i in range(1, generation_count+1):
        parent1, parent2 = selection.parent_selection(population, 5)
        offspring1, offspring2 = crossover_method(initial_data, parent1, parent2)
        rand = random.randint(1, 100)
        if rand <= 10:
            offspring1 = mutation_method(initial_data, offspring1)
            offspring2 = mutation_method(initial_data, offspring2)
        if two_opt and i % k == 0:
            twooptoperator.execute(initial_data, population, m, n)
        weak, rand_selected = selection.survival_selection(population)
        population.individuals[weak[0]] = offspring1
        population.individuals[rand_selected[0]] = offspring2
        result.append(GenerationResult(population.strong()[1].distance, population.weak()[1].distance,
                                       population.average()))
    return result
