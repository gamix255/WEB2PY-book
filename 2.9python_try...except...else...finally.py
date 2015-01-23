
"""
this test check by Python 2.7.6 (ubuntu 14.04)

Python try...except...else...finally.  information. For example,

>>> try:
...     a = 1 / 0
... except Exception, e:
...     print 'oops: %s' % e
... else:
...     print 'no problem here'
... finally:
...     print 'done'
...
oops: integer division or modulo by zero
done
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()

