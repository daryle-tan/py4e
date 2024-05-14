eng2sp = dict()
print(eng2sp) # {}

eng2sp['one'] = 'uno'
print(eng2sp) # {'one': 'uno'}

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp['two']) # dos

print('one' in eng2sp) # True

print(len(eng2sp)) # 3

vals = list(eng2sp.values())
print(list(eng2sp.values()))

word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d) # {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}

# get method
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
print(counts.get('jan', 0)) # 100

word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c, 0) + 1
print(d) # {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}

# you can't look up if a non exisitent key is in a dictinary otherwise you will get an error
# print(counts['csev']) # KeyError: 'csev'
# therefore in order to accomplis this we must use the for in loop
for key in counts:
    if key not in counts:
        counts[key] = 1
    else:
        counts[key] = counts[key] + 1
print(counts) # {'chuck': 2, 'annie': 2, 'jan': 2}