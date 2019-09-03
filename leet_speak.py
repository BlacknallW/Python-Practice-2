#Leetspeak
user_input = input("Type a word or phrase. ").upper()

def leet_generator(user_input):
    for words in user_input:
        if words == "A" or words == "E" or words == "G" or words == "I" or words == "O" or words == "S" or words == "T":
            user_input = user_input.replace("A", "4")
            user_input = user_input.replace("E", "3")
            user_input = user_input.replace("G", "6")
            user_input = user_input.replace("I", "1")
            user_input = user_input.replace("O", "0")
            user_input = user_input.replace("S", "5")
            user_input = user_input.replace("T", "7")
        return user_input    

print(leet_generator(user_input))
