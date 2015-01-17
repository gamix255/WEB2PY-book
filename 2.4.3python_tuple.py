
"""
this test check by Python 2.7.6 (ubuntu 14.04)

Python tuple information. For example,

>>> a = [1, 2, 3]
>>> print type(a)
<type 'list'>
>>> a[1]=5
>>> print a
[1, 5, 3]
>>> a = (1, 2, 3)
>>> print type(a)
<type 'tuple'>
>>> a[1]=5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> a = (1)
>>> print a
1
>>> print type(a)
<type 'int'>
>>> a = (1,)
>>> print type(a)
<type 'tuple'>
>>> print a
(1,)
>>> a = 2, 3, "hello"
>>> x, y, z=a
>>> print y
3
>>> print z
hello

"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
