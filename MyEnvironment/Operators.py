# # Operators 

# Arithmetic Operators
a = 7
b =4 
c = a + b
print(c)        # Output :-  11




# Assignment Operators 
a = 4-2
print(a)        # Output :-  2

b = 6
b += 3      # Increment the value of b by 3 and then assign it to b 
b -= 3      # Decrement the value of b by 3 and then assign it to b 
print(b)




# Comparison Operators 
d = 5 < 4 
print(d)        # Output :- False

d = 5 <= 4 
print(d)        # Output :- False

d = 5 >= 4 
print(d)        # Output :- True
 

d = 5!=5 
print(d)        # Output :- False

d = 5==5 
print(d)        # Output :- True




# Logical Operators 
e = True or False           
print(e)                   # Output :-   True

i = True and False
print(i)                   # Output :-   False

# Truth table of 'or
print("True or False is ",True or False)
print("True or True is ",True or False)
print("False or True is ",False or True)
print("False or False is ",False or False)

# Truth table of 'and'
print("True and False is ",True and False)
print("True and True is ",True and False)
print("False and True is ",False and True)
print("False and False is ",False and False)

print(not(False))
print(not(True))


'''

Output :- 

True or False is  True
True or True is  True
False or True is  True
False or False is  False
True and False is  False
True and True is  False
False and True is  False
False and False is  False
True
False

'''




# Bitwise Operators :-  Bitwise operators operate at the bit level, meaning they work directly on binary representations of numbers.  

#  Understanding Binary to Decimal Conversion  :-  

# Step 1 :-  Assign Powers of 2

'''
Each digit in the binary number represents a power of 2, starting from right to left (0th position is the rightmost digit) :-

'''


'''

Binary :    0   1   0   1   1   0  
            ↑   ↑   ↑   ↑   ↑   ↑  
Power :     2⁵  2⁴  2³  2²  2¹  2⁰  
         (32) (16) (8) (4) (2) (1)


'''

# Step 2 :-  Multiply Each Bit by Its Power of 2

'''
Now, you multiply each bit by its corresponding power of 2 and sum them up :- 

'''

'''

= (0 × 2⁵) + (1 × 2⁴) + (0 × 2³) + (1 × 2²) + (1 × 2¹) + (0 × 2⁰)
= (0 × 32) + (1 × 16) + (0 × 8)  + (1 × 4)  + (1 × 2)  + (0 × 1)
= 0 + 16 + 0 + 4 + 2 + 0
= 22


Final Answer :-   010110 (binary) = 22 (decimal) ✅

'''

#  Types :- 

# 1) AND (&) :-  Returns 1 if both bits are 1, otherwise 0.

a = 5            # 0101

b = 3            # 0011

print(a & b)     # Output :-  1 (0001)



# 2) AND (&) :-  Returns 1 if at least one bit is 1.

a = 5            # 0101

b = 3            # 0011

print(a & b)     # Output :-  1 (0001)



# 3) XOR (^) :-  Returns 1 if bits are different, otherwise 0.

a = 5            # 0101

b = 3            # 0011

print(a ^ b)     # Output :-  6 (0110)


# How XOR (^) Works  ? :- 

'''

>> XOR (Exclusive OR) Operator compares corresponding bits of two numbers :- 

   a) If the bits are different, the result is 1.

   b) If the bits are same, the result is 0.

'''

# Step-by-Step Bitwise XOR Calculation :- 

'''

    0101   (Binary of 5)
 ^  0011   (Binary of 3)
 -----------
    0110   (Binary of 6)
    
'''

# Bitwise Comparison :- 

'''

Bit Position	   a(5)	    b(3)	 XOR Result
---------------------------------------------------
1st (Rightmost)	   1	     1	     0 (Same)

2nd         	   0	     1	     1 (Different)

3rd	               1	     0	     1 (Different)

4th (Leftmost)	   0	     0	     0 (Same)


>> Final Binary Output :-  0110 in binary is 6 in decimal, so a ^ b gives 6.

'''



# 4)  NOT (~) :-  Inverts bits (1 → 0, 0 → 1) and gives the two’s complement.

a = 5            # 0101

print(~a)        # Output :-  -6 (2’s complement)


# How  NOT (~)  Works  ?  :-

'''

>>>  The bitwise NOT (~) operator in Python inverts the bits of a number and returns its two's complement (negative value).

'''

