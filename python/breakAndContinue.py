# break

i = 1
while (i <= 10):
    if(i % 6 == 0):
        print("break statement")
        break
    print(i)
    i += 1
print("outside loop..")

# continue

j = 1
while(j <= 10):
    if(j % 3 == 0):
        j += 1 
        continue
    print(j)
    j += 1

k = 1
while(k <= 10):
    if(k % 2 == 0):
        k += 1
        continue
    print(k)
    k += 1