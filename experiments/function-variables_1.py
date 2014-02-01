# Explores the life of parameters

def fun(a, L=[]):
	L.append(a)
	return L

print(fun(1))
print(fun(2))
print(fun(3))
