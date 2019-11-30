#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`individual` module

:author: Arnaud Kaderi, Elhadj Ibrahima BAH, Aboubakar Siriki Diakité


:date: 2019, November
:last revision: 25/11/2019

"""


from problem import *
from random import *

class Individual(object):
    def __init__(self, size):
        """
        an Individual in genetic algorithm problem
        the value (or genome) of an individual is a sequence (e.g string or list) of a fixed size
        an individual has a fitness score

        :param size: (int) the length of the sequence of the individual

        """
        self.__fitness = 0
        self.__size = size
        self.__value = self.init_value()

    def copy(self):
        """
        build a copy of self, the genome is a copy of self’s genome

        :return: a new individual which is a << clone >> of self
        :rtype: an Individual object

        """
        individual_copy = Individual(self.get_size())
        individual_copy.set_value(self.get_value()[:])
        return individual_copy

    def cross_with(self, other):
        """
        perform a 1 point crossover between self and other,
        two new built individuals are returned

        :param other: (Individual) another individual

        """
        coupe_point = randint(1, self.get_size()-1)
        individu1 = self.copy()
        individu2 = other.copy()
        i=0
        while(i<coupe_point):
            individu1.get_value()[i], individu2.get_value()[i] = individu2.get_value()[i], individu1.get_value()[i]
            i+=1
        return (individu1, individu2)

    def get_value(self):
        """
        return the list of genes

        """
        return self.__value

    def evaluate(self, problem):
        """
        set the fitness score with the fitness computed by problem for self

        :param problem: (Problem) the problem

        """
        self.set_score(problem.evaluate_fitness(self)[1])

    def get_score(self):
        """
        return the fitness score

        :return: the fitness score
        :rtype: int
        """
        return self.__fitness

    def get_size(self):
        """
        :return: the size of self's genome
        :rtype: int
        """
        return self.__size

    def init_value(self):
        """
        randomly initialize the genome value of self

        :return: the genome of self
        :rtype: list
        """
        genome = []
        for i in range(self.get_size()):
            gene = randint(0,1000)%2
            genome.append(gene)
        return genome

    def mutate(self, probability):
        """
        apply mutation operation to self : each element of the genome
        sequence is randomly changed with given probabiliy

        side effect: self's genome is modified
        :param probability: (float) the probability of mutation for every gene
        :UC: probability in [0,1[

        """
        assert 0 <= probability < 1, 'the probability must be between 0 and 1 excluded'

        for i in range(self.get_size()):
            if random() < probability:
                self.get_value()[i] = self.get_value()[i] ^ 1

    def set_score(self, new_score):
        """
        change the fitness score of self

        :param new_score: (int) the new fitness score

        """
        self.__fitness = new_score

    def set_value(self, new_value):
        """
        change the genome value of self

        :param new_value: (list) the new genome value

        """
        self.__value = new_value

    def calculate_N(self):
        """
        calculate the value of the binary value in decimal value

        """
        res = 0
        for i in range(self.get_size()):
           res += self.get_value()[i]*(2**(self.get_size()-(i+1)))
        return res


    def __repr__(self):
        """
        represent the way individuals have to be written
        """
        return '{}'.format(self.get_value())

#def main():
#    """
#    main program to run on the population
#    given to a problem
#
#    """
#    global POPULATION_SIZE
#    global CROSSOVER_RATE



if __name__=='__main__':
    problem = Problem(13,18)
    individu = Individual(8)
    individu.evaluate(problem)
    individu2 = Individual(8)
    individu2.evaluate(problem)
    population = [individu, individu2]
    for i in population:   
        print("{} {}".format(i, i.get_score()))    
    print()
    individu3, individu4 = individu.cross_with(individu2)
    individu3.evaluate(problem)
    print("{} {}".format(individu3, individu3.get_score())) 
    individu4.evaluate(problem)
    print("{} {}".format(individu4, individu4.get_score())) 
    print()
    population.append(individu3)
    population.append(individu4)
    for ind in population:   
        print("{} {}".format(ind, ind.get_score()))    
   
#    

    

