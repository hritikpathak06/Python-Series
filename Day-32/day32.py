# SETS METHODS IN PYTHON

s1 = {1,2,5,6}
s2 = {3,6,7}

print(s1.union(s2))
print(s1.intersection(s2))
s1.update(s2)
print(s1,s2)

cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo", "Seoul","Kabul","Madrid"}
cities.add("Bhopal")
cities.remove("Tokyo")

print(cities)
print(cities.isdisjoint(cities2))
print(cities.issuperset(cities2))

