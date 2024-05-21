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

# counting pattern
counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

# Two iteration variables
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key,value in counts.items():
    print(key, value)

# histogram and finding the most common word
name = input('Enter file:')
handle = open(name)

counts = dict() # create a dictionary
for line in handle: # iterate through the file
    words = line.split() # split the line into a list of words
    for word in words: # iterate through the list of words
        counts[word] = counts.get(word, 0) + 1 # create a histogram of the words

bigcount = None
bigword = None
for word,count in counts.items(): # iterate through the dictionary
    if bigcount is None or count > bigcount: # if the count is greater than the bigcount
        bigword = word # assign the word to bigword
        bigcount = count # assign the count to bigcount