def st(s,n):
    if n<=0:
        return
    else:
        print(s)
        st(s,n-1)
def count(n):
    if n>=1:
        print (n-1)
        count(n-1)
def exponents(x,n):
    if n ==0:
        return 1
    else:
        return x*exponents(x,n-1)
def integer(n):
    if n%1==0:
        print(n,' is an integer')
    else:
        print(n," isn't an integer")
def factorish(n):
    if n<=0:
        return 1
    else:
        return n*factorish(n-2)
def itercountdown(n):
    while(n>0):
        print(n)
        n=n-1
    print("Blastoff!")
