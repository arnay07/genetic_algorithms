#!/usr/bin/python3
# -*- coding: utf-8 -*-




class Individual_Interface(object):

    def __init__(self, size):
        """
        an Individual in genetic algorithm problem
        the value (or genome) of an individual is a sequence (e.g string or list) of a fixed size
        an individual has a fitness score

        :param gene_length:(int) the length of the sequence of the individual

        """

        self.__fitness = 0
        self.__size = size
        self.__value = []




    def copy(self):
        """
        build a copy of self, the genome is a copy of self’s genome

        :return: a new individual which is a << clone >> of self
        :rtype: an Individual object

        """

        individual_copy = Individual_Interface(self.get_size())
        individual_copy.set_value(self.get_value()[:])

        return individual_copy


    def cross_with(self, other):
        """
        perform a 1 point crossover between self and other,
        two new built individuals are returned

        :param other:(Individual) another individual

        """
        coupe_point = randint(1, self.get_size()-1)
        i=0
        while(i<coupe_point):
            self.get_value()[i], other.get_value()[i] = other.get_value()[i], self.get_value()[i]
            i+=1
        return (self, other)

    def get_value(self):
        """
        return the list of genes

        """
        return self.__value


    def evaluate(problem):
        """
        set the fitness score with the fitness computed by problem for self

        :param problem:(Problem) the problem

        """

        pass


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
        score = 0
        for (i in range(self.get_size())):
            gene = randint(0,100)%2
            self.get_value()[i] = gene
            if gene==1:
                score += 1
                self.set_score(score)


    def mutate(self, probability):
        """
        apply mutation operation to self : each element of the genome
        sequence is randomly changed with given probabiliy

        side effect: self's genome is modified
        :param probability:(float) the probability of mutation for every gene
        :UC: probability in [0,1[

        """
        assert 0 <= probability < 1, 'the probability must be between 0 and 1 excluded'

        for i in range(self.get_size()):
            value = random()
            if value < probability:
                self.get_value()[i] = self.get_value()[i] ^ 1




    def set_score(self, new_score):
        """
        change the fitness score of self

        :param new_score:(int) the new fitness score

        """
        self.__fitness = new_score



    def set_value(self, new_value):
        """
        change the genome value of self

        :param new_value:(list) the new genome value

        """

        self.__value = new_value










