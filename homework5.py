list = [7,3,5,6,4,10,3,2]
even_list = []
odd_list = []
def sort(list1):
    for i in list1:
        if i % 2 == 0:
            even_list.append(i)
        else: 
            odd_list.append(i)
    even_list.sort(), odd_list.sort()
    even_list.extend(odd_list)
    return even_list
print(sort(list))






def inc_one(arr): 
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i -1] += 1
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)
    return arr

test = [9,9]
print(test)
print(inc_one(test))
        
