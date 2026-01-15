def power_of_two(power:int):
    sum = 1
    for i in range(power):
        sum = sum*2
        print(sum)

power_of_two(5)