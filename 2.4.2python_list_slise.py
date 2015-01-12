
"""
this test check by Python 2.7.6 (ubuntu 14.04)

Python list infomation. For example,

>>> a = [1, 2, 3]
>>> print type(a)
<type 'list'>
>>> print a
[1, 2, 3]
>>> a.append(8)
>>> print a
[1, 2, 3, 8]
>>> a.insert (2,7 )
>>> print a
[1, 2, 7, 3, 8]
>>> del a[0]
>>> print a
[2, 7, 3, 8]
>>> print len (a)
4
>>>
"""

"""
this test check by Python 2.7.6 (ubuntu 14.04)

Python list infomation. part 2, slice For example,

>>> a = [2, 7, 3, 8]
>>> a = [2, 7, 3, 8, 1]
>>> print a[:3]
[2, 7, 3]
>>> print a[-2]
8
>>> print a[-2:]
[8, 1]
>>> print a[:-2]
[2, 7, 3]
>>> print a[1:]
[7, 3, 8, 1]
>>> print a[1:-1]
[7, 3, 8]
>>> 
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
