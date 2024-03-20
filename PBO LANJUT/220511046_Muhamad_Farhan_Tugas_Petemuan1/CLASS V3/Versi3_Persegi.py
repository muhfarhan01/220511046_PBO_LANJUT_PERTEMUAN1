class Persegi:
    def __init__(self):
        self._sisi = None
        
    @property
    def sisi(self):
        return self._sisi
    
    @sisi.setter
    def sisi(self, value):
        self._sisi = value
        
    def hitung_luas(self):
        return self._sisi ** 2

persegi = Persegi()
sisi = float(input("Masukkan nilai sisi persegi: "))

persegi.sisi = sisi
luas_persegi = persegi.hitung_luas()

print("Sisi:", sisi)
print("Luas Persegi:", luas_persegi)

