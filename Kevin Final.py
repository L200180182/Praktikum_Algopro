Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> Nama
'Kevin Vittorio Dewangga'
>>> Panggilan
'Kevin'
>>> Agama
'Islam'
>>> NIM
'L200180182'
>>> Prodi
'Informatika'
>>> TTL
'Wonogiri, 12 Desember 1999'
>>> Alamat
'Jl. Kenang,Pokoh,Wonoboyo,Wonogiri'
>>> Hobi
'Renang'
>>> Email
'toshiem321@gmail.com'
>>> Nomor
'081234879970'
>>> ================================ RESTART ================================
>>> 
>>> Nama
'Kevin Vittorio Dewangga'
>>> Tanggal_Lahir
'12 Desember 1999'
>>> Nama_Singkat
'Kevin.V.D'
>>> ## Hasil dari Nama_Singkat yaitu slicing Nama indeks 0 sampai 5 ditambah titik dan Nama indeks 6 ditambah titik ditambah Nama indeks 15
>>> Username
'K121999'
>>> ## Hasil dari username yaitu slicing inisial Nama, Tanggal_Lahir, dan Tahun_Lahir
>>> Password
'Kev777'
>>> ## Hasil dari 3 huruf pertama Nama dan '777'
>>> ================================ RESTART ================================
>>> 
>>> Nama = 'Kevin Vittorio Dewangga'
>>> NIM = 'L200180182'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<type 'int'>
>>> ## Menampilkan Tipe dari variabel a yaitu integer atau bilangan bulat
>>> type(b)
<type 'int'>
>>>  ## Menampilkan Tipe dari variabel b yaitu integer atau bilangan bulat
>>> a / b
51.391304347826086
>>> ## Hasil dari variabel a dibagi variabel b (1182/23)
>>> a // b
51
>>> ## Hasil pembagian bilangan bulat variabel a dibagi variabel b
>>> 10 * (a - 999)
1830
>>> ## Hasil dari variabel a dikurangi 999 kemudian dikali 10 [10 x (1182-999) = 1830]
>>> b ** 2
529
>>>  ## Hasil dari variabel b dipangkatkan 2 yaitu 529
>>> a % b
9
>>> ## Sisa pembagian antara variabel a dibagi b adalah 9
>>> c = 12.5
>>> type(c)
<type 'float'>
>>>  ## Tipe dari variabel c adalah float atau bilangan desimal
>>> a / c
94,56
>>> ## Hasil bagi antara variabel a dibagi variabel c (1182/12.5)
>>> a // c
94.0
>>> ## Hasil pembulatan bilangan dari pembagian variabel a dibagi variabel c (94.56 dibulatkan menjadi 94.0)
>>> a % c
7.0
>>> ## sisa pembagian antara variabel a dibagi variabel c adalah 7
>>> c > b
False
>>> ## Karena variabel c tidak lebih besar dari variabel b maka hasilnya False (salah)
>>> type(c > b)
<type 'bool>
>>>  ## Tipe/jenis dari c > b merupakan Boolean karena berisi perbandingan antaradua objek
>>> a > b and b > c
True
>>> ## Karena a lebih besar dari b dan b lebih besar dari b maka hasilnya True, karena sesuai
>>> a > 1100 or b < 10
True
>>>  ## Karena memang variabel a lebih dari 1100 maka hasilnya True karena sesuai
>>> ================================ RESTART ================================
>>> 
>>> Nama = 'Kevin Vittorio Dewangga'
>>> NIM = 182
>>> Tinggi = 1.75
>>> Berat = 52
>>> TahunLahir = 1999
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<type 'tuple'>
>>> ## Tipe/jenis dari Aku merupakan suatu Tuple atau deretan objek
>>> Aku[0]
1999
>>> ## Menampilkan hasil dari elemen Tuple 'Aku' indeks ke 0
>>> a = NIM % 4; Aku[a]
182
>>> ## karena terdapat sisa pembagian dari operasi NIM % 4 maka yang ditampilkanadalah NIM itu sendiri
>>> type(Aku[a])
<type 'int'>
>>> ## Tipe/jenis dari variabel a adalah integer atau bilangan bulat
>>> Aku[a:4]
(182,)
>>> ## Hasil dari a sampai indeks ke 3 dari tuple Aku
>>> type(Aku[4])
<type 'str'>
>>> ## Tipe/jenis dari Tuple Aku indeks ke 4 adalah string
>>> Aku[0] = 'ok'

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> ## Program Error karena ingin mengubah elemen tuple Aku indeks ke 0 menjadi ok, padahal elemen tuple tidak bisa diubah sehingga prgram ini error
>>> type(Data)
<type 'list'>
>>> ##Tipe/jenis dari Data merupakan suatu List
>>> type(Data[4])
<type 'str'>
>>> ## Tipe/jenis dari elemen List Data indeks ke 4 adalah string
>>> Data[4][5]
' '
>>> ## Karena pada elemen List Data, indeks 5 tidak ada/ hanya sampai indks 4
>>> Data[4][a:6]
'in '
>>> ## Hasil dari Data indeks 4 yaitu 'Kevin Vittorio Dewangga' kemudian dipotong lagi dari huruf a sampai indeks ke 5 sehingga hasilnya adalah 'al'
>>> Data[0] = 'ok'; Data
['ok', 82, 1.75, 182, 'Kevin Vittorio Dewangga']
>>> ## Elemen dalam List dapat diubah dan program tersebut bertujuan untuk mengubah elemen List Data indeks ke 0 yang semula tahun lahir menjadi 'ok'
>>> Data[-a]
1.75
>>> ## Hasil dari Data[-a] yaitu tinggi = 1.75
>>> range(a)
[0, 1, 2]
>>> ## Karena a = 182 /terdiri dari 3 digit angka maka perhitungan rangenya adalah [0, 1, 2]
type (a) 'float'

