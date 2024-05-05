eng2sp = dict()
print(eng2sp) # {}

eng2sp['one'] = 'uno'
print(eng2sp) # {'one': 'uno'}

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp['two']) # dos

print('one' in eng2sp) # True

print(len(eng2sp)) # 3

vals = list(eng2sp.values())
print(list(eng2sp.values()))