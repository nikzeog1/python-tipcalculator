print ("Welcome to the Tip Calculator!")

initial_bill = float(input ("What was the total bill?: £"))
tip = int(input ("What percent(%) tip would you like to give?: "))
number_of_people = int(input ("How many people will split the bill?: "))

tip_percentage = tip / 100
total_tip = initial_bill * tip_percentage
total_bill = initial_bill + total_tip
bill_per_person = round(total_bill / number_of_people, 2)

print (f"\nYour total bill comes to £{total_bill}.\nEach Person can pay: £{bill_per_person}")