#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`algogen` module

:author: Arnaud Kaderi, Elhadj Ibrahima BAH, Aboubakar Siriki Diakité

:date: 14/11/2019

"""


import sys
from random import *


class AlgoGen(object):
    def __init__(self, problem, individual_size, population_size, crossover_rate, mutation_probability):
        """
        build a genetic algorithm to solve problem using a population of size population_size
        and a probability of mutation of mutation_probability

        :param problem:(Problem object) the problem to solve
        :param population_size:(int) the size of the population (must be even)
        :param mutation_probability:(float) the mutation probability
        :param crossover_rate: the crossover rate
        :UC: population_size must be even and mutation_probability must be >= 0 and <1

        """
        self.__problem = problem
        self.__population_size = population_size
        self.__crossover_rate = crossover_rate
        self.__mutation_probability = mutation_probability
        self.__individual_size = individual_size

    def get_problem(self):
        """
        return the genetic algorithm's problem
        """
        return self.__problem

    def get_population_size(self):
        """
        return the population size
        """
        return self.__population_size

    def get_crossover_rate(self):
        """
        return the crossover rate
        """

        return self.__crossover_rate

    def get_mutation_probability(self):
        """
        return the mutation probability
        """
        return self.__mutation_probability

    def get_individual_size(self):
        """
        return the mutation probability
        """
        return self.__individual_size


    def action_on_population(self, individus):
        """
        """

        problem = self.get_problem()
        for i in range(self.get_crossover_rate()):
            next_gen1 = []
            next_gen2 = []
            shuffle(individus)
            j=0
            while(j<self.get_population_size()-1):
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
                individu.mutate(self.get_mutation_probability())
                individu.evaluate(problem)
            #     print("{} {}".format(individu, individu.get_score()))
            # print()
            problem.sort_population(next_gen)
            print('{} {}\n'.format(next_gen[-1], problem.evaluate_fitness(next_gen[-1])))
            # for individu in next_gen:
            #     print("{} {}".format(individu, individu.get_score()))
            # print()
            meilleurs = next_gen[len(next_gen)-5:][:]
            next_gen = next_gen[5:][:]
            individus = next_gen+meilleurs
            # for individu in individus:
            #     print("{} {}".format(individu, individu.get_score()))
            # print()
            # print()
            
        
        res = problem.best_individual(individus)
        # print("{} {}\n".format(res, problem.evaluate_fitness(res)))
        return res






























