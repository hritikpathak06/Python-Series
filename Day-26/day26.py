# Exercise -2 Solution
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
print(hour)

if(hour >= 0 and hour<12):
    print("Good Morning sir")
elif(hour >= 12 and hour<=18):
    print("Good Evening Sir")
else:
    print("Good Night Sir")
