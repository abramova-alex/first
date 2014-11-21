str = 'X-DSPAM-Confidence:  0.8475'
start = str.find(':')
number = str[start+1:]
try:
    number = float(number)
except:
    print 'Something going wrong'
print number

str1 = '     b          '
print str1
str1 = str1.strip(' ')
print str1

str2 = 'er0n'

print str2
str2 = str2.replace('0', 'o')
print str2
