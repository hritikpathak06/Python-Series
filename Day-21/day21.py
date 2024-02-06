# Function Arguments And Return Statements
def Average(a,b):
    print("The Average Is:",(a+b)/2)
    
Average(10,12)


def name (firstName,middleName='Kumar',lastName="Pathak"):
    print("Hello ",firstName,middleName,lastName)
name("Ritik",'',"Pandey")


def ManyAvarage(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    print("Average Is: ",sum/len(numbers))
    
ManyAvarage(10,12,22)