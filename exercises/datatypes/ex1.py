def sum_two_numbers(a:int,b:int):
    return a+b

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(sum_two_numbers(a,b))
except ValueError as e:
    print(f"There is an error {e}")