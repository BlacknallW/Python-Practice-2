#Uppercase a String
user_input = input("Type anything here, pretty much. ")

print(f"{user_input.upper()}")

#Capitalize a String
user_input = input("Again, type whatever you want here. Ideally letters. ")

print(f"{user_input.title()}")

#Reverse a String
user_input = input("Guess who? It's me again. Type stuff. ")
reverse = "".join(reversed(user_input))

print(f"{reverse}")
