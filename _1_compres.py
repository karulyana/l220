import __def__._0_transform as tran
import __def__._0_read as r

def compression(data, barker):
    c = iter(barker)
    i = iter(data)
    res = []
    n = 0
    Sum = 0
    N_d = len(data)
    while N_d:
        try: # 210
            f = next(c) * next(i)
            Sum += f
        except StopIteration:
            n += 1
            N_d -= 1
            i = iter(data[n:])
            c = iter(barker)
            res.append(Sum)
            Sum = 0
            continue
        except:
            break
    return res


def compression_comp(Data_comp, barker):
    print('compres_comp')
    #barker_comp = trans.in_COMP(barker,barker)
    #print(barker_comp)
    c = iter(barker)
    i = iter(Data_comp)
    res = []
    n = 0
    Sum = complex()
    N_d = len(Data_comp)
    while N_d:
        try: # 210
            f = next(c) * next(i)
            Sum += f
        except StopIteration:
            n += 1
            N_d -= 1
            i = iter(Data_comp[n:])
            c = iter(barker)
            res.append(Sum)
            Sum = 0
            continue
        except:
            break
    print('end_compres')
    return res

def compression_2_comp(data_comp):
    print('compress_2')
    coef_2 = [1,0,1,0,1,0,1,0,1,0,1,0,-24,0,1,0,1,0,1,0,1,0,1,0,1]

    nol_ = complex()
    noly = [nol_]*12

    data_comp = noly + data_comp

    c = iter(coef_2)
    i = iter(data_comp)
    res = []

    n = 0
    sum = complex()
    n_d = len(data_comp)

    while n_d:
        try:
            f = next(c)*next(i)
            sum += f
        except StopIteration:
            n += 1
            n_d -= 1
            i = iter(data_comp[n:])
            c = iter(coef_2)
            res.append(sum)
            sum = complex()
            continue
        except:
            break

    print('end_compr_2')
    return res

def compression_2(data):
    print('compress_2')
    coef_2 = [1,0,1,0,1,0,1,0,1,0,1,0,-24,0,1,0,1,0,1,0,1,0,1,0,1]
    #print(len(coef_2))
    nol_ = 0
    #print(nol_)
    noli = [nol_]*12
    #print(noli)
    data_ = noli + data + noli
    #print(data_)
    c = iter(coef_2)
    i = iter(data_)
    res = []

    n = 0
    sum = 0
    n_d = len(data_)
    while n_d:
        try:
            f = next(c)*next(i)
            sum += f
        except StopIteration:
            n += 1
            n_d -= 1
            i = iter(data_[n:])
            c = iter(coef_2)
            res.append(sum)
            sum = 0
            continue
        except:
            break

    print('end_compr_2')
    return res



