#Auto Algorithm V2
#Sept 11, 2018
#Author: Anton

def main():
    #Declare and initialize variables
    #int maritalStatus, age
    maritalStatus = age = 0
    #float rate 
    rate = 0

    #Intro
    print("Welcome to the Santos automobile rate calculator ")
    #Prompt for age
    age = int(input("Please enter your age: " ))
    print()
    #Display a menu to prompt for marital status
    print("1) Married")
    print("2) Single")
    #Prompt for maritalStatus
    martialStatus = int(input("Are you currently married single: "))
    print()
    #nested if statements to determine rate
    if age < 25:
        if maritalStatus == 1:
            rate = 700
        else:
            rate = 800
    if age >= 25:
        if maritalStatus == 1:
            rate = 450
        else:
            rate = 500

    #Display rate to the user
    print("Your rate is", rate)
main()
