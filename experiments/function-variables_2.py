# Explores the life of parameters some more

# Function defs {{{
def test_1():
	"""If parameters are defined once, then the return value should remain the same as
	the initial assignment.

	If the parameters are defined every time they are called, then they should
	change to whatever the new assignment is."""

	c = 0
	def fun(a = c):
		return a

	print("Test 1:")

	c = 1
	print("\t", fun())

	c = 2
	print("\t", fun())

	c = 3
	print("\t", fun())

def test_2():
	"""If function copies the initially-defined parameter, then any changes to that
	copy should not be carried over to the parameter to any further function calls.

	If the function uses the initially-defined parameter itself, then any changes to
	that parameter should be carried across multiple function calls."""

	def fun(b = 0):
		b += 1
		return b # in C, I would have written `return ++b`, but that doesn't work in Python

	print("Test 2:")

	print("\t", fun())
	print("\t", fun())
	print("\t", fun())

def test_3():
	"""Given Test 2, you would expect any changes made to the function's copied object
	to not affect the original value of the parameter--but it does."""

	def fun(c, list_1 = []):
		list_1.append(c)
		return list_1

	print("Test 3:")

	print("\t", fun(1))
	print("\t", fun(2))
	print("\t", fun(3))
# }}}

# Main {{{
test_1()
# Result:
#	0
#	0
#	0

test_2()
# Result:
#	1
#	1
#	1

test_3()
# Result:
#	[1]
#	[1, 2]
#	[1, 2, 3]
# }}}
