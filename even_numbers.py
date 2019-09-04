#Even Numbers

number_list = [1,5,8,4,3,7,8,1,7,4,8,10]

empty_list = []


for numbers in number_list:
    if numbers % 2 == 0:
        empty_list.append(numbers)
        

print(empty_list)

