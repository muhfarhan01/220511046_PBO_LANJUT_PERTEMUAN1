class Balok:
    def __init__(self):
        self.panjang = None
        self.lebar = None
        self.tinggi = None
        self.volume = None
        
    def hitung_volume(self):
        self.volume = self.panjang * self.lebar * self.tinggi
        return self.volume

balok = Balok()
balok.panjang = float(input("Masukkan nilai panjang balok: "))
balok.lebar = float(input("Masukkan nilai lebar balok: "))
balok.tinggi = float(input("Masukkan nilai tinggi balok: "))
volume_balok = balok.hitung_volume()

print("Panjang:", balok.panjang)
print("Lebar:", balok.lebar)
print("Tinggi:", balok.tinggi)
print("Volume Balok:", volume_balok)
