""" This is my class of fractions: called Fractions , as a prototype of rationals
Implemented methods in this class: isproper, isfraction, printfraction simplify , amplify, 
add, subtract, multiply and divide 
More methods can be added as needed. 
By I. Sapariuc July, 2021 """

import math 

def intlcm(x, y):
	return int(math.fabs(x*y))//math.gcd(x,y)

class Fractions(): 

	def __init__(self, numerator, denominator):
		self.numerator = numerator
		self.denominator = denominator

	def isfraction(self):
		m=self.numerator
		n=self.denominator 
		if ( self.isproper() and n !=0 ):
			return True
		else:
			return False 

	def isproper(self): 
		''' This method checks if both numerator and denominator are integers, else 
		we do not have a proper fraction''' 
		m = self.numerator
		n = self.denominator 
		if (isinstance(m,int) and isinstance(n,int)) :
			return True
		if (isinstance(m, float) or isinstance(n, float)): 
			return ( m.is_integer() and n.is_integer() ) 
		return False

	def printfraction(self):
		print(f" {self.numerator} / {self.denominator} ")

	def simplify(self):
		num = self.numerator
		den = self.denominator 
		fact = math.gcd(num, den)
		if (fact != 1 and fact != -1): 
			newnum = num//fact
			newden = den//fact 
			self.numerator = newnum
			self.denominator = newden 
		else:
			print(f" attention in simplify: nothing to simplify through (gcd is 1 or -1) ")
			self.numerator=num
			self.denominator=den 

	def amplify(self, factor):
		if (factor ==0 or factor ==1 or factor ==-1):
			print(f"You cannot amplify with factor {factor} in Fractions.amplify ") 
			print(" procedure terminated ")
			return -1 
		else:
			self.numerator *= factor
			self.denominator *= factor


	def __add__(self, other):
		if ( self.isproper() and other.isproper() ):
			num1 = self.numerator
			den1 = self.denominator
			num2 = other.numerator
			den2 = other.denominator
			cd = intlcm(den1, den2)
			fac1 = cd//den1 
			fac2 = cd//den2 
			#print(f"in add: fac1*num1+fac2*num2 is {fac1*num1+fac2*num2} and den is {cd} " )
			return Fractions(fac1*num1+fac2*num2, cd)
		else:
			print("The first or the second fraction is not proper in add ")

	def negatefr(self):
		if (self.isproper()):
			numerator = self.numerator
			self.numerator = -numerator

	def __sub__(self,other):
		if ( self.isproper() and other.isproper() ):
			num1 = self.numerator
			den1 = self.denominator
			num2 = other.numerator
			den2 = other.denominator
			cd = intlcm(den1, den2)
			fac1 = cd//den1 
			fac2 = cd//den2 
			#print(f"in add: fac1*num1-fac2*num2 is {fac1*num1-fac2*num2} and den is {cd} " )
			return Fractions(fac1*num1-fac2*num2, cd)
		else:
			print("The first or the second fraction is not proper in sub ")	

	def __mul__(self, other): 
		if ( self.isproper() and other.isproper() ):
			num1 = self.numerator
			den1 = self.denominator
			num2 = other.numerator
			den2 = other.denominator
			return Fractions(num1*num2, den1*den2)
		else:
			print("The first or the second fraction is not proper in mul ")

	def __truediv__(self, other): 
		if ( self.isproper() and other.isproper() ):
			num1 = self.numerator
			den1 = self.denominator
			num2 = other.numerator
			den2 = other.denominator
			return Fractions(num1*den2, den1*num2)
		else:
			print("The first or the second fraction is not proper in mul ")


x = int(input("give me the numerator of the first fraction as an integer "))
y = int(input("give me the denominator of the first fraction as an integer "))
a = Fractions(x,y)
#print(f" The fraction {a.numerator} / {a.denominator} is proper returns {a.isproper()} ")
#print(f" The fraction {a.numerator} / {a.denominator} is fraction returns {a.isfraction()}") 
#print(f" The simplified form of {a.numerator} / {a.denominator} is ")
#a.simplify() 
a.printfraction()
x = int(input("give me the numerator of the second fraction as an integer"))
y = int(input("give me the denominator of the second fraction as an integer"))
b=Fractions(x,y)
print('The fraction b is')
b.printfraction()
#b.negatefr()
print("The fraction a / b is ")
c = a / b
c.simplify()
c.printfraction()


