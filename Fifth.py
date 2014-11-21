hours = raw_input('Enter Hours: ')
rate = raw_input('Enter Rate: ')
try:
    hours = float(hours)
    rate = float(rate)

    if hours > 40:
        overWork = hours - 40
        pay = (hours - overWork) * rate + overWork * rate * 1.5
    else:
        pay = hours * rate
    print 'Pay: ', pay
except:
    print 'Error, please enter numeric input'