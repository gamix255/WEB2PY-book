
"""
this test check by Python 2.7.6 (ubuntu 14.04)

Python indent information. For example,

>>> i = 0
>>> while i < 3:
...     print i
...     i = i + 1
...
0
1
2
>>> a = [0, 1, 'hello', 'python']
>>> for i in a:
...   print i
...
0
1
hello
python
>>>
>>> for i in xrange (0,4):
...     print i
...
0
1
2
3
>>> for i,j in enumerate(a):
...     print i,j
...
0 0
1 1
2 hello
3 python
>>>
>>> for i in [1, 2, 3]:
...     print i
...     break
...
1
>>> for i in [1, 2, 3]:
...     print i
...     continue
...     print 'test'
...
1
2
3
>>>
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
