
"""
this test check by Python 2.7.6 (ubuntu 14.04)

Python dict information. For example,

>>> a = { 'k':'v','k2':3 }
>>> print type(a)
<type 'dict'>
>>> a['k']
'v'
>>> a['k2']
3
>>> a.has_key('k')
True
>>> a.has_key('v')
False
>>> 

>>> a = dict(k='v',h2=3)
>>> a['k']
'v'
>>> print a
{'h2': 3, 'k': 'v'}
>>>

"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
