# Time Module

import time
timestamp = str(time.strftime("%H"));
print(type(timestamp))

name = str(input("Enter Your Name: "));

if(timestamp < 12):
    print("Good Morning ",name)
elif(timestamp >12 & timestamp<18):
    print("Good Evening ",name)
else:
    print("Good night ",name)