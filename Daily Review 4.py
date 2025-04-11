#Python knows a number of compound data types, used to group together other values.
#The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets.
#Lists might contain items of different types, but usually the items all have the same type.

squares = [1,4,9,16,25]
print(f"\nThis list contains the squares of integer values 1 through 5: {squares}.")

#Like strings (and all other built-in sequence types), lists can be indexed and sliced:
print(f"\nThis is the first item in the squares list: {squares[0]}.")
print(f"This is the last item in the squares list: {squares[-1]}.")
print(f"These are the last three items in the squares list: {squares[-3:]}.")

#Lists also support operations like concatenation:
print(f"\nThis is the result of the squares list added with the squares of integer values 6 through 10: {squares + [36,49,64,81,100]}.")

#Unlike strings, which are immutable, lists are a mutable type.
cubes = [1,8,27,65,125]
print(f"\nThis is a list containing the cubes of integer values 1 through 5: {cubes}. Notice anything wrong with it?")
cubes[3] = 64
print(f"This is the corrected version of the cubes list: {cubes}.")

#You can also add items at the end of the list by using the list.append() method:
cubes.append(216)
cubes.append(7 ** 3)
print(f"This is the cubes list with the cubes of integers 6 and 7 added to the end: {cubes}.")

#Simple assignment in Python never copies data.
#When you assign a list to a variable, the variable refers to the existing list.
#Any changes you make to the list through one variable will be seen through all other variables that refer to it.

rgb = ["Red", "Green", "Blue"]
rgba = rgb
rgba.append("Alph")
print(f"\n{rgb}.")

#All slice operations return a new list containing the requested elements.
#This means that the following slice returns a shallow copy of the list:

correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
print(correct_rgba)
print(rgba)

#Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
letters = ["a", "b", "c", "d", "e", "f", "g"]
print(f"\n{letters}")

letters[2:5] = ["C", "D", "E"]
print(letters)

letters[2:5] = []
print(letters)

letters[:] = []
print(letters)

#The built-in len() function also applies to lists:
letters = ["a", "b", "c", "d", "e", "f", "g"]
letters_count = len(letters)
print(f"\nThere were {letters_count} letters in the original letters list.")

#It is possible to nest lists (create lists containing other lists), for example:
a = ["a", "b", "c"]
n = [1, 2, 3]
x = [a, n]
print(f"\n{x}")
print(f"{x[0]}")
print(f"{x[0][1]}")