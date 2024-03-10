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

# finding the smallest
smallest = None
print('Before')
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After:', smallest)

# 5.1
num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    num = num + 1
    tot = tot + fval
print(tot, num, tot / num)

# 5.2
largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        numF = int(num)
    except:
        print('Invalid input')
        continue
        
    if largest is None and smallest is None:
        largest = numF
        smallest = numF
    elif numF > largest:
            largest = numF
    elif numF < smallest:
            smallest = numF

print('Maximum is', largest)
print('Minimum is', smallest)

# Looping through strings
fruit = 'banana'
for letter in fruit :
    print(letter)

index = 0 
while index < len(fruit) :
    letter = fruit[index]
    print(letter)
    index = index + 1