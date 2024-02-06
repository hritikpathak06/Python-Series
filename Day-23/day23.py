# List Methods In Python

list = [11,12,7,2,5,2];
print("General: ",list)

list.append(25)
print("Appended: ",list)

list.sort()
print("Sorted: ",list)

list.reverse()
print("Reverse: ",list)

print("Index: ",list.index(5))

print("Count: ",list.count(2))

copy = list.copy()
print(copy)

list.insert(1,188)
print("Insert: ",list)

m = [900,1000,11000]
k = list+m;

list.extend(m);

print(k)



