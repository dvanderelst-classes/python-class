
####1
import math
import random

lst = ['josh',3, math.pi]

####2
# one option...
lst.append(True)
# and another.
lst = lst + [True]

####3
# one option...
lst = [False] + lst
# and another.
lst.insert(0,False)

####4
a = range(1000,2501)
a = list(a)

####5
a.remove(1234)

####6
a.pop(1000)

####7
random.shuffle(a)

####8
print(a[0:10])

###10
print(1000 in a)

####11
a[2] = 'some string'



