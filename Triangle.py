import math

print("Hi! This is a program to find out some values of a triangle, hope you enjoy!")
print(" ")

Side_a = input("Length of the side a [cm]: ")
Side_b = input("Length of the side b [cm]: ")
Side_c = input("Length of the side c [cm]: ")

while Side_a == str(Side_a) and Side_b == str(Side_b) and Side_c == str(Side_c):
    try:
        Side_a = float(Side_a)
        Side_b = float(Side_b)
        Side_c = float(Side_c)
        break
    except ValueError:
        print("The sides' length must be a number!")
        exit()
    
else:
    Side_a = float(Side_a)
    Side_b = float(Side_b)
    Side_c = float(Side_c)

if Side_a <= 0 or Side_b <= 0 or Side_c <= 0:
    print("The sides' length can't be less than or equal to zero!")

elif Side_a >= Side_b + Side_c or Side_b >= Side_a + Side_c or Side_c >= Side_a + Side_b and Side_a > 0 and Side_b > 0 and Side_c > 0 and Side_a != str(Side_a) and Side_b != str(Side_b) and Side_c != str(Side_c):
    print("Warning! Remember that in a triangle each side must be smaller than the sum of the others!")

else:
    p = Side_a/2 + Side_b/2 + Side_c/2
    p_a = p - Side_a
    p_b = p - Side_b
    p_c = p - Side_c
    print("Triangle's perimeter:", str(Side_a + Side_b + Side_c), "cm")
    print("Triangle's area:", str(round(math.sqrt(p * p_a * p_b * p_c), 3)), "cm^2")
    print("Height relative to side a:", str(round(math.sqrt(p * p_a * p_b * p_c) * 2 / Side_a, 3)), "cm")
    print("Height relative to side b:", str(round(math.sqrt(p * p_a * p_b * p_c) * 2 / Side_b, 3)), "cm")
    print("Height relative to side c:", str(round(math.sqrt(p * p_a * p_b * p_c) * 2 / Side_c, 3)), "cm")
