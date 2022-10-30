def parent_selection(generation, tournament_count):
    first = generation.tournament(tournament_count)
    second = generation.tournament(tournament_count)
    while first != second:
        second = generation.tournament(tournament_count)
    return first, second


def survival_selection(generation):
    weak = generation.weak()
    second = generation.rand()
    while weak != second:
        second = generation.rand()
    return weak, second
