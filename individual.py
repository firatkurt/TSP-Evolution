
class Individual:
    def __init__(self, nodes, distance):
        self.nodes = nodes
        self.distance = distance
    
    def __str__(self):
        return "Individual Distance: {0}".format(self.distance)

