#Work or Sleep In?
#Requests integer for day of week, returns whether user should go to work.

day = int(input("Day (0-6)?"))
week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def work_or_not(day):
    if day == 0 or day == 6:
        print("Don't worry, go back to bed.")
    else:
        print("Get up and go to work!")

work_or_not(day) 