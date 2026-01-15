def simple_interest(pa: int,ri: float,time: int):
    return (pa*ri*time)/100

try:
    pa = int(input("Enter the principal amount: "))
    ri = float(input("Enter the Rate of Interest: "))
    time = int(input("Enter the time in years"))

    print(simple_interest(pa,ri,time))
except ValueError as e:
    print(f"The error is {e}")