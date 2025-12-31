#Tuples -> Immutable sequence of values
#? Similar to Lists, onlt diff is that they are immutable

tup = (1, 2, 3, 4, 5, "abc", False)
print(tup)
print(type(tup)) #tuple (class)
print(len(tup)) #7
print(tup[2]) #3
print(tup[1:5]) #(2, 3, 4, 5)

#Looping in tuple
for i in tup:
    print(i)

#? Sum of all values in a tuple
t1 = (4, 5, 6, 3, 8, 9)
sum = 0
for i in t1:
    sum += i
print(f"Sum of elements in the tuple: {sum}") #Sum of elements in the tuple: 35

# tup[3] = 9 #* Incorrect (Tuples are Immutable)

#! Methods in tuples
#? t.index(val) - returns first occ index
t2 = (3, 4, 5, 4 , 8, 9, 8, 4)
print(t2.index(4)) #1

#? t.count(val) - counts total occ
print(t2.count(8)) #2

#? Single Value tuple
tuple = ("abc",)