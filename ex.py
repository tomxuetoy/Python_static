def f(a, L=[]):
    L.append(a)
    return L
 
print f(1)
print f(2)
print f(3)
print f(4,['x'])
print f(5)
