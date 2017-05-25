from pprint import pprint


import __def__._0_read as r
import __def__._0_transform as tran

def bpf (COMP_DATA):
    print('bpf__')
    #name_fileS = ['WNnk_im_16_128.dat',  'WNnk_re_16_128.dat']
    #name_fileS = ['Coef_DPF13_im.txt', 'Coef_DPF13_re.txt']
    name_fileS = ['w_bartlett_im_.dat','w_bartlett_re_.dat']

    Coef_DPF16_im = [];    Coef_DPF16_re = []

    Coef_DPF13_im = [];    Coef_DPF13_re = []


    Coef = [Coef_DPF16_im,   Coef_DPF16_re]
    r.READ_float_fileS(name_fileS,Coef)
    #Coef = r.READ_float_fileS(name_fileS, Coef)
    #print(Coef[0])
    #r.READ_FILE_strip(name_fileS[1],Coef_DPF16_re)

    #Coef_DPF13_im = Coef_DPF13_im[::2];    Coef_DPF13_re = Coef_DPF13_re[::2]

    COMP_Coef_DPF16 = tran.in_COMP(Coef_DPF16_re, Coef_DPF16_im)

    #pprint(COMP_Coef_DPF16)

    n = 0
    d = 16
    n_16 = 16
    coef = []
    #COMP_data_16z = []
    while n_16:
        n_16 -= 1
        i = COMP_Coef_DPF16[n:d]
        coef.append(i)
        n += 16
        d += 16

    print(len(coef))

    res = []
    pprint(COMP_DATA)

    for i in COMP_DATA:
        for co in coef:
            comp_sum = complex()
            for  c in co:
                #print(type(i))
                comp_sum += c*i
            res.append(comp_sum)
    '''

    for i in comp_data:
        for co in coef_17:
            comp_sum = complex()
            for  c in co:
                comp_sum += c

            comp_sum *= i
            res3.append(comp_sum)'''
    res = tran.in_log_(res)

    MODUL = []
    for i in res:
        M = abs(i)
        MODUL.append(M)

    return res, MODUL

#bpf(complex())