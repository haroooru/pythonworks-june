import json

f = open("sample1.json", "r")

content = json.load(f)

print(content[0])

f.close()