#If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:
for i in range(5):
    print(i)
print("\n")

#The given end point is never part of the generated sequence; range(10) generates 10 values, the legal indices for items of a sequence of length 10.
#It is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is called the ‘step’):

print(list(range(5, 10)))
print("\n")

print(list(range(0, 10, 3)))
print("\n")

print(list(range(-10, -100, -30)))
print("\n")

#To iterate over the indices of a sequence, you can combine range() and len() as follows:
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

#In most such cases, however, it is convenient to use the enumerate() function.