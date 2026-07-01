import random
list = [random.randint(10,100) for i in range(10)]
list.append(20)
list.insert(3, 20)
print(list)

number = int(input('Enter your number you are looking for: '))

found = False
for i in list:
    if i == number:
        found = True
        break
else:
    print('Value not found')
if found:
    print('Found the value at', list.index(number))
else:
    print('Number not found')