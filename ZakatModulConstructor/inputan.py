class masukan(object):
    nama = []
    emas = []
    arraygaji = []
    

    def __init__(self):
        print("Data Baru Telah Dibuat")
       
    def inputnama(self):
        a = input    ('Masukan Nama                 : ')
        print('')
        self.nama.append(a)
        return self.nama

    def hargaemas(self):
        gold = input ('Masukan Harga Emas Saat Ini  : ')
        print('')
        self.emas.append(gold)
        return self.emas

    def gaji(self):
        c = int(input('Masukan Penghasilan Perbulan : '))
        print('')
        self.arraygaji.append(c)
        return self.arraygaji
    
