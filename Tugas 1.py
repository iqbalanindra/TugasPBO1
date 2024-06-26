def apakah_prima(bilangan):
    if bilangan > 1:
        for i in range(2, int(bilangan**0.5) + 1):
            if (bilangan % i) == 0:
                return "Bukan Bilangan Prima"
        else:
            return "Bilangan Prima"
    else:
        return "Bukan Bilangan Prima"

# Contoh penggunaan
angka = 17
print(apakah_prima(angka))