def parent_selection(population, tournament_count):
    _, first = population.tournament(tournament_count)
    _, second = population.tournament(tournament_count)
    while first == second:
        _, second = population.tournament(tournament_count)
    return first, second


def survival_selection(population):
    weak = population.weak()
    second = population.rand()
    while weak == second:
        second = population.rand()
    return weak, second


def two_opt_selection(population, m):
    two_opts = [population.strong()]
    m += 1
    while len(two_opts) < m:
        rand = population.rand()
        if rand not in two_opts:
            two_opts.append(rand)
    return two_opts
