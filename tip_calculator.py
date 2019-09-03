# Tip Calculator
# This program calculates tip based on user satisfaction.
bill_amount = float(input("How much was your bill? Leave out the $ sign. "))
satisfaction = input("How satisfied were you with the service? Use the ratings : Good, Fair, or Bad ")

def tip_calculator(bill_amount, satisfaction):
    good_service = bill_amount * .20
    fair_service = bill_amount * .15
    bad_service = bill_amount * .10
    if satisfaction.lower() == "good":
        print(f"Looks like you had a good service! A 20% tip for this bill amount would be ${round(good_service,2)}, bringing your total to ${round(bill_amount + good_service, 2)}. Have a great day!")
    elif satisfaction.lower() == "fair":
        print(f"Looks like your service was just okay. A 15% tip for this bill amount would be ${round(fair_service,2)}, bringing your total to ${round(bill_amount + fair_service, 2)}. Have a great day!") 
    elif satisfaction.lower() == "bad":
        print(f"Oh boy. Looks like you had a bad time. Well, just to be polite, a 10% tip for this bill amount would be ${round(bad_service,2)}, bringing your total to ${round(bill_amount + bad_service, 2)}. Hopefully your day gets better!")
    else:
        print("Please rate your service satisfaction wither either 'Good', 'Fair', or 'Bad'. Any other input will result in an error.")

tip_calculator(bill_amount, satisfaction)