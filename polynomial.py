''' This is the class of Polynomials in Python. 
It creates the basic polynomial object (defined by an order and its coefficients (a list of real numbers of size (order +1 )))
Then it creates specific functions: getcoeffs , setcoeffs, + , - , multiply (polynomials) , negatepol and buff. 
Extra routines (such as division of polynomials , which is more involved, can be added later)
By Ioan Sapariuc, July, 2021 '''

import math 

class Polynomial():

	def __init__(self, coeffs):
		self.coeffs = coeffs

	#def setceffs(self, order, coeffs):
	#	## Here, remember that coeffs is an (order+1) length list of real numbers
	#	self.coeffs = coeffs

	def getcoeffs(self):
		return self.coeffs 

	def __add__(self, other):
		m = len(self.coeffs)
		n = len(other.coeffs)
		M=max(m,n) 
		coeffr = [None]*M
		coeff1 = self.coeffs
		coeff2 = other.coeffs 

		if (m < M ):
			coeff1 = self.buffcoeffs(M, coeff1)
		elif (n < M): 
			coeff2 = other.buffcoeffs(M, coeff2) 

		for i in range(M):
			coeffr[i] = coeff1[i] +coeff2[i]
		return Polynomial(coeffr)

	def negofpoly(self):
		coeffs = self.coeffs 
		n=len(coeffs)
		coeffr=[None]*n
		for i in range(n):
			coeffr[i] = -coeffs[i]
		return Polynomial(coeffr) 

	def __sub__(self, other):
		return self + other.negofpoly() 


	def buffcoeffs(M , coeffs):
		if (len(coeffs) >= M ):
			print(f" The buffcoeffs method should be called on a list of size < {M} , check size of coeffs ")

		newcoeffs=[0]*M
		n = len(coeffs)
		for i in range(n):
			newcoeffs[i] = coeffs[i] 

		return newcoeffs 

	def printPoly(self):
		order = len(self.coeffs)-1
		if (order >= 1):
			print(self.coeffs)




#ord1 = int(input(" Enter the order of polynomial 1: "))
#ord2 = int(input(" Enter the order of polynomial 2: "))
#coeff1 = []*(ord1+1)
#coeff2 = []*(ord2+1)
#for i in range(ord1+1):
#	coeff1[i] = int(input('''Enter the coefficients of the first polynomial, in order, from 
#		lowest to highest '''))
#	coeff2[i] = int(input('''Enter the coefficients of the second polynomial, in order, from 
#		lowest to highest '''))
coeff1 = [1, 1]
coeff2 = [1, -1]
Poly1 = Polynomial(coeff1)
Poly2 = Polynomial(coeff2)
Polydiff = Poly1 - Poly2 
print('The first polynomial is ')
Poly1.printPoly()
print('The second polynomial is ')
Poly2.printPoly()
print('The negative of polynomial 2 is ')
Poly3 = Poly2.negofpoly()
Poly3.printPoly() 
print('The difference of P1 - P2 is ')
Polydiff.printPoly() 



