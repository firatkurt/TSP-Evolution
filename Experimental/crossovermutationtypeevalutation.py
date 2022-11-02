import itertools

from dataOperation import create_population
import generation


def evaluate_average_result(results):
    avg_best_result = sum(x.strong for x in results) / len(results)
    avg_avg_result = sum(x.avg for x in results) / len(results)
    return avg_best_result, avg_avg_result


def evaluate(initial_data, cx, mt, iteration_count=100, generation_count=20000):
    thousand_results = []
    five_thousand_results = []
    twenty_thousand_results = []
    for i in range(iteration_count):
        result = generation.generation(initial_data, cx, mt, True, generation_count=generation_count)
        if len(result) != generation_count:
            raise Exception("Wrong number of generation")
        thousand_results.append(result[999])
        five_thousand_results.append((result[4999]))
        twenty_thousand_results.append(result[-1])

    avg_thousand_results = evaluate_average_result(thousand_results)
    avg_five_thousand_results = evaluate_average_result(five_thousand_results)
    avg_twenty_thousand_results = evaluate_average_result(twenty_thousand_results)
    print("Avg 1000. iteration result of {0}_{1}: Best: {2}, Avg {3}"
          .format(cx, mt, avg_thousand_results[0], avg_thousand_results[1]))
    print("Avg 5000. iteration result of {0}_{1}: Best: {2}, Avg {3}"
          .format(cx, mt, avg_five_thousand_results[0], avg_five_thousand_results[1]))
    print("Avg 20000. iteration result of {0}_{1}: Best: {2}, Avg {3}"
          .format(cx, mt, avg_twenty_thousand_results[0], avg_twenty_thousand_results[1]))
    return cx + "_" + mt, avg_thousand_results, avg_five_thousand_results, avg_twenty_thousand_results


def evaluate_all(initial_data, iteration_count=100, generation_count=20000):
    all_result = []
    cxs = ["PMX", "OX"]
    mts = ["SM", "IM", "IVM"]
    products = itertools.product(cxs, mts)
    for product in products:
        result = evaluate(initial_data, product[0], product[1], iteration_count, generation_count)
        all_result.append(result)

    [print("Cx and mutation: {0} \nThousand results {1} {2} \nfive thousand results: {3} {4}"
           " \ntwenty thousand results: {5} {6}\n"
           .format(i[0], i[1][0], i[1][1], i[2][0], i[2][1], i[3][0], i[3][1])) for i in all_result]
