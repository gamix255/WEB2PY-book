
"""
this test check by Python 2.7.6 (ubuntu 14.04)

Python def...return and scope infomation first time. For example,

>>> def f(a):
...     return a + 1
...
>>> print f(1)
2
>>> print a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>>


"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()

