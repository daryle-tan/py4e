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

# Find the top 5 word by frequency
tmp = dict()
newlist = list()
for k,v in many.items():
    tup = (v,k)
    newlist.append(tup)

cool = sorted(newlist, reverse=True)
for v,k in cool[:5]:
    print(k,v)