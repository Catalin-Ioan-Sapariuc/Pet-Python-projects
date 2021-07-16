## this is my Python implementation of 2 non-linear solvers: 
## the user chooses at the beginning one choice of a non-linear solver :
## 1. bisection  or  2. Newton   
## with each solver a few other options are available: 
## TOL (such that abs(f(xs)) < TOL, where xs is the solution found)
## MAXITER (the maximum number of iterations allowed )
## verbose (True if we want to see the steps of the algorithm or False otherwise) 
## INPUT / OUTPUT description for each algorithm: 
## The input for bisection is a, b , ( f(x) is hardcoded now ) , 
## The input for Newton is a, b, and x0 (the starting point) . 
## The output for both algorithms is xs and possibly number of iterations and f(xs) (for verbose see above)

## The output for all algorithms is xs and possibly number of iterations (for verbose see above) 
## by Ioan Sapariuc, July 2021

import math as m 
dash = '-'*80 ## dashes needed later when printing 

def f(x):
	#return x-m.cos(x)
	return m.exp((x-2)**2)-x-2

def fp(x):
	#return 1+m.sin(x)
	return 2*(x-2)*m.exp((x-2)**2)-1

def bisection(a, b, TOL, MAXITER, verbose): 
	if (a > b): 
		print("error: a >b , restart with a < b ")
		return -1
	if (a ==b ):
		if (m.fabs(f(a)) < TOL):
			print(f"The solution is x= {a}")
			return a 
		else: 
			print(f"error: the interval [a,b] is of zero length and {a} is not a solution ")
			return -1
	else:
		if (f(a)*f(b) >0): 
			print(f"f({a})*f({b})>0, no root exist or the root cannot be found through bisection "),
			print(f"algorithm terminated")
			return -1
		else: 
			err = 1.0
			niter = 0
			if (verbose):
				print(dash) 
				print('{:^25s}{:^25s}{:^25s}'.format("Number of iterations", "Solution","f(Solution)"))
				print(dash) 
			while ( err > TOL) :
				xs=(a+b)/2.0  
				if (niter < MAXITER): 
					if ( f(a)*f(xs) <0 ): 
						b=xs 
					else: 
						a=xs 
					err=m.fabs( f(xs) )
					niter=niter+1 
					if (verbose):
						print('{:^25d}{:^25.15f}{:^25.15f}'.format(niter, xs, f(xs)))
				else:
					print(f"Maximum number of iteration reached: number of iterations is {niter}"),
					print("procedure terminated")
					return -1

			print(dash)
			print()
			print(f"The bisection algorithm has terminated in {niter} iterations ")
			return xs 


def Newton(a, b, x0, TOL, MAXITER, verbose): 

	if (a > b): 
		print("error: a >b , restart with a < b ")
		return -1

	if (x0<a or x0>b):
		print("error: x0 in not in [a,b], restart with x0 in [a,b] ")
		return -1

	if (a ==b ):
		if (m.fabs(f(a)) < TOL):
			print(f"The solution is x= {a}")
			return a 
		else: 
			print(f"error: the interval [a,b] is of zero length and {a} is not a solution ")
			return -1
	else:
		err=1.0 
		niter =0 
		if (verbose):
				print(dash) 
				print('{:^25s}{:^25s}{:^25s}'.format("Number of iterations", "Solution","f(Solution)"))
				print(dash) 
		while (err > TOL):
			if (niter < MAXITER):
				d0 = -f(x0)/fp(x0)
				xs = x0 + d0
				x0 = xs 
				err = m.fabs( f(xs) )
				niter = niter+1
				if (verbose):
						print('{:^25d}{:^25.15f}{:^25.15f}'.format(niter, xs, f(xs)))
			else:
				print(f"Maximum number of iteration reached: number of iterations is {niter}"),
				print("procedure terminated")
				return -1

		print(dash)
		print()
		print(f"Newton\'s algorithm has terminated in {niter} iterations ")
		return xs 

## drivers here : 
alg=str(input("Choose a nonlinear solver: for bisection type bisection, for Newton\'s type newton  "))
alg=alg.lower()
if (alg == "bisection"):
	print("bisection started :")	
	print(f"the solution for bisection(0,2,1.e-7,100,False) is",bisection(0,2,1.e-7,100,False))
elif (alg =="newton"):
	print("Newton\'s' started :")	
	print(f"the solution for newtons(0,2,1.e-7,100,True) is",Newton(0,2,1,1.e-7,100,True))
								