import math

#For the limit in the definition of the derivative
h = 0.00000001

#Should improve the user input to not rely upon them entering lambda's
#and then calling eval()
#Usage: If f = x * y * z and (x,y,z) = (1,2,3) and the uncertainty's in 
#(x,y,z) are (0.1,0.1,0.1):
#Function: lambda x: x[0] * x[1] * x[2]
#Experimental Values: 1 2 3
#Errors: 0.1 0.1 0.1
def run():
	func = raw_input("Function: ")
	val = inputNumericArray("Experimental Values: ")
	err = inputNumericArray("Errors: ")
	expVal = eval(func)(val)
	errVal = error(eval(func), val, err)
	print "Experimental value: {0}".format(expVal)
	print "Uncertainty: {0}".format(errVal)
	print "Range: ({0},{1})".format((expVal - errVal), (expVal + errVal))

def inputNumericArray(str):
	#http://stackoverflow.com/questions/7845165/how-to-take-input-in-an-array-python
	valStr = raw_input(str).split(' ')
	val = [float(num) for num in valStr]
	return val

#Numeric derivative using the defintion of the derivative
#The n is which variable to take the derivative with respect to (indexd from 0)
def deriv(func, val, n):
	fx = func(val)
	val[n] = val[n] + h
	numerator = func(val) - fx
	return numerator / h

#The numeric value of the gradient vector
def grad(func, val):
	g = []
	for i in range(len(val)):
		g.append(deriv(func, val,i))
	return g

#Like Haskell's zipWith function
def zip(func,a,b):
	l = []
	for i in range(len(a)):
		l.append(func(a[i],b[i]))
	return l

def sumSquares(list):
	sum = 0
	for i in list:
		sum += i ** 2
	return sum

#the error for a function f : Rn -> R
# sqrt(<entries of grad f squared > dot <entries of error in values squared>)
def error(func, val, err):
	return math.sqrt(sumSquares(zip((lambda x,y: x*y), grad(func, val), err)))

#Some common functions as shortcuts
def product(val): return reduce(lambda x,y: x * y, val)
def sum(val): return reduce(lambda x,y: x + y, val)

if __name__ == "__main__":
	run()