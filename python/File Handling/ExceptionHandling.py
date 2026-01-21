# Exception Handling

#! try, except, else and finally
#? finally - block of code which gets executed irrespective of errors thrown or not

try:
    x = int(input("enter x: "))
    ans = 10 / x
except ZeroDivisionError:
    print("Division by 0 is not allowed!")
except ValueError:
    print("Invalid input!")
else:
    print(f"Ans: {ans}")
finally:
    print("End of Program")

try:
    list = [1, 2, 3]
    ans = list[2]
except Exception:
    print("Out of bounds!")
else:
    print(ans)