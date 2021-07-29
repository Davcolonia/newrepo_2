#1. 
def sel_sort(l):
    for i in range(len(l)-1):
        min_index = i
        for j in range(i+1, len(l)-1):
            if l[j]>l[min_index]:
                min_index = j
        l[min_index], l[i] =  l[i], l[min_index]
        
list = [3,1,41,59,26,53,59]
sel_sort(list)
print(list)


#2
def bubble_sort(list):
    #keep track of up to which index is still unsorted with the unsorted_until_index variable. At the beginning the array is totally unsorted so we initialize this variable to be the final index in the array
    #also create a sorted variable that will allow us to kep track wheter the array is fully sorted
    unsorted_until_index = len(list) - 1
    sorted = False
    #while loop that will last as long as the array is not sorted. sorted=true changes back to false as soon as we make swaps, if no swaps then array is completely sorted
    while not sorted: 
        sorted = True
        for i in range(unsorted_until_index):
            if list[i] > list[i + 1]:
                sorted = False
                list[i+1], list[i] = list[i], list[i+1] 
                # for loop goes from beginning untill index that has not been sorted. in loop we compare every pair of adjacent values, and swap them if there out of order. chang sorted to false if we have to make a swap
                # decrement the unsorted index by 1 since the index it was already pointed to is now sorted
                unsorted_until_index = unsorted_until_index - 1
                
list = [65, 55, 45, 35, 25, 15, 10]
bubble_sort(list)
print(list)

#3
def insertion_sort(array):
    #loop at i=1 through length of array, current index is kept in index variable
    for index in range(1, len(array)):
          #mark a position at current index. then assign the value at that index to the variable temp_value
        position = index
        temp_value = array[index]
     #begin an inner while loop. check whether the value to the left of position is greater than the temp_value, if it is, we use   array[position] = array[position -1] to shift that left value one cell to the right, and decrement position by one. we then check wheter the value to the left of the new position is greater than temp_value and keep repeating untill we find a value that is less then the temp_value 
        while position > 0 and array[position -1] > temp_value:
            array[position -1] =  array[position] 
            position = position -1
        #drop temp value into the gap within the array
        array[position] = temp_value
array = [65, 55, 45, 35, 25, 15, 10]
insertion_sort(array)
print(array)