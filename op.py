print("Kindly give values for arithmetic operators")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print(f"Addition of {a} and {b} is:", a + b)
print(f"Subtraction of {a} and {b} is:", a - b)
print(f"Multiplication of {a} and {b} is:", a * b)
print(f"Division of {a} and {b} is:", a / b)
print(f"Modulus of {a} and {b} is:", a % b)
print(f"Exponent of {a} and {b} is:", a ** b)
print(f"Floor Division of {a} and {b} is:", a // b)
print()

# Relational Operators or Comparison Operators
print("Kindly give values for Relational operators")
c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))
print(f"Is {c} == {d}? :", c == d)
print(f"Is {c} != {d}? :", c != d)
print(f"Is {c} >= {d}? :", c >= d)
print(f"Is {c} <= {d}? :", c <= d)
print(f"Is {c} > {d}? :", c > d)
print(f"Is {c} < {d}? :", c < d)
print()

# Assignment Operators
print("Kindly give values for Assignment operators")
e = int(input("Enter the value of e: "))
f = int(input("Enter the value of f: "))
print(f"The value of e is:", e)
print(f"The value of f is:", f)
e += f
print(f"The value of e += f is:", e)
e -= f
print(f"The value of e -= f is:", e)
e *= f
print(f"The value of e *= f is:", e)
e = e / f
print(f"The value of e /= f is:", e)
print()

# Logical Operators
print("Kindly give values for Logical operators")
g = int(input("Enter the value of g: "))
h = int(input("Enter the value of h: "))
i = int(input("Enter the value of i: "))
print(f"Logical AND of {g}>{h} and {h}>{i} is:", (g > h and h > i))
print(f"Logical OR of {g}>{h} or {h}>{i} is:", (g > h or h > i))
print(f"Logical NOT of {g}>{h} is:", (not g > h))
print()

# Membership Operators
print("Checking Membership Operators")
lst = [1, 2, 3, 4, 5]
j = int(input("Enter any number: "))
if j in lst:
    print(f"{j} is available in given list")
else:
    print(f"{j} is not available in the given list")

list1 = [1, 2, 3, 4, 5]
k = int(input("Enter any number: "))
if k not in list1:
    print(f"{k} is not available in given list")
else:
    print(f"{k} is available in the given list")
print()

# Identity Operators
print("Checking identity operators")
# Please give same l and m values to see the use of 'is' operator
l = int(input("Enter value of l: "))
m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))
print("The value of l is", l, "and id of l is:", id(l))
print("The value of m is", m, "and id of m is:", id(m))
print("The value of n is", n, "and id of n is:", id(n))
if l is m:
    print(f"{l} and {m} have same identity")
else:
    print(f"{l} and {m} do not have same identity")
if l is not n:
    print(f"{l} and {n} do not have same identity")
else:
    print(f"{l} and {n} have same identity")
print()

# Bitwise Operators
print("Kindly give values for Bitwise operators")
p = int(input("enter value of p: "))
q = int(input("enter value of q: "))
print(f"Bitwise AND of {p} ,{q} is:", p & q)
print(f"Bitwise OR of {p} ,{q} is:", p | q)
print(f"Bitwise XOR of {p} ,{q} is:", p ^ q)
print(f"Bitwise NOT of {q} is:", ~q)
print(f"Bitwise RIGHT SHIFT of {p} by 2 is:", p >> 2)
print(f"Bitwise LEFT SHIFT of {q} by 2 is:", q << 2)
print()

# Ternary Operator
print("Kindly give values for Ternary operators")
r = int(input("Enter value of r: "))
s = int(input("Enter value of s: "))
print(r, "is minimum") if (r < s) else print(s, "is minimum")
