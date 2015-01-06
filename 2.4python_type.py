"""
this test check by Python 2.7.6 (ubuntu 14.04)

Python type infomation. For example,

>>> a = 3
>>> print type(a)
<type 'int'>
>>> a = 3.14
>>> print type(a)
<type 'float'>
>>> a = 'hello python'
>>> print type(a)
<type 'str'>
"""



if __name__ == "__main__":
    import doctest
    doctest.testmod()
