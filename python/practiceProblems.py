#Practice Problems

#! Given list of tuples of info (name, subject) and derive required data
info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

#* List all unique subjects
unique_subjects = set()
for tup in info:
    unique_subjects.add(tup[1])
print(unique_subjects)

#* List students who enrolled English
for (name, course) in info:
    if(course == "English"):
        print(name)

#* Create dictionary (student, set of courses) --
dict = {}
for (name, course) in info:
    if(dict.get(name) == None):
        dict.update({name : set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)
