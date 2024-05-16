# 14/05/2024
# JSON parsing and understanding
# 1) How many keys (countries) in dictionary(json file)?
'''import json
with open('default_1.json') as file:
    json_default = json.load(file)

print(json_default) # Normal print
print(json_default['alb']['dl']['supportedSide'])
print(json_default.keys()) # keys print(EX:alb est)
print(len(json_default.keys())) # keys count print 118 keys
print(json_default['alb']) # print in full of alb 
print(len(json_default['alb'])) #print in alb len(Example:2(id,dl))
a = json_default['alb']'''

# 2) How many number of documents in lex config(json file)?
# Total documents count code
'''import json
with open('default_1.json') as file:
    json_default = json.load(file)

count = 0

for i in json_default:
    keys = list(json_default[i].keys())
    print(keys)
    #print(keys)
    total= len(keys)
    count = count+total
print(count) # 248 documents'''

# 15/05/2024
# JSON access, update, saving
# 1) Add “back” to side supported list in all countries with name starting with A
import json
with open('default_1.json') as file:
    json_default = json.load(file)
for country in json_default:
    if country[0] == 'a':
        for document in json_default[country]:
            json_default [country] [document] ['supportedSide'].append("back")
print(json_default['alb'])

# 2) Add a new country “sww” which has same configuration as “alb” and save the json as a new text file 
'''import json
with open('default_1.json') as file:
    json_default = json.load(file)

# Create a new country entry for "sww" with the same configuration as "alb"
json_default['sww'] = json_default['alb'].copy()

# Sort the JSON data by country name
sorted_json_default = dict(sorted(json_default.items()))

# Convert the dictionary to a string representation with indentation for readability
# json.dumps - convert a Python object into a JSON string.
json_str = json.dumps(sorted_json_default, indent=4)

# Save the modified JSON data as text to a new file
with open('new_default.txt', 'w') as file:
    file.write(json_str)

print(sorted_json_default.keys()) # keys print(EX:alb est)
print(len(sorted_json_default.keys())) # keys count print 119 keys'''