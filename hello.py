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