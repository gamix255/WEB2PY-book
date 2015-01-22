
"""
this test check by Python 2.7.6 (ubuntu 14.04)

Python if ... elif ... else  information. For example,

>>> for i in range(3):
...     if i == 0:
...         print 'zero'
...     elif i == 1:
...         print 'one'
...     else:
...         print 'other'
...
zero
one
other
>>> for i in range(3):
...     if i == 0 or (i == 1 and i + 1 == 2):
...         print '0 or 1'
...
0 or 1
0 or 1
>>>
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()

