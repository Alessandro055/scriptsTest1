#-- Developer: Alessandro Macarie
#-- Helped by: Femi Fisher

import math # We'll need it for some calculations

#------------------------------------------------------------------------------------
#  Introduction

print("Hi! This is a program to find out some values of a triangle, hope you enjoy!")
print(" ")

#------------------------------------------------------------------------------------
#  Creating variables

Side_a, Side_b, Side_c = "", "", "" 
notOk = True

#------------------------------------------------------------------------------------
#  Checking if the variables that the user will give can be turned into numbers

while(notOk):
    try :
        Side_a = input("Length of the side 'a' [cm]: ")
        Side_a = str.replace(Side_a, ",", ".")
        Side_a = float(Side_a)
        print("")
        notOk = False
    except :
        notOk = True
        if Side_a == "":
            print("")
            print("You have to add a number!")
            print("")
        else:
            print("")
            print ("'" + str(Side_a) + "'" + " it's not a number!")
            print("")

notOk = True
while(notOk):
    try :
        Side_b = input("Length of the side 'b' [cm]: ")
        Side_b = str.replace(Side_b, ",", ".")
        Side_b = float(Side_b)
        print("")
        notOk = False
    except :
        notOk = True
        if Side_b == "":
            print("")
            print("You have to add a number!")
            print("")
        else:
            print("")
            print ("'" + str(Side_b) + "'" + " it's not a number!")
            print("")

notOk = True
while(notOk):
    try :
        Side_c = input("Length of the side 'c' [cm]: ")
        Side_c = str.replace(Side_c, ",", ".")
        Side_c = float(Side_c)
        notOk = False
    except :
        notOk = True
        if Side_c == "":
            print("")
            print("You have to add a number!")
            print("")
        else:
            print("")
            print ("'" + str(Side_c) + "'" + " it's not a number!")
            print("")

#------------------------------------------------------------------------------------
#  Checking if the lengths are positive

if Side_a <= 0 or Side_b <= 0 or Side_c <= 0 :
    print("The sides' length can't be less than or equal to zero!")

#------------------------------------------------------------------------------------
#  Checking if the triangle can actually exist

elif Side_a >= Side_b + Side_c or Side_b >= Side_a + Side_c or Side_c >= Side_a + Side_b :
    print("Warning! Remember that in a triangle each side must be smaller than the sum of the others!")

#------------------------------------------------------------------------------------
#  Calculating the perimeter, the area, and the heights relative to each side of the triangle with Heron's formula

else :
    p = Side_a/2 + Side_b/2 + Side_c/2
    p_a = p - Side_a
    p_b = p - Side_b
    p_c = p - Side_c
    
    print("")
    print("-------------------------------------")
    print("")
    print("Triangle's perimeter:", str(round(Side_a + Side_b + Side_c, 3)), "cm")
    print("")
    print("Triangle's area:", str(round(math.sqrt(p * p_a * p_b * p_c), 3)), "cm^2")
    print("")
    print("Height relative to side a:", str(round(math.sqrt(p * p_a * p_b * p_c) * 2 / Side_a, 3)), "cm")
    print("")
    print("Height relative to side b:", str(round(math.sqrt(p * p_a * p_b * p_c) * 2 / Side_b, 3)), "cm")
    print("")
    print("Height relative to side c:", str(round(math.sqrt(p * p_a * p_b * p_c) * 2 / Side_c, 3)), "cm")
    print("")
