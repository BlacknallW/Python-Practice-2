# Tip Calculator + Split Bill
#This program takes user input to calculate tip amount and splits checks evenly.

bill_amount = round(float(input("How much was your bill? Leave out the $ sign. ")),2)
satisfaction = input("How satisfied were you with the service? Use the ratings : Good, Fair, or Bad ")
party_size = int(input("How many ways is this check being split? "))

def tip_calculator(bill_amount, satisfaction, party_size):
    good_service = round(bill_amount * .20, 2)
    fair_service = round(bill_amount * .15, 2)
    bad_service = round(bill_amount * .10, 2)
    if satisfaction.lower() == "good":
        print(f"Looks like you had a good service! A 20% tip for this bill amount would be ${good_service}, bringing your total to ${bill_amount + good_service}. In your party of {party_size}, each person will pay ${round((bill_amount + good_service) / party_size, 2)}. Have a great day!")
    elif satisfaction.lower() == "fair":
        print(f"Looks like your service was just okay. A 15% tip for this bill amount would be ${fair_service}, bringing your total to ${bill_amount + fair_service}. In your party of {party_size}, each person will pay ${round((bill_amount + fair_service) / party_size, 2)}. Have a great day!") 
    elif satisfaction.lower() == "bad":
        print(f"Oh boy. Looks like you had a bad time. Well, just to be polite, a 10% tip for this bill amount would be ${bad_service}, bringing your total to ${bill_amount + bad_service}. In your party of {party_size}, each person will pay ${round((bill_amount + bad_service) / party_size, 2)}. Hopefully your day gets better!")
    else:
        print("Please rate your service satisfaction wither either 'Good', 'Fair', or 'Bad'. Any other input will result in an error.")

tip_calculator(bill_amount, satisfaction, party_size)