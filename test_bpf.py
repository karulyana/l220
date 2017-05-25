import math

a = [0,0,0,0,0,0,0,0,0,10,0,0,0,0,0,0,0]
print('a_count = ', len(a))

k = range(16)
n = range(16)
#for a,x in zip(a,k):
#    pass
    #print(a,x)
w = []
for k_i in k:
    for n_i in n:
        try:
            w_i = math.exp((2*math.pi*k_i)/n_i)
        except ZeroDivisionError:
            w_i = 0
        #print(k_i,n_i, "w_i = ", w_i)
        w.append(w_i)

wn = []
for n_i in n:
    try:
        wn_i = math.exp((2*math.pi*1.0)/n_i)
    except ZeroDivisionError:
        wn_i = 0
    wn.append(wn_i)


wnk = []

for k_i in k:
    for wn_i in wn:
        wnk.append(wn_i**k_i)
        #print('k_i:',k_i, 'wn_i:', wn_i)

print('wn:', wn)
print('count_wn:',len(wn))
print('w:', w)
print('count_w:',len(w))
print('wnk:', wnk)
print('count_wnk:',len(wnk))
if wnk == w:
    print('True')
else:
    print('False')



c = iter(w)
i = iter(a)
res = []
n = 0
Sum = 0
N_d = len(w)
while N_d:
    try: # 210
        f = next(c) * next(i)
        Sum += f
    except StopIteration:
            n += 1
            N_d -= 1
            i = iter(a)
            res.append(Sum)
            Sum = 0
            continue
    except:
            break

print(res)

A_wn0 = []

import matplotlib.pyplot as plt

plt.plot(wnk, 'b-')

#plt.show()