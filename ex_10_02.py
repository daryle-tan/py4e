name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        hour = time.split(":")[0]
        count[hour] = count.get(hour, 0) + 1

# Create a list of tuples sorted by hour
sortedHourCount = sorted(count.items())

# Print the counts sorted by hour
for k, v in sortedHourCount:
    print(k, v)
