# F-string In Python
letter = "Hey My Name is {1} and I am from {0}"

country = "India"
name = "Ritik"

print(letter.format(country,name));
print(f"Hey My Name is {name} and I am from {country}")

print(type(f"Hey My Name is {name} and I am from {country}"))

