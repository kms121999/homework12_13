



def main():
    myFunc(5, True)



def myFunc(myInt, increasing):

    if increasing:
        for n in range(1, myInt + 1):
            print("*" * n)
        myFunc(myInt, False)

    else:
        for n in range(myInt - 1, 0, -1):
            print("*" * n)







'''
    if increasing:
        if myInt > 1:
            myFunc(myInt - 1, True)
        print("*" * myInt)
        
    if not increasing:
        print("*" * (myInt - 1))
        if myInt > 1:
            myFunc(myInt - 1, False)




def func2(n, y):
    if y:
        if n > 1:
            func2(n-1, True)
        print("*" * n)

    if not y:
        print("*" * (n-1))
        if n > 2:
            func2(n-1, False)
'''

    
    
