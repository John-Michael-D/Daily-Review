#Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.

#Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(f"The word {w} is {len(w)} letters long")

#Code that modifies a collection while iterating over that same collection can be tricky to get right.
#Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection:

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy: Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy: Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)