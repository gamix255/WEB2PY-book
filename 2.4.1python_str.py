"""
this test check by Python 2.7.6 (ubuntu 14.04)

Python type infomation. For example,

>>> a = 'this is an ASCII string'
>>> b = u'This is a Unicode string'
>>> print type(a)
<type 'str'>
>>> print type(b)
<type 'unicode'>
>>> a = b.encode('utf8')
>>> print type(a)
<type 'str'>
>>> print a
This is a Unicode string
>>>
>>> print 'number is ' + str(3)
number is 3
>>> print 'number is %s' % (3)
number is 3
>>> print 'number is %(number)s' % dict (number=3)
number is 3
>>> print 'number is %(i)s' % dict (i=3)
number is 3
>>>
>>> for i in  [3, 'hello']:
...    print str(i), repr(i)
...
3 3
hello 'hello'
>>> for i in 'hello':
...   print i
...
h
e
l
l
o
"""



if __name__ == "__main__":
    import doctest
    doctest.testmod()
