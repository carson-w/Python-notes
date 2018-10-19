def factorial(n):
    '''
    Description: Finds the factorial of n
    Parameters: N
    Return Values: It returns the factorial of n
    '''
    if n == 1:
        return 1
    return n* factorial(n-1)
def secfac(n):
    g = n
    while g > 1:
        g-=1
        n = n*g
    print("That has " + str(len(str(n))) +" digits")
    return n
def fibonacci(n):
    '''
    finds the nth term in the fibonacci sequence
    Parameters:n
    Returns: the nth term
    '''
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
'''
while True:
    n = input("enter a number:")
    if (n=="done"):
        break
    else:
        print(n)
'''
print(secfac(10000))
