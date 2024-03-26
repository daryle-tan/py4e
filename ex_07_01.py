# fh = open('mbox-short.txt')

# for lx in fh:
#     ly = lx.rstrip()
#     print(ly.upper())


# 7.2
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
# extract floating point values from each line
    count = count + 1
    pos = line.find(':')
    line = line[pos+1:]
    line = line.strip()
    fval = float(line)
    tot = tot + fval
    avg = tot / count
# compute the average of those values
print('Average spam confidence:', avg)
