def cari_suburut_menaik(angka):
    suburut = []
    suburut_saat_ini = [angka[0]]

    for i in range(1, len(angka)):
        if angka[i] > angka[i - 1]:
            suburut_saat_ini.append(angka[i])
        else:
            if len(suburut_saat_ini) > 1:
                suburut.append(suburut_saat_ini)
            suburut_saat_ini = [angka[i]]

    if len(suburut_saat_ini) > 1:
        suburut.append(suburut_saat_ini)

    return suburut

def jumlah_suburut(suburut):
    return sum([sum(suburut_elemen) for suburut_elemen in suburut])

n = int(input().strip())
angka = list(map(int, input().strip().split()))

if n != len(angka):
    print("Jumlah bilangan tidak sesuai dengan jumlah yang ditentukan.")
else:
    suburut_menaik = cari_suburut_menaik(angka)
    
    if not suburut_menaik:
        print(0)
    else:
        total_jumlah = jumlah_suburut(suburut_menaik)
        print(total_jumlah)
