def consecutive(string):
    x = 0
    if len(string)>=6:
        for i in range(len(string)-6):
            if string[i] == string[i+1] and string[i+2] == string[i+3] and string[i+4] == string[i+5]:
                return True
    return False
def equalizer(x):
    y = str(x)
    if x<100000:
        y= '0' +y
        if x<10000:
            y = '0' + y
            if x<1000:
                y = '0' + y
                if x<100:
                    y = '0' + y
                    if x<10:
                        y = '0' + y
    return y

def is_palindrome(x):
    test = ''
    for i in range(len(x)):
        test += x[len(x)-i-1]
    if test == x:
        return True
    else:
        return False

def palendromicnumb():
    list = ''
    for i in range(0,999999):
        if is_palindrome(equalizer(i)) == True:
            list += str(equalizer(i))
            list += '\n'
    return list
