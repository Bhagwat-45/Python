sum = 0
prev_number = 0

for i in range(10):
    sum = i + prev_number
    print(f"Current Number {i} Previous Number {prev_number} Sum : {sum}")
    prev_number = i