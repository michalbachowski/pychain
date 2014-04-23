#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Chain(object):
    """Class that allows users to chain function execution"""

    def __init__(self, *functions):
        """Class initialization

        Params:
            :param:    *functions  -- one or more functions to be chained
            :type:     *functions  -- tuple

        >>> Chain()
        <pychain.chain.Chain object at 0x...>
        >>> Chain(1,2,3,)
        <pychain.chain.Chain object at 0x...>
        >>> Chain(sum).execute([1,2,3])
        6
        """
        self._f = list(functions)

    def chain(self, *functions):
        """Adds one or more function to chain

        Params:
            :param:    *functions  -- one or more functions to be chained
            :type:     *functions  -- tuple

        >>> Chain().chain()
        <pychain.chain.Chain object at 0x...>
        >>> Chain().chain(sum)
        <pychain.chain.Chain object at 0x...>
        >>> Chain(sum).chain(lambda a: a-1).execute([1,2,3])
        5
        """
        self._f.extend(functions)
        return self

    def __or__(self, function):
        """Adds function to chain

        Params:
            :param:    functions  -- one or more functions to be chained
            :type:     functions  -- callable

        >>> Chain() | sum
        <pychain.chain.Chain object at 0x...>
        >>> (Chain(sum) | (lambda a: a-1)).execute([1,2,3])
        5
        """
        self.chain(function)
        return self

    def execute(self, data):
        """Executes chained function with given input data

        Params:
            :param:    data -- data to be passed to functions
            :type:     data -- any

        >>> Chain().execute()
        Traceback (most recent call last):
        ...
        TypeError: execute() takes exactly 2 arguments (1 given)
        >>> Chain().execute(1)
        1
        >>> Chain(sum, lambda a: a-1).execute([1,2,3])
        5
        """

        for function in self._f:
            data = function(data)
        return data

    def __call__(self, data):
        """Executes chained function with given input data

        Params:
            :param:    data -- data to be passed to functions
            :type:     data -- any

        >>> Chain()()
        Traceback (most recent call last):
        ...
        TypeError: __call__() takes exactly 2 arguments (1 given)
        >>> Chain()(1)
        1
        >>> Chain(sum, lambda a: a-1)([1,2,3])
        5
        """
        return self.execute(data)

    def __lt__(self, data):
        """Executes chained function with given input data

        Params:
            :param:    data -- data to be passed to functions
            :type:     data -- any

        >>> Chain() < 1
        1
        >>> Chain(sum, lambda a: a-1) < [1,2,3]
        5
        """
        return self.execute(data)