# Step 1 :-  Represent the Number in Binary

'''

>>>  We start with a = 5 in 8-bit binary (Python uses more bits internally, but for simplicity, we'll use 8 bits) :- 
      
    00000101   (this is 5 in binary)

'''

# Step 2 :-  Apply the NOT (~) Operator

'''

>>> The NOT operator flips all bits (1 → 0, 0 → 1) :-    

    ~(00000101)  →  11111010

'''

# Step 3 :-  Convert to Decimal Using Two’s Complement

'''

>>> Since the result 11111010 starts with 1, it represents a negative number in two’s complement notation. To find the decimal equivalent :- 


1)  Invert the bits (flip 1s → 0s, 0s → 1s) :-      11111010  →  00000101

2)  Add 1 to get the positive equivalent :-         00000101 + 1 = 00000110  (which is 6 in decimal)


Note :-   We are adding 1 to 00000101 . How does it work column by column ?

>>>  We add from right to left (just like in normal math) :- 

Column	             Bit in 00000101	Bit in 00000001	    Sum       	Carry
------------------------------------------------------------------------------------
1st (rightmost)	       1	              1	                0	         1 (carry)

2nd	                   0                  0	                1            0 (no carry)

3rd	                   1                  0	                1	         0 (no carry)

4th+	            All 0s	            All 0s	            0            0 (no carry)


# Why Did 1 + 1 Become 10 ?

>>>  This follows the same principle as decimal addition :- 

    a) In decimal, when you add 9 + 1, you get 10, and you carry 1 to the next column.

    b) In binary, when you add 1 + 1, you get 10, and you carry 1 to the next column.


3) Put the negative sign :-   -6    
   
   ✅ So ~5 = -6 in Python.


'''



# 5) Left Shift (<<) :-   Shifts bits left by n places, effectively multiplying by 2^n.

a = 5            # 0101

print(a << 1)    # Output :-  10 (1010)



# How Left Shift (<<) Works - Step by Step ? 


# Step 1 :-  Convert 5 to Binary

'''
   00000101   (This is 5 in binary)

'''

# Step 2 :  Shift All Bits Left by 1

'''

>>> Each bit moves one position to the left, and a 0 is added at the rightmost end :- 

   00000101   (5 in binary)
   << 1       (Shift all bits one step left)
   --------
   00001010   (10 in binary)


Original:    00000101   (5)
Shift << 1:  00001010   (10)
                  ↑
                  (Moved left, added 0)

Shift << 2:  00010100   (20)
                 ↑  ↑
                 (Moved left twice, added 0s)

'''


# 6)  Right Shift (>>) :-  Shifts bits right by n places, effectively dividing by 2^n.

a = 5            # 0101

print(a >> 1)    # Output :-  2 (0010)


# How Right Shift (>>) Works - Step by Step ? 
 
# Step 1 :-  Convert 5 to Binary

'''

   00000101   (This is 5 in binary)

'''

# Step 2 :-  Shift All Bits Right by 1

'''

>>> Each bit moves one position to the right, and the leftmost bit is filled based on sign extension (0 for positive numbers, 1 for negative numbers).


   00000101   (5 in binary)
   >> 1       (Shift all bits one step right)
   --------
   00000010   (2 in binary)

   
Original:    00000101   (5)
Shift >> 1:  00000010   (2)
                      ↓
                  (Moved right, leftmost bit filled with 0)

Shift >> 2:  00000001   (1)
                         ↓  ↓
                   (Moved right twice, leftmost bit filled with 0)


'''



# Type() Function
a = 31.2
t = type(a)       # Output :-   class <int>
print(t)




# Type Casting 
a = 32.9
b = complex(a)      
print(b)             # Output :-  (32.9+0j)

print(type(b))       # Output :-  <class 'complex'>




# Input Function
a = input("Enter number 1 :- ")       # 1 
b = input("Enter number 2 :- ")       # 2
print("Number 2 is :- " ,b)
print("Number 1 is :-  " ,a)
print("Sum is ", a +b)               # output 12 as it takes string it concatinates 


a = int(input("Enter number 1 :- ")) # 1 
b = int(input("Enter number 2 :- ")) # 2
print("Number 2 is :- " ,b)
print("Number a is :- " ,a)
print("Sum is ", a +b)               # output 3 




