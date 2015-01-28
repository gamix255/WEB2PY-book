
"""
this test check by Python 2.7.6 (ubuntu 14.04)

Python def...return information. For example,

>>> def f(x):
...     def g(y):
...         return x*y
...     return g
...
>>> doubler =  f(2) # doubler is a new function
>>> tripler =  f(3) # tripler is a new function
>>> quadrupler = f(4) # quadrupler is a new function
>>> print doubler(5)
10
>>> print tripler(5)
15
>>> print quadrupler(5)
20

"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()

