import json
import email.utils
import matplotlib.pyplot as plt


with open('pract3/table.json', encoding='utf8') as f:
    table = json.loads(f.read())  # Таблица решений задач

with open('pract3/failed.json', encoding='utf8') as f:
    failed = json.loads(f.read())  # Данные по ошибкам

with open('pract3/messages.json', encoding='utf8') as f:
    messages = json.loads(f.read())  # Полученные сообщения

t = []
for i in messages:
    stra = i["date"]            #2
    stra = stra[:3]
    t.append(stra)
t.sort()
plt.plot(t)
plt.show()

messages = [(m['subj'].upper(), email.utils.parsedate(m['date'])) for m in messages]

t = []
for i in messages:
    tup = i[1][3:5]             #1
    t.append(tup[0]+tup[1]/60)
t.sort()
plt.hist(t)
plt.show()

t = []
for i in messages:
    stra = i[0][:3]              #3
    t.append(stra)
t.sort()
plt.figure(figsize=(30, 10))
plt.hist(t, bins=len(set(t)))
plt.show()

t = []
for i in table['data']:
    if i[3] == 1:
        t.append(i[0])           #4
t.sort()
plt.figure(figsize=(30, 10))
plt.hist(t, bins=len(set(t)))
plt.show()

t = dict()
t1 = dict()
for i in table['data']:
    if i[2] in t.keys():
        t[i[2]] += 1
    t.setdefault(i[2], 1)        #5
    t1.setdefault(i[2], 1)
    if i[3] == 1:
        t1[i[2]] += 1
t3 = dict()
for key in t.keys():
    t3[key] = t1[key] / t[key]
plt.hist(t3, bins=14)
plt.show()

t = []
for i in failed:
    if failed[i][1] is not None:
        lis = failed[i][1]       #6
    else:
        lis = 'None'
    t.append(lis)
t.sort()
plt.figure(figsize=(10, 100))
plt.plot(t)
plt.show()