def check(number):
    try:
        number = float(number)
    except:
        print 'Invalid input'
    return number

total = 0
count = 0

number = raw_input('Enter a number: ')
if number != 'done':
    number = check(number)
    if isinstance(number, float):
        total += number
        count += 1
        min = number
        max = number
    while True:
        number = raw_input('Enter a number: ')
        if number == 'done':
            break
        number = check(number)
        if isinstance(number, float):
            total += number
            count += 1
            if number > max:
                max = number
            if number < min:
                min = number
average = total / count
print 'total =', total, 'count =', count, 'average =', average, 'min =', min, 'max =', max

