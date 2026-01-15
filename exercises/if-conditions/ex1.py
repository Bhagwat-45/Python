def largest(var1: int,var2: int):
    return var1>var2

var1 = int(input("Enter the first number: "))
var2 = int(input("Enter the second number: "))

if(largest(var1,var2)):
    print("The var1 is higher")
else:
    print("The var2 is higher")

