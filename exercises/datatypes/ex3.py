def far_to_cels(far:float):
    return (far-32)*5/9

try:
    far = float(input("Enter the far: "))
    print(far_to_cels(far))
except:
    print("There is an error")