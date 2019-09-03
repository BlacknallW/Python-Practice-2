#Takes user input and returns a story.

name = input("Type in the name of a fictional character. Feel free to use your own name too. ")
business = input("Make up a name for a business, or use the name of your favorite business. Be creative, you tool. ")
adjective = input("What's your favorite adjective? You don't know what I'm going to do with it so be careful. ")
activity = input("What's your favorite thing to do? Rather, what is something you'd rather be doing right now if given the choice? ")


print(f"Here lies {name}, owner of {business}. Ever the {adjective.lower()} person, {name} was unfortunately killed from {activity.lower()}. May thy soul rest in pieces.")