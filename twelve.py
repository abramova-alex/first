fruit = 'banana'
index = 0

while index < len(fruit):
    letter = fruit[index]
    print letter
    index = index + 1
print('----')
last = len(fruit) - 1
while last >= 0:
    letter = fruit[last]
    print letter
    last = last - 1
print('----')
for char in fruit:
    print char