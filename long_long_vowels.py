#Long Vowels are Long
user_input = input("Type some words or phrases here that use double vowels. ")

def vowel_elongator(user_input):
    if "oo" in user_input or "aa" in user_input or "ee" in user_input or "ii" in user_input or "uu" in user_input:
        user_input = user_input.replace("oo", "ooooo") 
        user_input = user_input.replace("aa", "aaaaa")
        user_input = user_input.replace("ee", "eeeee")
        user_input = user_input.replace("ii", "iiiii")
        user_input = user_input.replace("uu", "uuuuu")
    return user_input

print(vowel_elongator(user_input))