#Sets -> collection of unique elements
#* python set can be mutable & unordered, but it's elements should be immutable

s = {1, 2, 2, 2, 3}
print(s) #{1, 2, 3} #* set contains unique values only
print(type(s)) #set
print(len(s)) #3

#? To create a empty set -> we use a constructor function
empty_set = set()
print(type(empty_set)) #set

#! Methods

#? set.add(val) - Adding elements to set
s.add(4)
print(s) #{1, 2, 3, 4}

#? set.remove(val) - to remove a value from set
s.remove(2)
print(s) #{1, 3, 4}

#? s.clear() - empties the set
#s.clear()
print(s) #set()

#? set.pop() - removes a random val from the set
s.pop()
print(s) #{3, 4}

#? s.union(set2) - returns new union
s1 = {1, 2, 3, 4}
s2 = {4, 6 ,7, 2, 9}
print(s1.union(s2)) #{1, 2, 3, 4, 6, 7, 9}

#? s.intersection(set2) - returns the intersection (common elements)
print(s1.intersection(s2)) #{2, 4}