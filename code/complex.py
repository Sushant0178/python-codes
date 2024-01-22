# complex
var_name = 5 + 6j
print(type(var_name))
print(var_name.real)
print(var_name.imag)
######## note -----> real part can be int or float imag. part must be decimal or float #################

# binary the number in the form of 1 and 0

binary = 0b10100  # binary number
print(binary)
print(type(binary))

# octal ----> between 0 to 7

octal = 0o12327  # octal number
print(type(octal))
print(octal)

# convert the decimal in binary

a = bin(12)
print(a)

# convert decimal to octal

num = oct(122)
print(num)

# decimal the number between 0 to 9

decimal = 100
print(type(decimal))
print(decimal)

# num = 10
# print(oct(num))

# hexa decimal ----> 0-9 a-f A-F

ver_name = 0xaA
print(ver_name)


c = 10 + 5j

print(c.real)
print(c.imag)

# complex with binary

c = 0b101 + 5j
print(c)

# complex with octal

c = 0o101 + 5j
print(c)

# complex with hexa-decimal

c = 0x101 + 5j
print(c)

# indexing
a = "rameshwaram"
print(a[4: -1])

cls = 'The Kiran Acadamy'
print(cls[4:9])
