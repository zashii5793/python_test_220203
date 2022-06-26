def posi_nega_zero(val):
    if val > 0:
        print(val, "正の数です")
    else:
        print(val, "AA") 
           
posi_nega_zero(-5)

data = [
    [1,2,3,4,5],
    [10,20,30,40,50],
    [100,200,300,400,500,]
]
import random
from re import A
from sys import set_coroutine_origin_tracking_depth
for i in range(10):
    r = random.randint(1, 6)
    print(r)

def average_calc(data[]):
    x = 0
    for i in range(data.length)
        x += data[i]        
    print(x)  
      

# 2-1 平均値を求める
score = [70,80,90,100,110]
total = 0
for i in range(5):
    total = total + score[i]
average = total / 5
print("合計点", total)    
print("平均点", average)

# 2-2 1からｎまで足し合わせる

def addup(n):
    a = 0
    for i in range(1, n+1):
        a = a + i
    return a

# 2-3 99の式を出力する
# 2-4 素数を求める
for i in range(2, 101):
    h = i//2
    f = True
    for j in range(2, h+1):
        if i % j == 0:
                f = False
                break
    if f == True:
        print(i, end=",")
    
# 2-5 nの階乗を求める

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


for i in range (0, 20):
    print(fact(i))

 
##データ構造
# 3-1 スタック

MAX = 5
stack = [0]*MAX
sp = 0
def push(d):
    global sp 
    if sp < MAX:
        stack[sp] = d
        sp = sp + 1
    else:

def pop():
    global sp
    if sp > 0:
        sp = sp -1
        return stack[sp]
    else:
        return None

for i in range(6):
    push(i)
                
# 3-2 キュー
# 3-3 リスト
# 3-4 木
# 3-5 グラフ

##サーチ
# 4-1 線形探索
# 4-2 二分探索
# 4-3 木探索
# 4-4 計算量

##ソート
# 5-1 選択ソート
# 5-2 バブルソート
# 5-3 挿入ソート
# 5-4 クイックソート
# 5-5 マージソート
# 5-6 ヒープソート

##ハッシュ
# 6-1 ハッシュとは
# 6-2 ハッシュ関数
# 6-3 ハッシュテーブル
# 6-4 衝突を回避する

##さまざまなアルゴリズム
# 7-1 ユークリッドの互除法
# 7-2 文字列探索
# 7-3 最短経路

##アルゴリズムを見える化する
# 8-1 n次関数の曲線
# 8-2 フラルタル図形を描く
# 8-3 迷路を解く過程を描く
