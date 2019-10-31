# create a list with 10 intergers
lst_1 = [2, 99, 1, 3, 9, 11, 56, 12, 43, 9]
lst_2 = [4, 99, 5, 11, 23, 2]

# find the fifth element in list
print ('Fifth element: {}'.format(lst_1[4]))

# add third and sevenght element in list
print('Addition of 3rd and 7th element: {}'.format(lst_1[2] + lst_1[6]))

# get the last two elements in list
print ('Last two elements: {}'.format(lst_1[-2: ]))

# get the items of all odd numbers
print ('Odd elements: {}'.format([element for element in lst_1 if element % 2 != 0]))

# get the item of all integers


# add 78 to the current list
add_item = lst_1.append(78)
print ('After adding 78: {}'.format([element for element in lst_1]))

# drop seventh item from the list
lst_1.pop(6)
print ('After removing 7th element: {}'.format([element for element in lst_1]))

# create a list from two lists
print ('Create a new list: {}'.format(lst_1 + lst_2))

# find difference between two lists
print ('Difference of lst_1 to lst_2: {}'.format([x for x in lst_1 if x not in lst_2]))
print ('Difference of lst_2 to lst_2: {}'.format([x for x in lst_2 if x not in lst_1]))
# find common points in two lists
print ('Common points: {}'.format([x for x in list(set(lst_1 + lst_2)) if x in lst_1 and x in lst_2]))


#Interview question:
# prepare and record the answer
print(lst_1.sort())
print (sorted(lst_1))
# 1. difference between list and tuples
print ('Lists are mutable whereas tuples are immutable')
# 2. difference between sort and sorted
print ('Sort function sorts the passed list in place and there is no return value where sorted function returns list which is sorted')
