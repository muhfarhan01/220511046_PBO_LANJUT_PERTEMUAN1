class PersegiPanjang:
    def __init__(self):
        self._panjang = None
        self._lebar = None
        
    @property
    def panjang(self):
        return self._panjang
    
    @panjang.setter
    def panjang(self, value):
        self._panjang = value
        
    @property
    def lebar(self):
        return self._lebar
    
    @lebar.setter
    def lebar(self, value):
        self._lebar = value
        
    def hitung_luas(self):
        return self._panjang * self._lebar

persegi_panjang = PersegiPanjang()
panjang = int(input("Masukkan nilai panjang persegi panjang: "))
lebar = int(input("Masukkan nilai lebar persegi panjang: "))

persegi_panjang.panjang = panjang
persegi_panjang.lebar = lebar
luas_persegi_panjang = persegi_panjang.hitung_luas()

print("Panjang:", panjang)
print("Lebar:", lebar)
print("Luas Persegi Panjang:", luas_persegi_panjang)
