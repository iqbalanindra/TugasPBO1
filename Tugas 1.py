# definisi kelas Barang
class Barang:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

# definisi kelas Kasa
class Kasa:
    def __init__(self):
        self.barang = []
        self.jumlah = 0
        self.total_harga = 0

    def tambah_barang(self, nama, harga, jumlah):
        barang = Barang(nama, harga)
        self.barang.append(barang)
        self.jumlah += jumlah
        self.total_harga += barang.harga * jumlah

    def cetak_total(self):
        print("Total Harga:", self.total_harga)

    def cetak_rincian(self):
        with open("invoice.txt", "w") as f:
            f.write("Rincian Belanja:\n")
            for barang in self.barang:
                f.write(f"{barang.nama} x {self.jumlah} : {barang.harga * self.jumlah}\n")
            f.write(f"Total Harga: {self.total_harga}\n")

# input data barang
nama = input("Masukkan nama barang: ")
harga = int(input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah barang: "))

# inisialisasi kasir dan barang
kasir = Kasa()
kasir.tambah_barang(nama, harga, jumlah)

# menampilkan total harga
kasir.cetak_total()

# mencetak rincian belanja ke file invoice.txt
kasir.cetak_rincian()