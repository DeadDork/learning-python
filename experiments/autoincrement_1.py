# Interesting: none of these values autoincremented.

b = 3
print("Plain print:\n", "\tb = ", b, "(expected value = 3)")

++b
print("Print outside autoincrement:\n", "\tb = ", b, "(expected value = 4)")

print("Print inside autoincrement:\n", "\tb = ", ++b, "(expected value = 5)")
