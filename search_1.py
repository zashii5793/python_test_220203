data = [1,2,3,4,5,6,7,8,9]

n = len(data)
key = 7
flg = False

for i in range(n):
    if data[i] == key:
        print("data[{}]が{}です".format(i,key))
        flg = True
        break
    else
    
if flg == False:
    print("存在しない")