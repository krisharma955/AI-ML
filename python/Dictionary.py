#Dictionary -> (key : value) pairs
#* keys -> always unique

dict = {
    "name": "Lando",
    "wdc": 1,
    "number": [4, 1],
    2025: "best one yet!"
}
print(dict)
print(type(dict)) #* dict

#? Accessing values using keys
print(dict["wdc"]) #1
print(dict["name"]) #Lando

#? Dictionaries are mutable & unordered
print(dict["name"]) #Lando
dict["name"] = "Lando Norris"
print(dict["name"]) #Lando Norris

#! Methods
#? dict.keys() -> returns all the keys (can be typecasted in list)
print(dict.keys()) #dict_keys(['name', 'wdc', 'number', 2025])

#? dict.values() -> returns all the values (can be typecasted in list)
print(dict.values()) #dict_values(['Lando Norris', 1, [4, 1], 'best one yet!'])

#? dict.items() -> returns all the key values pairs
print(dict.items()) #dict_items([('name', 'Lando Norris'), ('wdc', 1), ('number', [4, 1]), (2025, 'best one yet!')])

#? dict.get(key) -> returns value acc to a key
#* here, if key is not found -> returns None (dict[key] - this method returns error)
print(dict.get("name")) #Lando Norris
print(dict.get("f1")) #None

#? dict.update(new_item) -> adds a new item(key-value pair) in the dict
dict.update({
    "home": "england"
})
print(dict) #{'name': 'Lando Norris', 'wdc': 1, 'number': [4, 1], 2025: 'best one yet!', 'home': 'england'}