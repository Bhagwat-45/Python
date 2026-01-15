def pos_neg(var1:int):
    return var1>0

var1 = int(input("Enter the number: "))

if(pos_neg(var1)):
    print("Positive Number")
else:
    print("Negative Number")