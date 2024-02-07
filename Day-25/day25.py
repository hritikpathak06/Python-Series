# Opeartions On Tuple In Python
countries = ("India","America","Russia","Newzealand","Africa")
print(countries)
temp = list(countries)
temp.append("Pakistan")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)
print(countries.count("India"))
print(countries.index("Finland"))