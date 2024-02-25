# Exception Handling In Python
a = input("Enter the number: ")
print(f"Multiplication table of {a} is : ")

try:
   for i in range(1,11):
    print(f"{a} X {i} = {int (a)*i}")
except:
    print("Invalid Input")
    
    
print("some lines of code")
print("end of programs")