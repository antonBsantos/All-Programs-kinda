#File Name:Discussion 2.py
#author: Anton Santos
#Description: This program will calculate one's monthly payment at a banks
#based on how many checks they have made a month.


def main():
    #Define and Initialize Variables
    user_name = ""

    COST_MONTH = 10
    DEPOSIT_FEE_1 = 0.10
    DEPOSIT_FEE_2 = 0.08
    DEPOSIT_FEE_3 = 0.06
    DEPOSIT_FEE_4 = 0.04
    checks_monthly = 0
    total_pay = 0.0

    #Display intro about the program
    print("Welcome to the Santos monthly banking program!")
    print()
    print("In this program we will give you your monthly check cost based on")
    print("how many checks you make each month, with varying discounts.")
    print()

    #ask for the user's name
    user_name = input("What is your name?: ")
    print()

    #prompt for how many checks the user writes each month
    checks_monthly = int(input("How many checks have you deposited this month/each month: "))
    print()

    #thank the user
    # this code here is a contingancy if the user inputs a negative number
    if checks_monthly < 1:
        checks_monthly = int(input("Im sorry, please put in a positive number: "))

    amount1 = checks_monthly * DEPOSIT_FEE_1 + COST_MONTH
    amount2 = checks_monthly * DEPOSIT_FEE_2 + COST_MONTH
    amount3 = checks_monthly * DEPOSIT_FEE_3 + COST_MONTH
    amount4 = checks_monthly * DEPOSIT_FEE_4 + COST_MONTH


    print()
    print("Thank you for your time", user_name)
    print()

    #calculate the banks servIce fee monthly
    if checks_monthly < 20 and checks_monthly >= 0:
        total_pay = amount1
    elif checks_monthly <= 39 and checks_monthly >= 20:
        total_pay = amount2
    elif checks_monthly <= 59 and checks_monthly >= 40:
        total_pay = amount3
    else:
        total_pay = amount4


    #display the service fee per-month
    print("**********************************************")
    print()
    print("Your monthly fee is: $%0.2f\t"% total_pay)
main()
