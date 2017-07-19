#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Module for Genetic Algorithm mutation operator class '''


class GASelection(object):
    '''
    Class for providing an interface to easily extend the behavior of selection
    operation.
    '''

    def __init__(self, pm):
        '''
        The constructor of the base-class.

        :param pm: The probability of mutation (usually between 0.001 ~ 0.1)
        :type pm: flaot in (0.0, 1.0]
        '''
        if pm <= 0.0 or pm > 1.0:
            raise ValueError('Invalid mutation probability')


    def mutate(self, individual):
        '''
        Called when an individual to be mutated.

        :param individual: The individual to be mutated.
        :type individual: GAInvidual
        '''
        raise NotImplementedError

