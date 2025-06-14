# conditional_Handling 
import sys

type = sys.argv[1]
if type == "t2.micro":
    print("ok,we will create the instance for you")
elif type == "t2.medium":
    print("it will charge you 4 dollar a day")
elif type =="t2.xlarge":
    print("it will charge you 8 dollars a day")
else :
    print("Please provide a validate instance type")
    