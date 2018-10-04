#Software Sales Algorithm
#Author: Anton Santos

def main():
    #Declare and initialize variables and constants
    #int quantity 
    quantity = 0
    #float discount, totalCost 
    discount = 0.0
    totalCost = 0.0
    #const float PACKAGE_COST 
    PACKAGE_COST = 99.0

    #Intro
    print("Welcom to the Santos Sales Program")
    #Prompt for quantity
    quantity = int(input("How much would you like to buy?: "))

    #If statements to calculate discount
    if quantity >= 10 and quantity <= 19:
                     discount = .20
    elif quantity >= 20 and quantity <= 49:
                     discount = .30
    elif quantity >= 50 and quantity <= 99:
                     discount = .40
    elif quantity >= 100:
                     discount = .50
    else:
                     discount = 0.0

    #Calculate totalCost
    totalCost = quantity * PACKAGE_COST *(1 - discount)

    #Display totalCost
    print("Total cost: \t $%0.02f" % totalCost)
main()
