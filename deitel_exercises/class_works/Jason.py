import json
# dump in json and load from json


config_dict = {
    "name": "Samson",
    "age": 30,
    1: "Birthday",
    "wives": [1,2,3,4],
    "boolean": True
}

with open("config_dict", mode="w") as file_obj:
    json.dump(config_dict, file_obj,indent=4, separators=(",",":"))
with open("config_dict", mode="r") as file_obj:
    con = json.load(file_obj)
    print(con)

