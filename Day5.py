# Menghitung usia penumpang berdasarkan tahun kelahiran
def hitung_usia(tahun_lahir):
    tahun_sekarang = 2023  # Tahun saat ini
    return tahun_sekarang - tahun_lahir

# Meminta input tahun kelahiran penumpang dan harga tiket
tahun_lahir = int(input("Masukkan tahun kelahiran penumpang: "))
harga_tiket = float(input("Masukkan harga tiket kereta: "))

# Menghitung usia penumpang
usia = hitung_usia(tahun_lahir)

# Menentukan diskon berdasarkan usia
if usia >= 0 and usia <= 4:
    diskon = 1.0  # Diskon 100%
elif usia >= 5 and usia <= 11:
    diskon = 0.5  # Diskon 50%
else:
    diskon = 0.0  # Tidak ada diskon

# Menghitung harga setelah diskon
harga_setelah_diskon = harga_tiket * (1 - diskon)

# Menampilkan hasil
print(f"Usia penumpang: {usia} tahun")
print(f"Diskon: {int(diskon * 100)}%")
print(f"Harga tiket setelah diskon: Rp {harga_setelah_diskon:.2f}")