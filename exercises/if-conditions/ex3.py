def even_odd(var1:int):
    return var1%2==0

var1 = int(input("Enter the number: "))

if(even_odd(var1)):
    print("Even")
else:
    print("Odd")

    