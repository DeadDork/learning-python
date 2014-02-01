# Explores scope

integer = 1
print(integer)

def fun():
	integer = 2
	print(integer)

fun()
print(integer)
