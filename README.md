PyChain
=======

[![PyPi package status](https://badge.fury.io/py/pychain.png)](http://badge.fury.io/py/pychain)

[![Build Status](https://travis-ci.org/michalbachowski/pychain.png?branch=master)](https://travis-ci.org/michalbachowski/pychain)

[![PIP status](https://pypip.in/d/pychain/badge.png)](https://crate.io/packages/pychain?version=latest)

Chain python functions execution. For more tools supporting functional programming in Python refer to great [fn.py](https://github.com/kachayev/fn.py) module by Alexey Kachayev.

* Free software: MIT license

Example
-------

```python
>>> Chain(sum).chain(lambda a: a - 1) | (lambda b: b * 3) < [1,2,3]
15
```
