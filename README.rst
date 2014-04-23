===============================
PyChain
===============================

.. image:: https://badge.fury.io/py/pychain.png
    :target: http://badge.fury.io/py/pychain
    
.. image:: https://travis-ci.org/michalbachowski/pychain.png?branch=master
        :target: https://travis-ci.org/michalbachowski/pychain

.. image:: https://pypip.in/d/pychain/badge.png
        :target: https://crate.io/packages/pychain?version=latest


Chain python functions execution. For more tools supporting functional programming in Python refer to great [fn.py](https://github.com/kachayev/fn.py) module by Alexey Kachayev.

* Free software: MIT license

Example
-------

```python
>>> Chain(sum).chain(lambda a: a - 1) | (lambda b: b * 3) < [1,2,3]
15
```
