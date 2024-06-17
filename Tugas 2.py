 # Input jumlah anak bebek
jumlah_anak_bebek = int(input("Masukkan jumlah anak bebek: "))

# Loop untuk menampilkan lirik lagu
for i in range(jumlah_anak_bebek, 0, -1):
    if i > 1:
        print(f"Anak bebek turun {i}, mati satu tinggal {i - 1}")
    else:
        print("Anak bebek turun 1, mati satu tinggal induknya")