#Print list of numbers greater than 0.
number_list = [5,19,5,20,-1,-5,-9,-23,10,11,51,-17]
empty_list = []

for numbers in number_list:
    if numbers > 0:
        empty_list.append(numbers)

print(empty_list)