# Introduction To List In Python
num = [3,4,6,7,10,"Rohit"]

print(num)
print(type(num))
num.append(12)
print(num)
print(len(num))

if "t" in "Rohit":
    print("Yes")
else:
    print("No")
    
    
marks = [18,97,63,"Ritik",11,78,"Kartik",111,88]
print(marks)
print(marks[1:7])
print(marks[1:10:2])

# List Compherisson
lst = [i*i for i in range(4)]
print(lst)

lst = [i for i in range(10) if i%2==0]
print(lst)