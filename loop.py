#for loops
for item in 'python':
    print(item)

for item in ['Peter', 'Josh']:
    print(item)
for item in range(5, 10):
    print(item)

prices = [10,20,30]
a,b,c = prices
print(a+b+c)

prices = [20,30,50]
total = 0
for price in prices:
    total += price
print(f"total: {total}")

#nested loops
for X in range(4):
    for Y in range(3):
        print(f' ({X}, {Y})')


numbers = [5,6,3,2,8]
for number in numbers:
    print('x' * number)


names = ['Peter', 'Stephen','Sunday','Yanke','Marquess']
print(names[-2])

numbers = [2,1,4,6,7,9,5]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
