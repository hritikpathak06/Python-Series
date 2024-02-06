# Functions In Python
def greateNum(a,b):
    if(a>b):
        print("A is Greater")
    else:
        print("B is Greater")
        
def calclulateMean(a,b):
    mean = (a*b)/(a+b)
    print("Mean: ",mean)
    num = greateNum(a,b)
    return num
    
calclulateMean(10,12)
calclulateMean(12,2)