def avg(a:float,b:float,c:float):
    return (a+b+c)/3

try:
    a = float(input("Enter a number: "))
    b = float(input("Enter a number: "))
    c = float(input("Enter a number: "))
    print(avg(a,b,c))
except:
    print("There is an error!")