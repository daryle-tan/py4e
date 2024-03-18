xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)

# # Counting lines in a file
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

# searching through a file
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
# skipping with continue
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:') :
        continue
    print(line)

# using in to select lines
    fhand = open('mbox-short.txt')
    for line in fhand:
        line = line.rstrip()
        if not '@uct.ac.za' in line:
            continue
        print(line)

# bad file names
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)