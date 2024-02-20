import math

welcome = print("Welcome to the financial calculator!")

# Give user two options and prompt input to choose between investment and bond

first_message = """
Investment - to calculate the amount of interest you'll earn on your investment 
Bond - to calculate the amount you'll have to pay on a home loan 

Enter either 'investment' or 'bond' from the menu above to procees: """

# if user has input investment, ask for deposit amount, interest rate (divide by 100 to convert percentage to decimal) and
# number of years and convert all to strings. Ask the user for the type of interest
# simple or compound, using the if-else function. Calculate and print answer, according to input.

while True:
    answer = input(first_message)
    if answer.lower() == "investment":
        deposit_amount = float(input("Please enter the amount of money that you are depositing: £"))
        interest_rate_investment = float(input("Please enter the annual interest rate (%) as a number: ")) / 100
        number_years = float(input("Please enter the number of years you plan on investing: "))
        interest = input("Please enter the type of interest, either 'simple' or 'compound': ")

        if interest == "simple":
            print("The interest you have earnt in total is: £" + str(deposit_amount *(1 + interest_rate_investment * number_years)))
        elif interest == "compound":
            print("The interest you have earnt in total is: £" + str(deposit_amount * math.pow((1+interest_rate_investment), number_years)))
        break
# if the user has input bond, prompt input for the value of the house, interest rate (divide by 100 first and then 12 to work out monthly rate),
# and the number of months they plan to repay in. Calculate and print answer, according to input.

    elif answer.lower() == "bond":
        house_value = float(input("Please enter the present value of the house: "))
        interest_rate_bond = (float(input("Please enter the annual interest rate as a number: ")) / 100) / 12
        number_months = float(input("Please enter the number of months you plan to take, to repay the bond: "))
        print("The amount you will have to repay each month is: £" + float(int((interest_rate_bond * house_value)/(1 -(1 + interest_rate_bond)**(-number_months)))))
        break

# if the user does not type in a valid input, print error message and ask again
    
    else:
        print(("-" * 80) + "\nYou have not chosen one of the options. Please try again\n" + ("-" * 80))
    