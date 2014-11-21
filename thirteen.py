word = 'banana'

def count_char(word, ch):
    count = 0
    for letter in word:
        if letter == ch:
            count = count + 1
    return count

print count_char(word, 'n')
print word.count('a')