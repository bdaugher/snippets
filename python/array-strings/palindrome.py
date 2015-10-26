
# palindrome - a sequence which reads the same forward and backward

# test input
pals = ('a', 'aa', 'ab', 'bb', 'aba', 'abc', 'abba', 'abca', 'zamaz', 'lama', 'doggod', 'goddog', 'godaddy', 'spindrift')

for pal in pals:
    
    # start at beginning, start at end -- break if not equal. 
    # if pointers meet we've found a palindrome
    i = 0
    j = len(pal) - 1
    while i != j and i < j:
        #if pal[0:] == pal[:-1]:
        if pal[i] != pal[j]:
            print pal, 'is not a palindrome'
            break
        i += 1
        j -= 1
    else:
        print pal, "is a palindrome"
                    
# alternatively
# or str == str[::-1]
# str == str.reverse()