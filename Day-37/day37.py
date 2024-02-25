# Finally Keyword In Python
def func1():
     try:
      l=[1,5,6,7]
      i = int(input("Enter The Index: "))
      print(l[i])
      return 1
     except:
      print("some error occured")
      return 0
     finally:
      print(l,"I am always Executed")
       
func1()