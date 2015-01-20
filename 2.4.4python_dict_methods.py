
"""
this test check by Python 2.7.6 (ubuntu 14.04)

Python dict information. part2 methods. For example,

>>> a = dict (k='v', k2=3)
>>> print a.keys()
['k2', 'k']
>>> print a.values()
[3, 'v']
>>> print a.items()
[('k2', 3), ('k', 'v')]
>>>
>>> a = [1, 2, 3]
>>> del a[1]
>>> print a
[1, 3]
>>> a = dict (k='v', k2=3)
>>> del a['k2']
>>> print a
{'k': 'v'}
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
