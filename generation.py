import random


class Generation:
    def __init__(self, population):
        self.population = population

    def strong(self):
        strong = min(self.population, key=lambda x: x.distance)
        index = self.population.index(strong)
        return index, strong

    def weak(self):
        weak = max(self.population, key=lambda x: x.distance)
        index = self.population.index(weak)
        return index, weak

    def avarage(self):
        avarage = sum(self.population, key=lambda x: x.distance)/len(self.population)
        return avarage

    def tournament(self, count):
        instances = random.sample(self.population, count)
        winner = min(instances, key=lambda x: x.distance)
        index = self.population.index(winner)
        return index, winner

    def rand(self):
        rand = random.sample(self.population, 1)[0]
        index = self.population.index(rand)
        return index, rand
