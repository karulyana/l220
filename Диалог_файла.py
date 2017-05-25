import __def__._0_read as r
import __def__._0_transform as tran
import __def__._1_compres as sg

import __def__.bpf__ as BPF

import math
from pprint import pprint

barker = r.barker_('p13')
data_test = r.data_test(13)

def FileDialog(fileName):
    print('FileDialog')
    d = r.READ_FILE_zoo(fileName)
    data1 = tran.from_COMP_in_RE_IM(d[0])[0::2]
    data2 = tran.from_COMP_in_RE_IM(d[1])[1::2]

    dialog1 = data1
    plot1 = [data1, data2]

    r1 = sg.compression_comp(data1, barker)
    r2 = sg.compression_comp(data2, barker)
    r1_ = tran.from_COMP_in_RE_IM(r1)[0::2]
    r2_ = tran.from_COMP_in_RE_IM(r2)[0::2]

    dialog2 = r1
    plot2 = [r1_, r2_]

    r1 = sg.compression_2_comp(r1)
    r2 = sg.compression_2_comp(r2)

    r1_ = tran.in_log_(r1)
    r2_ = tran.in_log_(r2)

    r1_ = tran.from_COMP_in_RE_IM(r1)[0::2]
    r2_ = tran.from_COMP_in_RE_IM(r2)[0::2]

    #dialog2 = r1_

    plot3 = [r1_, r2_]

    #r3 = BPF.bpf(r1)[1]
    #r4 = BPF.bpf(r2)[1]

    #plot4 = [r3, r4]

    #dialog1 = []
    #dialog2 = []
    #plot1 = []
    #plot2 = []
    #plot3 = []
    plot4 = []
    #print(dialog1)

    return dialog1,dialog2,plot1,plot2,plot3,plot4


'''
    Диалог1.table.my_signal.emit(data1)

    data = []
    data.append(data1)
    data.append(data2)

    #self.Диалог1.table.my_signal.emit(self.data2)
    plot1.my_signal_plot.emit(data) # вкладка - график 1

    r1 = __def__.compres.compression_comp(data1, barker)
    r2 = __def__.compres.compression_comp(data2, barker)
    r1_ = tran.from_COMP_in_RE_IM(r1)[0::2]
    r2_ = tran.from_COMP_in_RE_IM(r2)[0::2]


    res = []
    res.append(r1_)
    res.append(r2_)
    plot2.my_signal_plot.emit(res) # вкладка - график 2

    r1 = __def__.compres.compression_2_comp(r1)
    r2 = __def__.compres.compression_2_comp(r2)
    r1_ = tran.in_log_(r1)
    r2_ = tran.in_log_(r2)

    #r1_ = tran.from_COMP_in_RE_IM(r1)[0::2]
    #r2_ = tran.from_COMP_in_RE_IM(r2)[0::2]

    Диалог2.table.my_signal.emit(r1_) #обновление таблицы #2

    res = []
    res.append(r1_)
    res.append(r2_)
    plot3.my_signal_plot.emit(res) # вкладка - график 3 после 2 сжатия

    r3 = bpf(r1)
    Диалог2.table.my_signal.emit(r3) #обновление таблицы #

    #r4 = Windows.BPF.bpf(r2)[0]
    r4 = r3
    res = []
    res.append(r3)
    res.append(r4)
    plot4.my_signal_plot.emit(res) # вкладка - график 4 БПФ'''
