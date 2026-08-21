a = 3           # a variable declaration
b = 4

# numeric operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)          # modulus - returns a division's remainder
print(a**b)
print(a//b)          #Floor division- truncates fractional remainders down to their floor

#comparison operators
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a == b)
print(a != b)

# truncation and floor methods of math module
import math
print(math.floor(2.5)) #floor and truncation are same for positive results but deviate for positive results like trunc(-2.5) is -2 and floor(-2.5) will be -3 and for // they use floor internally
print(math.trunc(2.5))
print(math.floor(-2.5))
print(math.trunc(-2.5))

#Hex, Octal and Binary  
print(0x01,0o1,0b1)      # prints the base10 value
x = oct(64)              # numbere => digit strings
y = hex(64)
z = bin(64)
int('0x40',16) #converts this string into a decimal value 

# Bitwise Operations
x = 1
x = x << 2 #shift bits left by 2 positions
print(x)
y = x | 3 #Bitwise OR
print(y)
y = x & 3  #Bitwise AND
print(y)
y = x ^ 3 #Bitwise XOR
print(y)



dd