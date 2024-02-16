print("Welcome to the tip calculator!")
#Ask the total bill amount
total_bill = input("What was the total bill?\n")
#Ask the percentage tip that will be given
tip_percentage = input("What percentage tip would you like to give? 0, 10, 12, or 15?\n")
#Ask how many people will split the bill
people = input("How many people to split the bill?\n")
#Create variable for the computed tip percentage
int_tip_percentage = int(tip_percentage)
int_tip_percentage_divided = 1 + int_tip_percentage / 100
#Compute the bill per person including the tip
payment = int(total_bill) / int(people) * float(int_tip_percentage_divided)
#Round the amount of bill to 2 decimal places
rounded_payment = "{:.2f}".format(payment)
print(f"Each person should pay ${rounded_payment}.")
#Ask the amount of money available per person
contribution = input("How much is your money?\n")
#Compute the exact change
int_contribution = int(contribution)
change = int_contribution - float(rounded_payment)
final_amount = "{:.2f}".format(change)
print(f"Your exact change is ${final_amount}.")