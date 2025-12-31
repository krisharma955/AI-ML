#Strings -> Sequence of characters

word = "python"

#len() - to get length of the string
print(len(word)) #6

#Concatenation -> Addition of Strings
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2) #Hello World

#Accessing elements - indexes
str = "formula1"
print(str[2]) #r
print(str[0]) #f
for i in str:
    print(i)

#Strings are immutable

#Slicing in Strins - to create substring
#format -> str[startIdx : stopIdx] & stopIdx not included

a = "youtube"
print(a[3:6]) #tub
print(a[-4:-1]) #tub
print(a[2:]) #utube
print(a[:]) #youtube

#startIdx default value = 0, endIdx def = len(string)

#String Formatting - dynamic strings
#format & f_strings(mostly used)

#normal formatting
a = 3
b = 7
sum = 10
print("Sum is {}".format(sum)) #Sum is 10
print("Sum of {} & {} is {}".format(a, b, sum)) #Sum is 3 & 7 is 10
print("Language is {}".format("python")) #Language is python

#index based formatting
print("Sum of {1} & {0} is {2}".format(a, b, sum)) #Sum is 7 & 3 is 10

#value based formatting
print("Values of vars {a} & {b}".format(a = 1, b = 6)) #Values of vars 1 & 6

#f_strings - mostly used
print(f"sum is {a} & {b} is {a+b}") #sum is 3 & 7 is 10