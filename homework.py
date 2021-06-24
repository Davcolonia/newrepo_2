# Compute the sum of digits in all numbers from 1 to n
number = int(input('enter number '))
sum = 0 
for i in range(1, number + 1):
    sum = sum + i 
print(sum)




#Find max number from 3 values
num_1 = int(input('enter 1st number '))
num_2 = int(input('enter 2nd number '))
num_3 = int(input('enter 3rd number '))
result = ''
if num_1 > num_2 and num_1 > num_3:
    result = num_1
elif num_2 > num_1 and num_2 > num_3:
    result = num_2
else:
    result = num_3
print(result)

#cound odd and even number
num = int(input("Enter a number: "))
even = 0 
odd = 0 
while num > 0: 
    digit = num % 10
    num = num // 10
    if digit % 2 == 0: 
        even += 1
    else:
        odd += 1
print(even, odd)



#alternately tried to split digits into list to print individial odd, even digits (ex 3062 prints 062 in even and 3 in odd) 

num = int(input("Enter a number: "))
digits = [int(x) for x in str(num)]
even = 0 
odd = 0 
for i in range(digits): 
    if i % 2 == 0:
        even += 1
    else: 
        odd += 1
print(even, odd) 

