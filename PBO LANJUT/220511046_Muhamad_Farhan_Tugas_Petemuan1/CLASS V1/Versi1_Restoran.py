class Restoran:
    def __init__(self, nama, jenis_masakan, alamat):
        self.nama = nama
        self.jenis_masakan = jenis_masakan
        self.alamat = alamat
        
    def info(self):
        print(f"Nama Restoran: {self.nama}\nJenis Masakan: {self.jenis_masakan}\nAlamat: {self.alamat}")

restoran1 = Restoran("Sate Khas Senayan", "Masakan Indonesia", "Jl. Gatot Subroto No. 123, Jakarta")
restoran1.info()
