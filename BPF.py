
import __def__._0_read as r
import __def__._0_transform as tran

def bpf (comp_data):
    print('bpf')

    count_zap = 16

    coef = []
    coef_16_0 = [complex(0.0025,0.0025)]*16
    coef_16_1 = [complex(1,1)]*16
    #print(coef_16_1)

    coef.append(coef_16_1)
    #print('coef', coef)
    coef_16 = []

    coef_16 = [coef_16_1] + [coef_16_0]*14 + [coef_16_1]
    coef_17 = [coef_16_1]*17
    #print("coef_16_count", len(coef_16))

    n_proverka = 1
    coef_res = []
    res3 = []
    for i in comp_data:
        for co in coef_17:
            #print(co)
            n_proverka = 1
            comp_sum = complex()
            for  c in co:
                #print(n_proverka)
                n_proverka +=1
                #print(type(i))
                comp_sum += c
                coef_res.append(c)
            comp_sum *= i
            res3.append(comp_sum)

    #print('res3', res3)
    res3 = tran.in_log_(res3)


    print('end_bpf')
    return res3, coef_res