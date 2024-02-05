def cari_subderet_menaik(arr):
    subderet = []
    subderet_saat_ini = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            subderet_saat_ini.append(arr[i])
        else:
            if len(subderet_saat_ini) > 1:
                subderet.append(subderet_saat_ini)
            subderet_saat_ini = [arr[i]]
    
    if len(subderet_saat_ini) > 1:
        subderet.append(subderet_saat_ini)
        
    return subderet

def jumlah_subderet(subderet):
    return sum([sum(deret) for deret in subderet])

n = int(input().strip())
bilangan = list(map(int, input().strip().split()))

if n != len(bilangan):
    print("Jumlah bilangan tidak sesuai dengan nilai N yang diberikan.")
else:
    subderet_menaik = cari_subderet_menaik(bilangan)
    
    if not subderet_menaik:
        print(0)
    else:
        total_jumlah = jumlah_subderet(subderet_menaik)
        print(total_jumlah)


#Github: https://github.com/Aseptrisna/Algoritma-dan-Pemrograman.git
#Dokumentasi :https://github.com/Aseptrisna/Algoritma-dan-Pemrograman/blob/master/README.md
#Full code:https://github.com/Aseptrisna/Algoritma-dan-Pemrograman/blob/master/soal2.py