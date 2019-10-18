nama = 'Fani Rohmiasih'
program = 'Energi'

print(f'Program perhitungan {program} oleh {nama}')
print(f'{program} potensial, kinetik dan mekanik')

def hitung_potensial(massa,grafitasi,ketinggian):
    potensial = massa * grafitasi * ketinggian
    print(f'jika benda bermassa {massa} kg berada pada ketinggian {ketinggian} m dari permukaan tanah')
    print(f'maka energi potensial nya {potensial} J')
    return(potensial)

def hitung_kinetik(massa, kecepatan):
    kinetik = 0.5 * massa * kecepatan**2
    print(f'jika benda bermassa {massa} kg mempunyai kecepatan {kecepatan} m/s')
    print(f'maka energi kinetiknya {kinetik} J')
    return(kinetik)

# massa = 5
# grafitasi = 9.8
# ketinggian = 8
# kecepatan = 5
potensial = hitung_potensial(5, 9.8, 8)
potensial = hitung_potensial(4, 9.8, 9)
kinetik = hitung_kinetik(5, 5)
kinetik = hitung_kinetik(4, 9)

def hitung_mekanik(energipotensial, energikinetik):
    mekanik = energipotensial + energikinetik
    print(f'Jika benda memiliki energi potensial {energipotensial} J dan energi kinetik {energikinetik} J')
    print(f'maka energi mekaniknya {mekanik} J')
    return(mekanik)

# energipotensial = 392
# energikinetik = 62.5
mekanik = hitung_mekanik(392, 62.5)
mekanik = hitung_mekanik(352.8, 162)