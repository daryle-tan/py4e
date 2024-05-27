# tuples are immutable where as lists are mutable
# tuples are faster than lists
# tuples are used when data is fixed
y = (1, 2, 3, 4, 5)
print(y)
print(y[2])

(A, B) = (99, 98)

fhand = open('mbox-short.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)

# this is a shorter version of lines 17 - 25
c = {'a': 10, 'b': 1, 'c': 22}
print(sorted([ (v,k) for k,v in c.items()]))