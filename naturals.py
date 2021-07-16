""" This is my class of natural numbers: called Naturals , as a child class of Integers. 
On this class I implement:
isnatural (to check is a number is natural or not), 
isprime (to check if it is prime) and 
proper_prime_factors (to list all its proper prime factors), 
More methods can be added as needed. 
By I. Sapariuc July, 2021 """

import math 

class Integers:
	''' This class is a parent of Naturals '''
	def __init__(self, value):
		self.value = value 

	def isinteger(self):
		n = self.value
		if isinstance(n,int):
			return True
		if isinstance(n,float):
			return n.is_integer()
		return False


class Naturals(Integers): 

	def __init__(self,value):
		super().__init__(value)

	def isnatural(self):
		if ( self.isinteger() and self.value >=0 ):
			return True
		else:
			return False 

	def isprime(self):
		number=self.value
		limit = int(math.sqrt(number)) 
		checkifprime = True 

		for i in range(2,limit):
			if (number%i ==0):
				checkifprime =  False 
				break
		return checkifprime 

	def list_of_proper_divisors(self):
		number = self.value
		listofdiv =[] 
		limit = int(math.sqrt(number))
		for i in range(2, number-1):
			if (number%i ==0):
				listofdiv.append(i) 
		return listofdiv 


n=Naturals(15) 
m=Naturals(18)
print(f" The gcd: ( {n.value} , {m.value} ) = {math.gcd(m.value, n.value)} ")



