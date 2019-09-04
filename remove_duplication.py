#Removes duplicate items in list using dictionary -> <- list conversion

number_list = [5,6,7,8,4,6,5,3]

no_dupes = list(dict.fromkeys(number_list))

print(no_dupes)