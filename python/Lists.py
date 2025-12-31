#Lists -> mutable sequence of values

marks = [88, 90, 78, 87, 99]
print(marks)

#?indexing
print(marks[0]) #88
print(marks[3]) #87

#?len()
print(len(marks)) #5

#!Mutability of Lists -> values can be modified
print(marks[1]) #90
marks[1] = 93
print(marks[1]) #93

#*Lists can store different values of different data type
list = ["abc", 45, True]
print(type(list)) #list

#!Slicing -> subList (same concept as of Strings)
print(marks[1:4]) #[90, 78, 87]
print(marks[-4:-1]) #[90, 78, 87]

#!Methods in Lists
#?list.append(val) - add one element to the end
nums = [1, 2, 3, 4]
nums.append(5)
print(nums) #[1, 2, 3, 4, 5]

#?list.insert(idx, val) - for adding element in middle of list
l1 = [1,2,3,4,6]
l1.insert(3, 0)
print(l1) #[1, 2, 3, 0, 4, 6]

#?list.sort() - arranges in asc order (sorting)
l2 = [4, 7, 0, 5, 1]
l2.sort()
print(l2) #[0, 1, 4, 5, 7]
#desc order -> list.sort(reverse = True)
l2.sort(reverse=True)
print(l2) #[7, 5, 4, 1, 0]

#?list.reverse() - reverses the order
l3 = [1, 2, 3, 4, 5]
l3.reverse()
print(l3) #[5, 4, 3, 2, 1]

#!Loops with Lists

#?Print all the elements of a list
numbers = [1, 2, 3, 4 ,5, 6]
for i in numbers:
    print(i)

#?Linear Search
key = 4
idx = 0
for i in numbers:
    if(i == key):
        print(idx)
        break
    idx += 1
