# Practice Problems

#! Word Search
#? search "Python" in sample.txt - if it exists or not and if exists, on which line

data = True
i = 0
word = "solved"
with open("sample.txt", "r") as f:
    while(data):
        i += 1
        data = f.readline()
        if(word in data):
            print(f"{word} found in line: {i}")
            break