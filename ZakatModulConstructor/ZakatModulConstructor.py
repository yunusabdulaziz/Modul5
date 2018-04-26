print ('+-----------------------------------------------+')
print ('|  Program  Menghitung Zakat Penghasilan        |')
print ('|      menurut pendapatan kasar (brutto)        |')
print ('|                                               |')
print ('|      Kelompok 31 Shift 1                      |')
print ('|  1. Luqman Setyo Nugrogho / 21120117120008    |')
print ('|  2. Dina Lusiana          / 21120117120030    |')
print ('+-----------------------------------------------+')
print ('')
print('==========================================')

from inputan import masukan
from fungsi import fungsi

Orang_1 = masukan()
Orang_1.inputnama()
Orang_1.hargaemas()
Orang_1.gaji()


Fungsi_Orang1 = fungsi()
Fungsi_Orang1.gajisetahun()
Fungsi_Orang1.zakat()
Fungsi_Orang1.nisabu()

print('')
print('===========================================')
print('             Zakat Penghasilan')
print('===========================================')
print('Nama                     : ',Orang_1.nama[0] )  
print('')
print('Harga 1 Gram Emas        : ','Rp.',Orang_1.emas[0])
print('')
print('Penghasilan Perbulan     : ','Rp.', Orang_1.arraygaji[0])
print('')
print('Penghasilan Pertahun     : ','Rp.',Fungsi_Orang1.gajipertahun[0])
print('')
print('Harga Nisab 85 gram emas : ','Rp.',Fungsi_Orang1.nisab[0])
print('')
print('Zakat Penghasilan        : ','2.5% x', Fungsi_Orang1.gajipertahun[0] ,'=','Rp.', Fungsi_Orang1.zakatpertahun[0])
print('')

if Fungsi_Orang1.gajipertahun[0] >= Fungsi_Orang1.nisab[0] :
    print ('Keterangan               :  Wajib Zakat Rp.',Fungsi_Orang1.zakatpertahun[0],' /tahun')
    print('')

if Fungsi_Orang1.gajipertahun[0] < Fungsi_Orang1.nisab[0] :
    print ('Keterangan               :  Anda Belum Wajib Zakat')
    print('')
