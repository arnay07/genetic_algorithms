#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`individual` module

:author: Arnaud Kaderi, Elhadj Ibrahima BAH, Aboubakar Siriki Diakité


:date: 2019, November
:last revision: 08/12/2019

"""

from enum import Enum
from problem import *
from random import *

DIRECTIONS = ['U','D','L','R']



class IndividualState(Enum):
    """
    A class to define an enumarated type with four values:
        
        *``success``
        *``blocked``
        *``monster``
        *``alive``
        
    for the four state of the individual state
    """
    success = 1
    blocked = 2
    monster = 3
    alive = 4
    start = 5


class Individual(object):
    def __init__(self, y, x):
        """
        an Individual in genetic algorithm problem
        the value (or genome) of an individual is a sequence (e.g string or list) of a fixed size
        an individual has a fitness score

        :param size: (int) the length of the sequence of the individual

        """
        self.__fitness = 0
        self.__position = (y,x)
        self.__value = self.init_value()
        self.__state = IndividualState.start
        
    def get_position(self):
        return self.__position
    
    def set_position(self, x,y):
        self.__position = (x,y)
    
    def get_state(self):
        return self.__state
    
    def set_state(self, state):
        self.__state = state
        

    def copy(self):
        """
        build a copy of self, the genome is a copy of self’s genome

        :return: a new individual which is a << clone >> of self
        :rtype: an Individual object

        """
        individual_copy = Individual(self.get_position()[0], self.get_position()[1])
        individual_copy.set_value(self.get_value()[:])
        return individual_copy

    def cross_with(self, other):
        """
        perform a 1 point crossover between self and other,
        two new built individuals are returned

        :param other: (Individual) another individual

        """
        coupe_point = randint(1, 242)
        individu1 = self.copy()
        individu2 = other.copy()
        genome_list1 = individu1.get_value()[:]
        genome_list2 = individu2.get_value()[:]
        i=0
        while(i<coupe_point):
            genome_list1[i], genome_list2[i] = genome_list2[i], genome_list2[i]
            i+=1
        individu1.set_value(genome_list1)
        individu2.set_value(genome_list2)
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
        self.set_score(problem.evaluate_fitness(self))

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
        for i in range(243):
            gene = choice(DIRECTIONS)
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

        for i in range(243):
            if random() < probability:
                gene = choice(DIRECTIONS)
                self.get_value()[i] = gene

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
        return '{}'.format("".join(self.get_value()))
    
if __name__=='__main__':
    individu = Individual()
    print(individu)
    
