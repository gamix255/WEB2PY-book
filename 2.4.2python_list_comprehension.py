
"""
this test check by Python 2.7.6 (ubuntu 14.04)

Python list information. part 5, comprehension. For example,

>>> a = [1, 2, 3, 4, 5]
>>> b = []
>>> for x in a:
...    if x % 2 == 0:
...       b.append(x * 3)
...
>>> b
[6, 12]

>>> 

>>> a = [1, 2, 3, 4, 5]
>>> b = [x * 3 for x in a if x % 2 == 0]
>>> b
[6, 12]
>>>
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
