def triarea(b,h):
    return b*h/2
def divisable(n,k):
    if n%k == 0:
            return True
    else:
        return False
def max(p,q):
    x = p[0]-q[0]
    y = p[1]-q[1]
    return {x,y}
def test(x,y,z,n):
    if x**n+y**n==z**n:
        return True
    else:
        return False
print (test(3987,4365,4472,12))
