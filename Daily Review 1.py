import random

#Expression syntax is straightforward:
#The operators +, -, *, and / can be used to perform arithmetic.
#Parentheses can be used for grouping.

random_a = random.randint(1,100)
random_b = random.randint(1,100)
random_c = random.randint(1,100)
random_d = random.randint(1,100)
random_e = random.randint(1,100)

def addition(a,b):
    sum = a + b
    return sum

def subtraction(a,b):
    difference = a - b
    return difference

def multiplication(a,b):
    product = a * b
    return product

def division(a,b):
    quotient = a / b
    return quotient #Notice how this will always return a floater.

def floor_division(a,b):
    quotient = a // b
    return quotient #Notice how this will always return an integer.

def remainder_division(a,b):
    remainder = a % b
    return remainder

def combination(a,b,c,d,e):
    combo = a + b - c * d / e * (a + b + c + d + e)
    return combo

def exponential(a,b):
    power = a ** b
    return power

sum_result = addition(random_a,random_b)
print(f"\nThe sum of {random_a} and {random_b} is {sum_result}.")

difference_result = subtraction(random_a, random_b)
print(f"\nThe difference between {random_a} and {random_b} is {difference_result}.")

product_result = multiplication(random_a, random_b)
print(f"\nThe product of {random_a} and {random_b} is {product_result}.")

quotient_result = division(random_a,random_b)
print(f"\nThe float quotient of {random_a} divided by {random_b} is {quotient_result}.")

floor_result = floor_division(random_a,random_b)
print(f"\nThe floor quotient of {random_a} divided by {random_b} is {floor_result}.")

remainder_result = remainder_division(random_a,random_b)
print(f"\nThe remainder of {random_a} divided by {random_b} is {remainder_result}.")

combo_result = combination(random_a,random_b,random_c,random_d,random_e)
print(f"\n{random_a} plus {random_b} minus {random_c} multiplied by {random_d} divided by {random_e} multiplied by the sum of {random_a + random_b + random_c +random_d + random_e} is {combo_result}.")

power_result = exponential(random_a,random_b)
print(f"\n{random_a} raised to the power of {random_b} is {power_result}.")