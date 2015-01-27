
"""
this test check by Python 2.7.6 (ubuntu 14.04)

Python def...return and scope infomation first time. For example,

>>> a = 1
>>> def f(b):
...     return a + b
...
>>> print f(1)
2
>>>
>>> a = 2
>>> print f(1)#new value of is used
3
>>> def g(b):
...     a = 2 #creates a new local a
...     return a + b
...
>>> print g(2)
4
>>> a = 1 #reset
>>> print g(2) #global a used 
4
>>> print a
1
>>>


"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()

