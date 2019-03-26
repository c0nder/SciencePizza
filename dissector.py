import unicodedata
from collections import defaultdict
import json
import sys

filename = sys.argv[1]
with open(filename) as f:
	data = json.loads(f.read())

pizza_dict = defaultdict(lambda:[])
no_pizza_dict = defaultdict(lambda:[])
pizzas = 0
not_pizzas = 0

for pizza in data:
	word = ""
	for symbol in pizza["request_text_edit_aware"]:
		if not(unicodedata.category(symbol)[0]=="L"):
			word = word.lower()
			if len(word)>2 and pizza["requester_received_pizza"]:
				if not pizzas+not_pizzas in pizza_dict[word]:
					pizza_dict[word].append(pizzas+not_pizzas)
			elif len(word)>2 and not(pizza["requester_received_pizza"]):
				if not pizzas+not_pizzas in no_pizza_dict[word]:
					no_pizza_dict[word].append(pizzas+not_pizzas)
			word = ""
		else:
			word+=symbol
	if pizza["requester_received_pizza"]:
		pizzas += 1
	else:
		not_pizzas += 1

for word in pizza_dict:
	pizza_dict[word] = len(pizza_dict[word])

for word in no_pizza_dict:
	no_pizza_dict[word] = len(no_pizza_dict[word])

intersection = {}
threshold = 0.15

for word in pizza_dict:
	if word in no_pizza_dict:
		quality = pizza_dict[word]/(no_pizza_dict[word]*pizzas/not_pizzas+pizza_dict[word])
		if not (0.5+threshold>quality>0.5-threshold):
			intersection[word] = quality

with open("dump.json","w") as f:
	f.write(json.dumps(intersection))

for pizza in data:
	test = pizza["request_text_edit_aware"]
	test_dict = defaultdict(lambda:0)
	for symbol in test:
		if not(unicodedata.category(symbol)[0]=="L"):
			word = word.lower()
			if len(word)>2:
				test_dict[word]+=1
			word = ""
		else:
			word+=symbol
	sum = 0
	res_len = 0
	for word in test_dict:
		if word in intersection:
			sum+=intersection[word]
			res_len+=1
	if res_len>0:
		print(str(sum/res_len)+" "+str(pizza["requester_received_pizza"]))
	else:
		print("Unable to decide "+str(pizza["requester_received_pizza"]))