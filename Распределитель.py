import json

with open('POVT2.json') as f:
    data = json.loads(f.read())
MASS = []
for i in data:
    i[1] = i[1] // 3
    MASS.append([i[0],i[1], i[2]])

with open('POVT3.json','w') as v:
    json.dump(MASS, v)
