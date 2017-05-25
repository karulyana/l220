from pprint import pprint
from math import pi, exp, cos, sin, log10
import math
import numpy as np

N = 17
k = range(N)
n = range(N)
h = 1000
i = np.arange(0,2.0*pi,2.0*pi/h)
Signal = np.outer(i,n)
nk     = np.outer(n,k)
Signal = np.matrix([[x + 1j*y for x,y in zip(a,b)] for a,b in zip(np.cos(Signal),np.sin(Signal))])
c = (2*pi)/N
nk = nk*c
Coef = np.matrix([[x + 1j*y for x,y in zip(a,b)] for a,b in zip(np.cos(nk),np.sin(nk))])

def traj(ai,N):
    diag = np.diag(ai)
    y = np.dot(Signal,np.dot(diag,Coef))
    y = 20 * np.log10(np.abs(y))
    max = np.max(y)*np.ones((h,N))
    min = np.min(y)*np.ones((h,N))
    y = y - max
    return y

ai = [
        0.940306193319157, 0.954130733952570,
        0.966193987895793, 0.976461070265884,
        0.984902269883832, 0.991493145379124,
        0.996214604271025, 0.999052964757309,
        1.0,
        0.999052964757309, 0.996214604271025,
        0.991493145379124, 0.984902269883832,
        0.976461070265884, 0.966193987895793,
        0.954130733952570, 0.940306193319157,
    ]
#traj(ai)

'''
for o in i:
    O = []
    for s in n:
        s *= o
        s = cos(s)+ 1j* sin(s)
        O.append(s)
    Xn.append(O)

    #print('lenXn = ',len(Xn))
    #print((Xn[1]))
    #print((Signal[1,:]))

cnk = []
c = (2*pi)/N
for a in k:
    O = []
    for b in n:
        b *= a
        b *= c
        b = complex(cos(b), sin(b))
        O.append(b)
    cnk.append(O)

    #print('lennk = ',len(cnk))
'''

'''

'''