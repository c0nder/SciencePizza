import json
import collections

with open('train.json') as f:
    data = json.loads(f.read())

    
MASSIV1 = []
MASSIV2 = []
MASSIV = []
MASS = []
NEPOVT = []

c = collections.Counter()
k = collections.Counter()

for pizza in data:
        if pizza["requester_received_pizza"]:
                pizza["request_text_edit_aware"]=pizza["request_text_edit_aware"].lower()
                pizza["request_text_edit_aware"]=pizza["request_text_edit_aware"].replace(',',' ')
                pizza["request_text_edit_aware"]=pizza["request_text_edit_aware"].replace('.',' ')
                pizza["request_text_edit_aware"]=pizza["request_text_edit_aware"].replace('!',' ')
                pizza["request_text_edit_aware"]=pizza["request_text_edit_aware"].replace('?',' ')
                pizza["request_text_edit_aware"]=pizza["request_text_edit_aware"].replace('*',' ')
                pizza["request_text_edit_aware"]=pizza["request_text_edit_aware"].split()
                
                MASSIV1 = MASSIV1 + pizza["request_text_edit_aware"]
        else:
                pizza["request_text_edit_aware"]=pizza["request_text_edit_aware"].lower()
                pizza["request_text_edit_aware"]=pizza["request_text_edit_aware"].replace(',',' ')
                pizza["request_text_edit_aware"]=pizza["request_text_edit_aware"].replace('.',' ')
                pizza["request_text_edit_aware"]=pizza["request_text_edit_aware"].replace('!',' ')
                pizza["request_text_edit_aware"]=pizza["request_text_edit_aware"].replace('?',' ')
                pizza["request_text_edit_aware"]=pizza["request_text_edit_aware"].replace('*',' ')
                pizza["request_text_edit_aware"]=pizza["request_text_edit_aware"].split()
               
                MASSIV2 = MASSIV2 + pizza["request_text_edit_aware"]

                
for word in MASSIV1:
    c[word] += 1
for word in MASSIV2:
    k[word] += 1
    
c = c.most_common()
k = k.most_common()       

for i in c:
    for j in k:
        if j[0] == i[0]:
            MASSIV.append([j[0],j[1],i[1]])

for i in MASSIV:
    i[1] = i[1] // 3
    MASS.append([i[0],i[1],i[2]])

#with open('POVT3.json','w') as v:
 #   json.dump(MASS, v)
            
    
with open('NEPOVT.json','w') as v:
    json.dump(NEPOVT, v)
            
        
