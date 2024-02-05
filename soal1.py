
# https://github.com/Aseptrisna/Algoritma-dan-Pemrograman/tree/master
def main():
    try:
        N = int(input("Masukkan jumlah pegawai (N): "))
        if N <= 0 or N > 500:
            print("Data jumlah pegawai tidak tepat.")
            return

        # Inisialisasi variabel untuk menghitung jumlah indeks
        count_A = 0
        count_B = 0
        count_C = 0

        # Membaca nilai kinerja pegawai sebanyak N kali
        for _ in range(N):
            nilai_kinerja = int(input("Masukkan nilai kinerja (0-100): "))
            while nilai_kinerja < 0 or nilai_kinerja > 100:
                print("Nilai kinerja harus antara 0 hingga 100.")
                nilai_kinerja = int(input("Masukkan nilai kinerja (0-100): "))

            # Menghitung indeks berdasarkan nilai kinerja
            if nilai_kinerja >= 85:
                count_A += 1
            elif 70 <= nilai_kinerja < 85:
                count_B += 1
            elif 50 <= nilai_kinerja < 70:
                count_C += 1

        # Menghitung indeks kinerja perusahaan
        IK = (count_A * 3 + count_B * 2 + count_C) / N

        # Menampilkan hasil
        print(f"Jumlah pegawai dengan indeks A: {count_A}")
        print(f"Jumlah pegawai dengan indeks B: {count_B}")
        print(f"Jumlah pegawai dengan indeks C: {count_C}")
        print(f"Indeks Kinerja (IK) perusahaan: {IK:.2f}")

    except ValueError:
        print("Masukan harus berupa bilangan bulat.")

if __name__ == "__main__":
    
    main()
