daftar_teman = {}
for i in range (5):
    nama = input(f"Masukkan nama teman {i + 1}: ")
    nomor_handphone = (f"Masukkan nomor handphone teman {i + 1}: ")
    daftar_teman[nama] = nomor_handphone
print("\nDaftar Teman: ")
for nama, nomor_handphone in daftar_teman.items():
    print(f"{nama}: {nomor_handphone}")