# JSON - Javascript object notation

import json

#! Dealing with Json / Python Strings
#? json.loads() - Json String to Python Object
#? json.dumps() - Python Obj to Json String 

# json_str = '{"name": "Lando", "isDriver": null}' 
# print(type(json_str)) #str

# py_obj = json.loads(json_str)
# print(type(py_obj)) #dict
# print(py_obj)

# print(json.dumps(py_obj)) #* reverse - py obj to json string

#! Dealing with Json / Python files
#? json.load() - reading a json file
#? json.dump() - writing in a json file

# with open("data.json", "r") as f:
#     py_obj = json.load(f)
#     print(py_obj)
#     print(type(py_obj)) #<class 'dict'>

data = {
    "name": "Krish",
    "job": None,
    "age": 20
}

with open("data.json", "w") as x:
    json.dump(data, x, indent=4, sort_keys=True)



