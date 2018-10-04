#File name: area of a rectangle program
#Date:September 3, 2018
#Name:Anton Santos

#define rectangle variables
def rectangleArea():
     base = 0.0
     width = 0.0
     hight = 0.0
     answer = 0.0

     print("This program automatically finds the area of any rectancle")
     print()
     base = float(input("Enter the base: "))
     width = float(input("Enter the width: "))
     hight = float(input("Enther the hight: "))

     answer = base * width * hight
     print("The Area is: ", answer)

rectangleArea()
