from inputan import masukan
class fungsi(masukan):
    zakat = []
    gajipertahun = []
    zakatpertahun = []
    nisab =[]
    
   # nisab = []

    def __init__(self):
       print("")

    def gajisetahun(self):
        upah = 12 * int(masukan.arraygaji[0])
        self.gajipertahun.append(upah)
        return self.gajipertahun
    
    def zakat(self):
        z = 25 * self.gajipertahun[0]
        y = z/1000
        self.zakatpertahun.append(y)
        return self.zakatpertahun
    
    def nisabu(self):
        n = 85 * int(masukan.emas[0])
        self.nisab.append(n)
        return self.nisab


    

