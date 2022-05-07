from sys import float_repr_style


data = [1,2,6,12,20,25,32,48,50,57,72,80,93,100]
key = int(input("探す値を入力してください"))

left = 0
right = len(data)-1
flg = False

while left <= right:
    mid = (left + right)//2
    print("L={} M={} R={}".format(left, mid, right))
    if data[mid] == key:
        print("data[{}]が{}です".format(mid, key))
        flg = True
        break
    if data[mid] < key:
        left = mid + 1
    else:
        right = mid - 1
        
if flg == False:
    print("その値は見つかりませんでした")            