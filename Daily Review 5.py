# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

#This example introduces several new features.

#The first line contains a multiple assignment: the variables a and b simultaneously get the new values 0 and 1.
#On the last line this is used again, demonstrating that the expressions on the right-hand side are all evaluated first before any of the assignments take place.
#The right-hand side expressions are evaluated from the left to the right.

#The while loop executes as long as the condition (here: a < 10) remains true.
#In Python, like in C, any non-zero integer value is true; zero is false.
#The condition may also be a string or list value, in fact any sequence; anything with a non-zero length is true, empty sequences are false.
#The test used in the example is a simple comparison.
#The standard comparison operators are written the same as in C: < (less than), > (greater than), == (equal to), <= (less than or equal to), >= (greater than or equal to) and != (not equal to).

#The body of the loop is indented: indentation is Python’s way of grouping statements.
#Note that each line within a basic block must be indented by the same amount.

#The print() function writes the value of the argument(s) it is given.
#It differs from just writing the expression you want to write in the way it handles multiple arguments, floating-point quantities, and strings.
#Strings are printed without quotes, and a space is inserted between items.

#The keyword argument end can be used to avoid the newline after the output, or end the output with a different string:

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b