# Strings are immutable, but lists are mutable.
# Lists are enclosed in square brackets.
# Lists can contain any type of object.
# Lists can contain lists.
# Lists can contain a mix of types.
# Lists can be changed.
# Lists can be nested.
# Lists can be indexed.

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

# Lists can be sliced.
t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3]) # ['b', 'c']
print(t[:5]) # ['a', 'b', 'c', 'd', 'e']
print(t[2:]) # ['c', 'd', 'e', 'f']
print(t[:]) # ['a', 'b', 'c', 'd', 'e', 'f']

# Building a list from scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff) # ['book', 99]

# Enter numbers: 3, 9, 5, done
# Average: 5.666666666666667

numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average:', average)

# Lists can be concatenated.
a = [1, 2, 3]
b= [4,5,6]
c = a + b
print(c)
print(b)