def main():
    """
    define the main method that the problem will be resolved
    """
    problem = Problem(16,16, 2)
    field = problem.get_field()
    print(field)
    population_size = field.get_height()*field.get_width()//2
    individus = [problem.create_individual() for i in range(population_size)]
    for individu in individus:
        print("{} {}".format(individu, individu.get_score()))
    print()
    print()
    for i in range(50):
        next_gen1 = []
        next_gen2 = []
        shuffle(individus)
        j=0
        while(j<population_size-1):
            individu1, individu2 = individus[j], individus[j+1]
            best_individu_tournoi = problem.tournament(individu1, individu2)
            next_gen1.append(best_individu_tournoi)
            cross1, cross2 = individu1.cross_with(individu2)
            cross1.evaluate(problem)
            cross2.evaluate(problem)
            best_individu_cross = problem.tournament(cross1, cross2)
            next_gen2.append(best_individu_cross)
            j+=2
        next_gen = next_gen1+next_gen2
        for individu in next_gen:
            individu.mutate(0.05)
            individu.evaluate(problem)
            print("{} {}".format(individu, individu.get_score()))
        print()
        problem.sort_population(next_gen)
        for individu in next_gen:
            print("{} {}".format(individu, individu.get_score()))
        print()
        meilleurs = next_gen[len(next_gen)-5:][:]
        next_gen = next_gen[5:][:]
        individus = next_gen+meilleurs
        for individu in individus:
            print("{} {}".format(individu, individu.get_score()))
        print()
        print()
    res = problem.best_individual(individus)
    print("{} {}".format(res, problem.evaluate_fitness(res)))
    print(field)
    return res