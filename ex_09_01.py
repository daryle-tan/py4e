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
bigword = None
for key, value in many.items():
    print(key, value)
    if largest is None or value > largest :
        largest = value
        bigword = key
print('The largest word is:', bigword, largest)

counts = dict()
days = {'May': 2, 'Apr': 30, 'Mar': 1, 'Feb': 1, 'jan': 19, 'dec': 1, 'nov': 1, 'oct': 11, 'sept': 11, 'aug': 17, 'jul': 27, 'Jun': 15, 'may': 25}
for day in days:
    counts[days[day]] = counts.get(days[day], 0) + 1
print(counts)

bigDay = None
mostFrequent = None
for day, count in counts.items():
    if mostFrequent is None or count > mostFrequent:
        mostFrequent = count
        bigDay = day
print('Day and Frequency: ', bigDay, mostFrequent)