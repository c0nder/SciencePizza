import json
import time
import sys
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

filename = sys.argv[1]

with open(filename) as f:
	data = json.loads(f.read())

days = {0:0,1:0,2:0,3:0,4:0,5:0,6:0}
pizzas = 0
age = {}
not_pizzas = 0
not_age = {}
for pizza in data:
	if pizza["requester_received_pizza"]:
		pizzas+=1
		temp = round(pizza["requester_account_age_in_days_at_request"],-1)
		if not (temp in age.keys()):
			age[temp] = 0
		age[temp]+=1
	else:
		not_pizzas+=1
		temp = round(pizza["requester_account_age_in_days_at_request"],-1)
		if not (temp in not_age.keys()):
			not_age[temp] = 0
		not_age[temp]+=1

x = []
y = []

maxn = sum(i[1] for i in age.items())
for key in sorted(age.items()):
	if 1500>key[0]>0:
		x.append(key[0])
		y.append(key[1]/maxn)
x = np.array(x)
y = np.array(y)
x_smooth = np.linspace(x.min(), x.max(), 100000)
y_smooth = spline(x, y, x_smooth)
plt.plot(x_smooth,y_smooth)
x = []
y = []
maxn = sum(i[1] for i in not_age.items())
for key in sorted(not_age.items()):
	if 1500>key[0]>0:
		x.append(key[0])
		y.append(key[1]/maxn)
x = np.array(x)
y = np.array(y)
x_smooth = np.linspace(x.min(), x.max(), 100000)
y_smooth = spline(x, y, x_smooth)
plt.plot(x_smooth,y_smooth)
plt.show()