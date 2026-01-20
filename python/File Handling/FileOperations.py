#File Operations - Open, read & close

# #! Open - open() - returns a file object
# #* f = open("file path", "mode")
# #* modes - r(read), w(write)

f = open("sample.txt", "r") #* file object
data1 = f.read() #? reads the complete file
print(data1)
print(type(data1)) # <class 'str'>

data2 = f.readline() #? reads the data line by line
print(data2)

f.close() #* always close the file to save resources

# #! Write - write() - overrides the previous data

w = open("sample.txt", "w")

w.write("123")

w.close()

#! Different Modes
#? r -> reading, default mode
f1 = open("sample.txt")
print(f1.read())
f1.close()

#? w -> writing, truncates file first (override), (creates new file if the file doesn't exists)
f2 = open("sample.txt", "w")
f2.write("Hello")
f2.close()

#? a -> writing, appends at the end (creates new file if the file doesn't exists)
f3 = open("sample.txt", "a")
f3.write(" new text appended\n to the file")
f3.close()

#? x -> creates a new file and opens it for writing
f4 = open("sample2.txt", "x")
f4.write("random text\n added")
f4.close()

#? t -> text mode, b -> binary mode
#* diff combinations -> rt (default), rb, wt, wb ...

#? + -> opens the file for read & write
#* r+ -> we can read & write -> ptr at the start of the file
#* w+ -> we can read & write -> the file will be overridden -> ptr points to the start of an empty file
#* a+ -> we can read & write -> ptr at the end of the file
f5 = open("sample.txt", "r+")
f5.write("ptr points to the start ")
print(f5.read())
f5.close()

f6 = open("sample.txt", "w+")
f6.write("fresh file")
f6.close()

f7 = open("sample.txt", "a+")
f7.write("\n text appended")
f7.close()

