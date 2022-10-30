from dataOperation import create_generation


def evaluate(crossover, mutation, initial_data, generation_count=20000):
    best_performance_results = []
    avg_performance_results = []
    initial_generation = create_generation(initial_data)
    for j in range(generation_count):
        #do crossover, mutation and two_opt something
        _, best = initial_generation.strong()
        best_performance_results.append(best)
        average = initial_generation.avarage()
        avg_performance_results.append(average)
    return best_performance_results, avg_performance_results
