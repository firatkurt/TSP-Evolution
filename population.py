import random


class Population:
    def __init__(self, individuals):
        self.individuals = individuals

    def strong(self):
        strong = min(self.individuals, key=lambda x: x.distance)
        index = self.individuals.index(strong)
        return index, strong

    def weak(self):
        weak = max(self.individuals, key=lambda x: x.distance)
        index = self.individuals.index(weak)
        return index, weak

    def average(self):
        avg = sum(i.distance for i in self.individuals) / len(self.individuals)
        return avg

    def tournament(self, count):
        instances = random.sample(self.individuals, count)
        winner = min(instances, key=lambda x: x.distance)
        index = self.individuals.index(winner)
        return index, winner

    def rand(self):
        rand = random.sample(self.individuals, 1)[0]
        index = self.individuals.index(rand)
        return index, rand

    def __str__(self):
        return "Best individual: {0} Worst individual: {1} Average: {2}"\
            .format(self.strong()[1].distance, self.weak()[1].distance, self.avg)
