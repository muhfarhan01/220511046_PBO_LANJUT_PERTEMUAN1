import math
class Lingkaran:
    def __init__(self):
        self.jari_jari = None
        self.luas = None
        
    def hitung_luas(self):
        self.luas = math.pi * (self.jari_jari ** 2)
        return self.luas

lingkaran = Lingkaran()
lingkaran.jari_jari = float(input("Masukkan nilai jari-jari lingkaran: "))
luas_lingkaran = lingkaran.hitung_luas()

print("Jari-jari Lingkaran:", lingkaran.jari_jari)
print("Luas Lingkaran:", luas_lingkaran)
