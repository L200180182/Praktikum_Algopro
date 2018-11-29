import shelve
a = open('L200180182', 'r')
NIM = a.readline()
TL = a.readline()
Nama = a.readline()
a.close()

a = shelve.open('Kevin')
a['b'] = [NIM, TL, Nama]
a.close()
