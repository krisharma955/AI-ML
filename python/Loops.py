# while loop

i = 1
while(i <= 5):
    print(i)
    i += 1

k = 5
while(k > 0):
    print(k)
    k -= 1

n = int(input("Enter a number: "))
j = 1
while(j <= 10):
    print(n, "*", j, "=", (n*j))
    j += 1

# for loop

# in -> membership operator
str = "hello"
for var in str:
    print(var)

if('o' in str):
    print(True)

for i in range(1,11):
    print(i)

# if range(n) -> loop runs from 0 to n-1
for i in range(5):
    print(i)

phrase = "artificial intelligence"
cnt = 0
for i in phrase:
    if(i == 'i'): cnt += 1
print(cnt) #no of i

#vowel count
word = "artificial"
count = 0
for ch in word:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'): 
        count += 1
print(count) # vowel count

#range function -> generates sequence
#range(start, STOP, step) -> stop is compulsory
# eg. range(5), here stop = 5, start = 0, step = +1

for i in range(1, 10, 2): # 1 3 5 7 9
    print(i)

#Sum of first N natural numbers
n = 10
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)