# Explores the life of parameters some more

# Test 1 {{{
"""If parameters are defined once, then the return value should remain the same as
the initial assignment.

If the parameters are defined every time they are called, then they should
change to whatever the new assignment is."""

c = 0
def fun_1(d = c):
	return d

print("Test 1:")

c = 1
print("\t", fun_1())

c = 2
print("\t", fun_1())

c = 3
print("\t", fun_1())
# }}}

# {{{
"""If function copies the initially-defined parameter, then any changes to that
copy should not be carried over to the parameter to any further function calls.

If the function uses the initially-defined parameter itself, then any changes to
that parameter should be carried across multiple function calls."""

def fun_2(a, b = 0):
	b += a
	return b

print("Test 2:")

print("\t", fun_2(1))
print("\t", fun_2(2))
print("\t", fun_2(3))
# }}}

# {{{
"""Given Test 2, you would expect any changes made to the function's copied object
to not affect the original value of the parameter--but it does."""

def fun_3(a, list_1 = []):
	list_1.append(a)
	return list_1

print("Test 3:")

print("\t", fun_3(1))
print("\t", fun_3(2))
print("\t", fun_3(3))
# }}}
