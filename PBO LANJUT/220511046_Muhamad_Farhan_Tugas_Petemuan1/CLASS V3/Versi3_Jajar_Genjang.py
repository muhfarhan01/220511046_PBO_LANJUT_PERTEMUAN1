class JajaranGenjang:
    def __init__(self):
        self._alas = None
        self._tinggi = None
        
    @property
    def alas(self):
        return self._alas
    
    @alas.setter
    def alas(self, value):
        self._alas = value
        
    @property
    def tinggi(self):
        return self._tinggi
    
    @tinggi.setter
    def tinggi(self, value):
        self._tinggi = value
        
    def hitung_luas(self):
        return self._alas * self._tinggi

jajaran_genjang = JajaranGenjang()
alas = float(input("Masukkan nilai alas jajaran genjang: "))
tinggi = float(input("Masukkan nilai tinggi jajaran genjang: "))

jajaran_genjang.alas = alas
jajaran_genjang.tinggi = tinggi
luas_jajaran_genjang = jajaran_genjang.hitung_luas()

print("Alas:", alas)
print("Tinggi:", tinggi)
print("Luas Jajaran Genjang:", luas_jajaran_genjang)
