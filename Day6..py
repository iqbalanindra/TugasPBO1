class Mahasiswa:
    def __init__(self, nim, nama, angkatan, prodi):
        self.nim = nim
        self.nama = nama
        self.angkatan = angkatan
        self.prodi = prodi

    def kartu_mahasiswa(self):
        print(f"NIM: {self.nim}")
        print(f"Nama: {self.nama}")
        print(f"Angkatan: {self.angkatan}")
        print(f"Prodi: {self.prodi}")

    def selamat(self):
        print(f"Selamat datang {self.nama} di kampus UMS")


mahasiswa1 = Mahasiswa("A710230042", "Riski Bimo Aji", "2023", "Pendidikan Teknik Informasi")
mahasiswa2 = Mahasiswa("A710230008", "Nabira Zain", "2023", "Pendidikan Teknik Informasi")
mahasiswa3 = Mahasiswa("A710230017", "Azzun Adna", "2023", "Pendidikan Teknik Informasi")

mahasiswa1.kartu_mahasiswa()
mahasiswa1.selamat()

mahasiswa2.kartu_mahasiswa()
mahasiswa2.selamat()

mahasiswa3.kartu_mahasiswa()
mahasiswa3.selamat()