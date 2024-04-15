# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()

# for line in fh:
#     line.rstrip()
#     words = line.split()
#     # print('line:', words)
#     for word in words:
#         if word not in lst:
#             lst.append(word)
#         else:
#             continue
# lst.sort()
# print(lst)

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.startswith("From "):
        words = line.split()
        if len(words) > 2:
            print(words[1])
            count += 1
print("There were", count, "lines in the file with From as the first word")