# Integer Division :- 

'''
Integer division returns the floor of the division. That is, the values after the decimal point are discarded.
It is written as ‘//’ in Python 3. So, 1//3 = 0, 2//3 = 0 and 3//3 = 1. Integer values are precisely stored, so they are safe to use in comparisons.
 
'''

# Float Division :- 

'''
Float division returns a floating point approximation of the result of a division.
For example, Only a certain number of values after the decimal can be stored, so it is not possible to store an exact binary representation of many floating point numbers. This sometimes leads to problems when comparing numbers or when rounding.

'''



def main():
    A = int(input("Enter the value for A :- "))
    B = int(input("Enter the value for B :- "))
    # Print seven lines as described above
    print("Sum is :- " , A+B)   
    print("Difference is :- " ,A-B)   
    print("Product is :- " ,A*B)   
    print("Interger Division :- " ,A//B)   
    print("Float Division :- ", A/B)   
    print("Remainder is :- ",A%B)   
    print("Product is :- ", A**B)   
    

if __name__ == '__main__':
    main()


'''

Output :- 

Enter the value for A :- 10
Enter the value for B :- 5
Sum is :-  15
Difference is :-  5
Product is :-  50
Interger Division :-  2
Float Division :-  2.0
Remainder is :-  0
Product is :-  100000

'''




# Identity Operators :- Identity operators in Python are used to compare the memory locations of two objects. They determine whether two variables point to the same object in memory. There are two identity operators :-

# is: Returns True if both variables point to the same object.

a = [1, 2, 3]
b = [1 ,2 ,3]
print(a is b)       # Output :- False
print()
b = a
print(a is b)       # Output :- True 
print()
c = [1, 2, 3]
print(a is b)       # Output: True (both a and b refer to the same object in memory)

print(a is c)       # Output: False (a and c refer to different objects with the same content)



# Immutable Types :-  For small integers and short strings, Python may reuse memory addresses.
# For example :- 
a = 256
b = 256
print(a is b)              # Output: True

print()


# Mutable Types :-  Lists, dictionaries, and other mutable types will have different memory addresses unless explicitly assigned :-

# For example :- 
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is list2)      # Output: False

print()

# is not :-  Returns True if both variables do not point to the same object.
a1 = [1,2,3]
b1 = [1,2,3]
print(a1 is not b1)          # Output :-  True

print()

x = 42
y = 42
z = 43

print(x is not y)           # Output: False (both x and y refer to the same object in memory for small integers)

print(x is not z)           # Output: True (x and z refer to different objects)



# Membership operators :-  Membership Operators in Python are used to test whether a value is found within a sequence (such as a string, list, tuple, set, or dictionary). There are two membership operators :- 

# Use Cases :- 

'''

Strings :-  Checking if a substring exists within a string.

Lists :-  Determining if an element is present in a list.

Tuples :- Identifying if an item exists in a tuple.

Sets :- Verifying membership in a set.

Dictionaries :- Checking if a key exists in a dictionary. 

'''


# in :-  Returns True if the specified value is found in the sequence.

# Example with a list
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)      # Output: True


# Example with a string
text = "Hello, World!"

print("World" in text)         # Output: True


# Example with a tuple
numbers = (1, 2, 3, 4, 5)

print(3 in numbers)            # Output: True


# Example with a set
unique_numbers = {1, 2, 3, 4, 5}

print(5 in unique_numbers)     # Output: True


# Example with a dictionary (checks keys by default)
person = {"name": "Alice", "age": 30}

print("name" in person)      # Output: True

print("Alice" in person)     # Output: False

print()



# not in :-  Returns True if the specified value is not found in the sequence.

# Example with a list
fruits = ["apple", "banana", "cherry"]
print("grape" not in fruits)         # Output :-  True


# Example with a string
text = "Hello, World!"

print("Python" not in text)          # Output :-  True


# Example with a tuple
numbers = (1, 2, 3, 4, 5)

print(6 not in numbers)              # Output :-  True


# Example with a set
unique_numbers = {1, 2, 3, 4, 5}

print(0 not in unique_numbers)       # Output :-  True


# Example with a dictionary (checks keys by default)
person = {"name": "Alice", "age": 30}
print("address" not in person)       # Output :-  True

print("Alice" not in person)         # Output :-  True


