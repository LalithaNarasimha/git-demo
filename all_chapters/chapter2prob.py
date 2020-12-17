# %%
#Chapter2
#Ex 2.1
#whats wron in this code

rating = input('enter an integer from 1 to 10')
#rating is a str so input value will be str not integer

# %%
# Ex 2.3
grade = 91

if grade >= 90:
    print(f'your grade {grade} earns a value of A in this course')

# %%
# Ex 2.5

r = 2
pi = 3.14159

diameter = 2*r
circumference = 2*pi*r
area = pi * r**2

print(f'diameter = {diameter}, circumference = {circumference}, area ={area} ')

# %%
#Ex 2.6 number is even or not

num = int(input('enter a number'))
rem = num % 2
if rem == 0:
    print(f'Entered number {num} is even')
else:
    print(f'Entered number {num} is odd')
# %%

# %%
#Ex 2.7 Multiples

num1 = 1024
num2 = 2

if (num1%4 == 0):
    print(f'the number {num1} is a multiple of 4')
else:
    print(f'the number {num1} is not a multiple of 4')

if (num2%10 == 0):
    print(f'the number {num2} is a multiple of 10')
else:
    print(f'the number {num2} is not a multiple of 10')

# %%
#Ex 2.9 to find Ascii value using keyword ord()

sequence = ['B','C','D','b','c','d','0','1','2','$','*','+']

for i in sequence:
    print(f'The ASCII values {i} is {ord(i)}')
# %%
#Ex 2.10 
sum = 0
num1 = int(input('enter the first number '))
num2 = int(input('enter the second number'))
num3 = int(input('enter the third number'))

sum = num1 + num2 +num3
average = sum/3
product = num1*num2*num3
smallest = min(num1,num2,num3)
largest = max(num1,num2,num3)

print(f'the sum of three numbers is {sum}')
print(f'the average is {average}')
print(f'the product is {product}')
print(f'the smallest is {smallest}')
print(f'the largest num is {largest}')
# %%
# Ex 2.11 

num = int(input('enter a five digit number'))
print(num//10000%10,'   ',num//1000%10,'   ',num//100%10,'   ',num//10%10,'   ',num//1%10)


# %%
#Ex 3.9
#numlist = []
digit = 0
num = str(input('enter a five digit number'))
length = len(num)
number = int(num)
base_val = 10
for i in range(length,0,-1):
    div = 10**(i-1)
    digit = number//div%10
    print(digit,end=' ')      #  numlist.append(digit) other way


#print(numlist)
# %%
# Ex 2.12

p = 1000
r = 7
n1 = 10
n2 = 20
n3 = 30

a1 = p*((1 + r)**n1)
print(f'the amount accumulated in {n1} years is {a1:.5f}')
a2 = p*((1 + r)**n2)
print(f'the amount accumulated in {n2} years is {a2:.5f}')
a3 = p*((1 + r)**n3)
print(f'the amount accumulated in {n3} years is {a3:.5f}')

# %%

#Ex 3.10
p = 1000
r = 7

for i in range(1,30,+1):
    a1 = p*((1 + r)**i)
    print(f'the amount accumulated in {i} years is {a1:.5f}')


# %%
#Ex 2.14
# to calculate the Max heart rate and target heart rate

age = int(input('enter your current age '))
heart_rate = 220 - age
print(f'the max heart rate is {heart_rate}')

#target heart rate ranges from 50 - 85%
min_range = 0.50
max_range = 0.85
target_rate1 = min_range * heart_rate
target_rate2 = max_range * heart_rate
print(f'The target heart rate ranges from {target_rate1} to {target_rate2}')

# %%
#Ex 2.15 
# Sorting in Ascending order

num1 = float(input('Enter the first number '))
num2 = float(input('enter the second number '))
num3 = float(input('enter the third number'))
print(f'the entered numbers are {num1},{num2},{num3}')
num = (num1,num2,num3)
sort_num = sorted(num)
print(f'the sorted order is {sort_num}')



# %%
#Ex 3.12 to check number is palindrome
in_num = int(input('enter a number '))

temp = in_num
reverse_num = 0

while(in_num > 0):
    digit = in_num % 10
    reverse_num = reverse_num*10 + digit
    in_num = in_num // 10

if(temp==reverse_num):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
# %%
#Ex 3.13
"""Calculate the factorial of a non-negative integer"""
number = int(input('Enter a non-negative integer: '))

if number < 0:
    print('Number must be non-negative')
else:
    factorial = 1
    
    for i in range(number, 1, -1):
        factorial *= i
    
    print(f'{number}! is {factorial}')
# %%
#Ex 3.15
n = int(input('enter the summing terms'))
fact = 1
res = 0.0

for i in range(0,n,+1):
    if i == 0:
        i = 1

    fact = fact*i
    res += 1/fact

print(f'the approximation for {n} terms is {res}')
# %%
#Ex 3.14
num = int(input('number of terms'))
#pi = 4.0                                                                      
#k = 3.0                                                                       
#est = 1.0                                                                     
#while num > 0:                                                               
#   est = est-(1/k)+1/(k+2)                                                   
#    num = num-1                                                               
#    k+=4 
#print(f'the approximated values of {num} terms is {est}')

sign    = 1.                  # +1. or -1.
pi_by_4 = 1.                  # first term
for div in range(3, 2 * num_terms, 2):   # 3, 5, 7, ...
        sign     = -sign          # flip sign
        pi_by_4 += sign / div     # add next term
# %%
#Ex 3.16 To find largest of two numbers
numlist = []
largest1 = 0
largest2 = 0 
x_count = int(input('How many integers do you want to input'))
for i in range(x_count):
    in_num = int(input('Enter the number '))
    numlist.append(in_num)
print(f'The entered numbers are {numlist} ')

for j in numlist:
    if j > largest1:
        largest2 = largest1
        largest1 = j
    elif j > largest2:
        largest2 = j
   


print(f'The First largest number in the list is {largest1}')
print(f'The Second largest number in the list is {largest2}')

# %%
numlist = []
largest1 = 0
largest2 = 0 
x_count = int(input('How many integers do you want to input'))
for i in range(x_count):
    in_num = int(input('Enter the number '))
    numlist.append(in_num)
print(f'The entered numbers are {numlist} ')

largest1 = max(numlist)
print(f'The First largest number in the list is {largest1}')

#remove largest integer from list
numlist.remove(largest1)

largest2 = max(numlist)
print(f'The Second largest number in the list is {largest2}')
# %%
decimal = 0
i = 0
binary = int(input('Enter a Binary Number'))
binary_num = binary

while(binary !=0 ):
    num = binary%10
    decimal = decimal + (num * pow(2,i))
    binary = binary//10
    i = i + 1

print(f'The Decimal value of binary number {binary_num} is {decimal} ')
# %%
for b in range (1,21,1):
    for p in range (1,21,1):
        for h in range (1,21,1):
            if ((h**2) == ((p**2)+(b**2))):
                print (f'Hypotenuse {h}, Perpendicular {p} and Base {b}.')