#!/usr/bin/python3from pprint import pprintimport mathdef in_COMP(RE,IM):    print('tran.in_COMP')    COMP_RES = [complex(a, b) for a, b in zip(RE,IM)]    return COMP_RESdef from_COMP_in_RE_IM(COMP_DATA):    print('tran.from_COMP_in_RE_IM')    DATA_RE_IM = []    for i in COMP_DATA:        r = i.real  # r = float.hex(r)        DATA_RE_IM.append(r)        im = i.imag  # im = float.hex(im)        DATA_RE_IM.append(im)    return DATA_RE_IMdef in_log(data):    print('tran.in_log')    res_log = []    #print(data)    for l in data:        while l:            try:                l = 20 * math.log10(abs(l))                break            except:                l = complex(0.000001,0.000001)                l = 20 * math.log10(abs(l))                #print(l)                break        res_log.append(l)    print('end_tran_log')    return res_logdef in_log_(data):    print('tran.in_log')    res_log = []    #print(data)    for l in data:        s = abs(l)        if s == 0.0 or s < 0.0:            l = 0.0        else:            l = 20 * math.log10(abs(l))            if l < 0.0:                l = 0.0        res_log.append(l)    print('end_tran_log')    return res_log'''    ---------TESTING--------'''#re = r.data_test(7)#im = r.data_test(7)[1::2]#in_COMP(re,im)#pprint(in_COMP(re,im))#print(from_COMP_in_RE_IM(in_COMP(re,im)))