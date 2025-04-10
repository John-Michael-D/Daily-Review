#Python can manipulate str data types as well as int and float types.
#This includes characters, words, names, sentences, etc.
#Str data types can be enclosed in single or double quotes.

print("Green eggs and ham.")
print('My rabbit came back home! :)')
print("1975")

#To quote a quote, we need to escape it with \
#Alternatively, we can use the opposite type of quotation marks

print("\"Four score and seven years ago...\"")
print("'Cry havoc! And let slip the dogs of war!")

#If you don't want characters prefaced by \ to be interpreted as special characters
#You can use raw strings by adding an r before the first quote

print(r"C:\Users\Mobi")

#String literals can span multiple lines. One way is by using triple quotes.
#End of line characters are automatically included in the string
#But it's possible to prevent this by adding a \ at the end of the line.

print("""\
OPTIONS: 
    -Alpha [01]
    -Bravo [02]
    -Charlie [03]
""")

#Strings can be concatenated with the + operator and repeated with the * operator

print(3 * "Pan" + "cakes")

#Two or more string literals next to each other are automatically concatenated.

print("Pan" "cakes")

#If you want to concatenate variables or a variable and a literal, use +:

first = "Pan"
print(first + "cakes")

#Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:

word = "Tantamount"
print(word[0])

#Indices may also be negative numbers, to start counting from the right:

print(word[-1])
print(word[-2])
print(word[-3])

#In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain a substring:

print(word[0:2])
print(word[2:6])

#Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.

print(word[:6])
print(word[:])

#Attempting to use an index that is too large (e.g. word[199]) will result in an error.
#However, out of range slice indexes are handled gracefully when used for slicing:

print(word[0:900])
print(word[900:])

#Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string (e.g. word[2] = "G") results in an error.
#If you need a different string, you should just create a new one.

print("Py" + word[0:6])

#The built-in function len() returns the length of a string:

print(len(word))




