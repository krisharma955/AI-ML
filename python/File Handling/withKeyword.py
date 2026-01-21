# with Keyword

#! When we open file using with keyword (format), it automatically closes the file when all the operations are done

with open("sample.txt", "r") as f:
    data = f.read()
    print(len(data))
