## this code solves the quadratic equation : a*x^2+b*x+c=0
## for modularization, we solve the problem in a function: quadraticeqsolver(a,b,c) , which returns (as a list)
## the solution of the quadratic equation a*x^2+b*x+c=0
## a, b and c are inputted by the user, they could be hard coded as well

## by Ioan Sapariuc, July 5, 2021 

import math as m 

##a = 1. 
##b=2. 
##c=1. 


def quadraticeqsolver(a, b, c):

	solution = [] 
	if (a ==0):
		print(f"Since a is {a}, the equation is linear, not quadratic, therefore no solution will be provided") 
	else:
		d = b**2-4.*a*c 
		if ( d > 0 ):
			x1 = (-b + m.sqrt(d))/(2*a)
			x2 = (-b - m.sqrt(d))/(2*a)
			solution = [ x1, x2]
			print(f"The quadratic equation: {a} x^2 +{b} x + {c} =0 has two real distinct roots ")
		elif (d ==0 ):
			xs = (-b)/(2*a)
			print(f"The quadratic equation: {a} x^2 +{b} x + {c} =0 has a double root ")
			solution = [xs] 
		else: 
			real = (-b)/(2*a)
			imaginary = m.sqrt(-d)/(2*a)
			print(f"The quadratic equation {a} x^2 +{b} x + {c} =0 has two complex roots: {real} + i *{imaginary} "),
			print(f" and {real} - i *{imaginary}; the real and the imaginary parts of the solution are returned "),
			print(f"in this order: [real , imaginary]") 
			solution = [real , imaginary] 
	return solution 

			
print(f"This code solves the quadratic equation a*x^2 +b*x + c =0 for any values of a, b and c")
a=float(input("Enter the value of a for your quadratic equation "))
b=float(input("Enter the value of b for your quadratic equation "))
c=float(input("Enter the value of c for your quadratic equation "))	
solution = quadraticeqsolver(a,b,c)
print(f" The solution of the quadratic equation  {a} x^2 +{b} x + {c} =0 is " ),
print(solution)


