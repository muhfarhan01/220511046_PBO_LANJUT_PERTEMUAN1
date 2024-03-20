class Persegi:
    def _init_(self):
        self.panjang=None
        self.lebar=None
        self.luas=None
    def Luas(self,panjang,lebar):
        self.panjang=panjang
        self.lebar=lebar
        self.luas=self.panjang * self.lebar
        return self.luas

P = Persegi()
panjang = input("Masukkan Nilai Panjang:")
lebar = input("Masukkan Nilai Lebar:")
luas = P.luas(int(panjang),int(lebar))

print("Panjang:",panjang)
print("lebar:",lebar)
print("luas:",luas)
