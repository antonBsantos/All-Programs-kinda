#Auto Algorithm V1
#Sept 11, 2018
#Author: Anton Santos

def main():
    #Declare and initialize variables
    #int maritalStatus, age
    maritalStatus = age = 0
    #int rate
    rate = 0

    #Intro
    print("Welcome to the Santos automobile rate calculator ")
    #Prompt for age
    age = int(input("Please enter your age: "))
    print()

    #Display a menu to prompt for marital status
    print("1) Married")
    print("2) Single")  

    #Prompt for maritalStatus
    martialStatus = int(input("Are you currently married or single?: "))
    print()

    #multi-way if statements to determine rate
    if age < 25 and maritalStatus == 2:
        rate = 800
    elif age < 25 and maritalStatus == 1:
        rate = 700
    elif age >= 25 and maritalStatus == 2:
        rate = 500
    else:
        rate = 450

    #Display rate to the user
    print("Your rate is", rate)
main()

