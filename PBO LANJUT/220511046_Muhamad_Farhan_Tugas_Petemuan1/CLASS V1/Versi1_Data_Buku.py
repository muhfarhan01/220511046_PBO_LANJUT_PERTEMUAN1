class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        
    def info(self):
        print(f"Judul Buku: {self.judul}\nPenulis: {self.penulis}\nTahun Terbit: {self.tahun_terbit}")

buku1 = Buku("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997)
buku1.info()
