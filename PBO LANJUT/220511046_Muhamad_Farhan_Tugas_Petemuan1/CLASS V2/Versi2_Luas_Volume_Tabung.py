import math
class Tabung:
    def __init__(self):
        self.jari_jari = None
        self.tinggi = None
        self.volume = None
        
    def hitung_volume(self):
        self.volume = math.pi * (self.jari_jari ** 2) * self.tinggi
        return self.volume

tabung = Tabung()
tabung.jari_jari = float(input("Masukkan nilai jari-jari tabung: "))
tabung.tinggi = float(input("Masukkan nilai tinggi tabung: "))
volume_tabung = tabung.hitung_volume()

print("Jari-jari:", tabung.jari_jari)
print("Tinggi:", tabung.tinggi)
print("Volume Tabung:", volume_tabung)
