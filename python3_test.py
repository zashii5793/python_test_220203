list_a=['dog','cat','tiger','horse','monkey']
for s in list_a[:]:
    if len(s)==5:
        list_a.append(s)
print(list_a)

for i in range(0,16,4):
    print(i,end=",")
    