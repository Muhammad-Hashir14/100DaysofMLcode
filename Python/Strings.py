# string methods
string = "python programmming"
print(len(string))
print(string[0])
print(string[:3])
print(string[-1])
print(string[5:])

# Escape
# \"
# \'
# \\
# \n
print("Python \" Programming")
print("Python \' Programming")
print("Python \\ Programming")
print("Python \nProgramming")

# String concatenation
a = "python"
b = "programming"
print(a + " " + b)
print(f"{a} {b}")
print(f"{1+3} {2*2}")

# String methods
string = "python programming"
print(string.upper())
print(string.lower())
print(string.title())
print(string.strip())
print(string.find('h'))
print(string.replace('p','T'))