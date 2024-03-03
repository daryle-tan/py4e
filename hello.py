greeting = "Hello, World!"
print(greeting)

n = 5

while n > 0:
    print(n)
    n = n - 1
print("Blastoff!")

# definite loops
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy Birthday:', friend)
print('Done!')

# find the largest number
largest = -1
print('Before:', largest)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest:
        largest = the_num
    print(largest, the_num)
print('After:', largest)

# find the average
count = 0
sum = 0
print('Before:', count, sum)
for value in [9,41,12,3,74,15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After:', count, sum, sum / count)