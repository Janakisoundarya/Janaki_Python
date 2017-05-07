import json
with open("D:\Janaki_Python\datatest.json") as jsondata:
    data = json.load(jsondata)
print data, type(data)