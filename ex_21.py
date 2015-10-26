def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

age = add(30, 5)
height = subtract(78, 8)
weight = multiply(80, 2)
iq = divide(100, 5)

print "Age: %d, Height: %d, Weight: %d, Iq: %d" % (age, height, weight, iq)