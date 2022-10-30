from dataOperation import create_generation


def evaluate(crossover, mutation, initial_data, k, m, n, generation_count=20000 ):
    base_performance_results = []
    two_opt_performance_results = []
    initial_generation = create_generation(initial_data)
    base_generation = initial_generation.clone()
    for j in range(generation_count):
        #do crossover, mutation  something
        pass
    _, base_best = base_generation.strong()
    _, base_worst = base_generation.weak()
    base_avg = base_generation.average()
    for j in range(generation_count):
        # do crossover, mutation and 2_opts  something
        pass
    _, two_opt_best = base_generation.strong()
    _, two_opt_worst = base_generation.weak()
    two_opt_avg = base_generation.average()
    best_rate = (base_best/two_opt_best) - 1
    worst_rate = (base_worst/two_opt_worst) - 1
    avg_rate = (base_avg/two_opt_avg) - 1
    return best_rate, worst_rate, avg_rate
