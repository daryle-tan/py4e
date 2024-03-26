# Strings are immutable, but lists are mutable.
# Lists are enclosed in square brackets.
# Lists can contain any type of object.
# Lists can contain lists.
# Lists can contain a mix of types.
# Lists can be changed.
# Lists can be nested.
# Lists can be sliced.
# Lists can be indexed.
# Lists can be concatenated.
lotto = [2, 14, 26, 41, 63]
lotto[2] = 28
print(lotto)

things = ["mozzarella", 2, [1, 2, 3], 13.2]
print(len(things))

# range function returns a list of numbers that range from zero to one less than the parameter.
print(range(5))
friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"] 
print(len(friends))
print(list(range(len(friends))))