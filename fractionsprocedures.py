''' This module enhances the fractions class by building procedures which work on two fractions: 
addition, subtraction, multiplication, division '''
from fractions import Fractions 
import math 

def lcm(x, y):
	return math.fabs(x*y)/math.gcd(x,y)

def addfractions(frac1, frac2):
	if ( frac1.isfraction() and frac2.isfraction() ): 
		num1 = frac1.numerator
		den1 = frac1.denominator
		num2 = frac2.numerator
		den2 = frac2.denominator
		cd = lcm(den1, den2)
		fac1 = cd/den1 
		fac2 = cd/den2 
		result = Fractions(fac1*num1+fac2*num2, cd)
		return result
	else:
		print(f"At least one of the input to addfractions is not a fraction , procedure terminated ")
		return -1 


frac1 = Fractions(1, 5)
frac2 = Fractions(2, 3)
fracr = addfractions(frac1 , frac2)
print(f"The sum of") 
frac1.printfraction() 
print("and ")
frac2.printfraction()
print("is ")
fracr.printfraction() 