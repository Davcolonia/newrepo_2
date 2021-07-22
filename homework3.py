#1 
text = "Everything is hard before it is easy"
a = []
words = text.split()
for i in range(1,len(words) + 1):
    a.append(words[len(words) -i])
    new = " ".join(a)
print(new)


#2
list1 = ['a', 'b', 'c']
listPerm = [[a, b, c]
            for a in list1
            for b in list1
            for c in list1
            if ( a != b and b != c and a != c )
            ]
print(listPerm)

#3
string = "hello world"
vowels = 0 
consenants = 0 
for i in string:
    if(i == 'a' or i == 'e'  or i == 'i' or i == 'o' or i == 'u'):
        vowels += 1
    else: 
        consenants +=1
print("vowles: ", vowels)
print("consenants: ", consenants)