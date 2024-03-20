class Parkir:
    def __init__(self, nomor_kendaraan, jenis_kendaraan, durasi_parkir):
        self.nomor_kendaraan = nomor_kendaraan
        self.jenis_kendaraan = jenis_kendaraan
        self.durasi_parkir = durasi_parkir
        
    def info(self):
        print(f"Nomor Kendaraan: {self.nomor_kendaraan}\nJenis Kendaraan: {self.jenis_kendaraan}\nDurasi Parkir: {self.durasi_parkir} jam")

parkir1 = Parkir("B 1234 AB", "Mobil", 2)
parkir1.info()
