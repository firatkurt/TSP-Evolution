from dataOperation import create_generation


def evaluate_average_result(results):
    avg_best_result = sum(results, key=lambda x: x[0])/len(results)
    avg_avg_result = sum(results, key=lambda x: x[1])/len(results)
    return avg_best_result, avg_avg_result


def evaluate(crossover, mutation, initial_data, iteration_count=100, generation_count=20000):
    thousand_results = []
    five_thousand_results = []
    twenty_thousand_results = []
    for i in range(iteration_count):
        initial_generation = create_generation(initial_data)
        for j in range(generation_count):
            if j == 1000:
                _, best = initial_generation.strong()
                average = initial_generation.avarage()
                thousand_results.append((best, average))
            elif j == 5000:
                _, best = initial_generation.strong()
                average = initial_generation.avarage()
                five_thousand_results.append((best, average))
            #do crossover, mutation and two_opt something
        _, best = initial_generation.strong()
        average = initial_generation.avarage()
        twenty_thousand_results.append((best, average))

    avg_thousand_results = evaluate_average_result(thousand_results)
    avg_five_thousand_results = evaluate_average_result(five_thousand_results)
    avg_twenty_thousand_results = evaluate_average_result(twenty_thousand_results)
    print("Avg 1000. iteration result of {0}_{1}: Best: {2}, Avg{3}") \
        .format(crossover, mutation, avg_thousand_results[0], avg_thousand_results[1])
    print("Avg 5000. iteration result of {0}_{1}: Best: {2}, Avg{3}") \
        .format(crossover, mutation, avg_five_thousand_results[0], avg_five_thousand_results[1])
    print("Avg 20000. iteration result of {0}_{1}: Best: {2}, Avg{3}") \
        .format(crossover, mutation, avg_twenty_thousand_results[0], avg_twenty_thousand_results[1])

    return avg_thousand_results, avg_five_thousand_results, avg_twenty_thousand_results


