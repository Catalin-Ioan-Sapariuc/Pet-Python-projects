""" This is my class of fractions: called Fractions , as a prototype of rationals
Implemented methods in this class: isproper, isfraction, printfraction simplify and amplify.
These will be enhanced in a separate file (module): by add, subtract, multiply, divide 
More methods can be added as needed. 
By I. Sapariuc July, 2021 """

import math 

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
		fac=math.gcd(num, den)
		if (fac != 1 and fac != -1): 
			newnum = num/fac
			newden = den/fac 
		self.numerator = newnum
		self.denominator = newden 

	def amplify(self, factor):
		if (factor ==0 or factor ==1 or factor ==-1):
			print(f"You cannot amplify with factor {factor} in Fractions.amplify ") 
			print(" procedure terminated ")
			return -1 
		else:
			self.numerator *= factor
			self.denominator *= factor

'''
a = Fractions(15,5)
print(f" The fraction {a.numerator} / {a.denominator} is proper returns {a.isproper()} ")
print(f" The fraction {a.numerator} / {a.denominator} is fraction returns {a.isfraction()}") 
print(f" The simplified form of {a.numerator} / {a.denominator} is ")
a.simplify() 
a.printfraction()
print(f" The amplified form of {a.numerator} / {a.denominator} with 5 is ")
a.amplify(5)
a.printfraction()
'''
