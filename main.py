# Python 1
# Basic Data Types

h = "hello"
w = "world"

print(h,w)
print(h+w)

n1 = 5

# How to concat str with number 
# Typecasting 
multilinestring = """
        str() --> cast to str,
        int() --> cast to int, 
        float() --> cast to float 
    """

print(h+str(n1))

# Formatted strings 
n1 = 5
n2 = 3
res = n1 + n2
out = f"{n1}+{n2}={res}"
print(out)

# Logical operators 
# Code block 
if n1<n2: 
    print("Lesser")
    print("<"*6)
elif n1 == n2:
    print("Equal")
    print('====')
else:
    print("Greater")
    print(">"*len("Greater"))

# blocks in python use indentation 
# used in if statements / function def 

f = 17.4
print(type(f))
