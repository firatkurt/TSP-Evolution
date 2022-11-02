import generation
import matplotlib.pyplot as plt


def evaluate(initial_data, cx, mt, generation_count=20000):
    result = generation.generation(initial_data, cx, mt, True, generation_count)
    return result


def evaluate_all(initial_data):
    best = evaluate(initial_data, "PMX", "IM")
    worst = evaluate(initial_data, "PMX", "SM")
    x = list(range(1, len(best)+1))
    best_best = [i.strong for i in best]
    best_avg = [i.avg for i in best]

    worst_best = [i.strong for i in worst]
    worst_avg = [i.avg for i in worst]

    figure, axis = plt.subplots(2, 1)
    figure.tight_layout(pad=5.0)
    axis[0].plot(x, best_best, label="Best")
    axis[0].plot(x, best_avg, label="Avg")
    axis[0].set_title("PMX and IM Best Result")

    axis[1].plot(x, worst_best, label="Best")
    axis[1].plot(x, worst_avg, label="Avg")
    axis[1].set_title("PMX and SM Worst Result")
    plt.show()