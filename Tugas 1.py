class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur}")

class Mahasiswa(Orang):
    def __init__(self, nama, umur, universitas):
        super().__init__(nama, umur)
        self.universitas = universitas

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur} dan aku kuliah di {self.universitas}")

class Pekerja(Orang):
    def __init__(self, nama, umur, tempatKerja):
        super().__init__(nama, umur)
        self.tempatKerja = tempatKerja

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur} dan aku kerja di {self.tempatKerja}")

orang1 = Orang("Nabira Zain", 20)
orang1.kenalan()

mahasiswa1 = Mahasiswa("Salman Al Frisi", 19, "Universitas Muhammad Iqbal Anindra")
mahasiswa1.kenalan()

pekerja1 = Pekerja("Riski Bimo Aji", 22, "Jual Alat Akustik")
pekerja1.kenalan()