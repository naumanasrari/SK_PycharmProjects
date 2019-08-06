import json

data = '{"var1":"harry", "var2":56}'
print(data)
parsed= json.loads(data) # Task1 - json load
print(parsed['var1'])
print(type(parsed))


data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferari'],
    "fridge": ('roti', 540),
    "isbad": False
}

jscomp = json.dumps(data2)
print(jscomp)