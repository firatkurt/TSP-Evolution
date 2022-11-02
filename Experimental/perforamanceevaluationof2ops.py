import itertools
import generation
from dataOperation import create_population


def evaluate(initial_data, cx, mt, k=20, m=1, n=5, iteration_count=100,  generation_count=20000):
    twenty_thousand_results = []
    for i in range(iteration_count):
        result = generation.generation(initial_data, cx, mt, True, k, m, n, generation_count=generation_count)
        if len(result) != generation_count:
            raise Exception("Wrong number of generation")
        twenty_thousand_results.append(result[-1])
    best = min(twenty_thousand_results, key= lambda x: x.strong)
    worst = max(twenty_thousand_results, key= lambda x: x.strong)
    avg = sum([i.avg for i in twenty_thousand_results]) / len(twenty_thousand_results)
    return cx + "_" + mt, best, worst, avg


def evaluate_all(initial_data, iteration_count=100, generation_count=20000):
    k = [10, 20, 50]
    m = [1, 3, 5]
    n = [5, 10, 20]
    all_result = []
    products = itertools.product(k, m, n)
    for product in products:
        result = evaluate(initial_data, "PMX", "IM", product[0], product[1], product[2], iteration_count, generation_count)
        all_result.append(result)

    base = evaluate(initial_data, "PMX", "IM", iteration_count, generation_count)
