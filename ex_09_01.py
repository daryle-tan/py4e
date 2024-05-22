fname = input('Enter file: ')
if len(fname) < 1:
    fname = 'clown.txt'
hand = open(fname) # open the file

many = dict() # create a dictionary

for line in hand: # iterate through the file
    line = line.rstrip() # remove the white space
    wds = line.split() # split the line into words

    for w in wds: # iterate through the words
       many[w] = many.get(w, 0) + 1 # count the words

print(many)

# Find the word with the largest count
largest = None
for key, value in many.items():
    print(key, value)
    if largest is None or value > largest :
        largest = value
print('The largest word is:', largest)