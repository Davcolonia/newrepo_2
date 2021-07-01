string2 = 'aabcde'
def unique_chars(st):
    if len(st) > 256:
        return False
    char_set = [False] * 128
    for i in range(0, len(st)):
        val = ord(st[i])
        if char_set[val]: 
            return False
        char_set[val] = True
    return True
string = 'abcd'
string2 = 'aabcd'
print(unique_chars(string))
print(unique_chars(string2)) 






#could not figure out how to deal with odd character string
s = 'bbbbcaaaa'
first = s[:len(s)//2]
second = s[len(s)//2:]
print(second+first)
