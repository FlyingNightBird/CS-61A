""" Lab 04 Optional Questions """

from lab04 import *

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    anslist = []
    i,j=0,0
    while i<len(s):
        if pow(s[i],0.5)==round(pow(s[i],0.5)):
            anslist[j]=pow(s[i],0.5)
            j+=1
        i+=1
    return anslist
seq = [8, 49, 8, 9, 2, 1, 100, 102]
print(squares(seq))
def key_of_min_value(d):
    """Returns the key in a dict d that corresponds to the minimum value of d.
    >>> letters = {'a': 6, 'b': 5, 'c': 4, 'd': 5}
    >>> min(letters)
    'a'
    >>> key_of_min_value(letters)
    'c'
    """
    "*** YOUR CODE HERE ***"
