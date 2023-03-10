import json
import matplotlib.pyplot as plt

with open('games.json', encoding='utf8') as f:
    games = json.loads(f.   read())

t = []
for i in games:
    y = i['Year']
    t.append(y)
t.sort()
plt.figure(figsize=(20, 5))
plt.hist(t, bins=len(set(t)))
plt.show()

t = []
t1 = []
for i in games:
    t.append(i['Genre'])
    t1.append(i['Year'])
plt.figure(figsize=(20, 5))
plt.bar(t1, t)
plt.show()