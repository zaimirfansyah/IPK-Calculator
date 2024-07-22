# Fungsi untuk mengonversi nilai huruf ke poin nilai
def nilai_ke_poin(nilai):
    konversi = {
        'F': 0.0,
        'D-': 0.7,
        'D': 1.0,
        'D+': 1.3,
        'C-': 1.7,
        'C': 2.0,
        'C+': 2.3,
        'B-': 2.7,
        'B': 3.0,
        'B+': 3.3,
        'A-': 3.7,
        'A': 4.0,
        'A+': 4.3
    }
    return konversi.get(nilai.upper(), 0.0)

# Fungsi untuk meminta input pengguna
def input_data():
    mata_pelajaran = input("Masukkan nama mata pelajaran: ")

    while True:
        try:
            kredit = int(input("Masukkan jumlah kredit: "))
            break
        except ValueError:
            print("Input tidak valid. Jumlah kredit harus berupa angka bulat. Silakan coba lagi.")
    
    while True:
        nilai = input("Masukkan nilai (contoh: A, B+, C-): ").upper()
        if nilai in ['F', 'D-', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']:
            break
        else:
            print("Input tidak valid. Nilai harus salah satu dari 'F', 'D-', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'. Silakan coba lagi.")

    return {'mata_pelajaran': mata_pelajaran, 'kredit': kredit, 'nilai': nilai}

# Data mata pelajaran
data = []

while True:
    data.append(input_data())
    tambah_lagi = input("Apakah Anda ingin menambah data lagi? (y/n): ")
    if tambah_lagi.lower() != 'y':
        break

# Hitung total kredit dan total poin nilai
total_kredit = 0
total_poin_nilai = 0

for item in data:
    kredit = item['kredit']
    nilai = item['nilai']
    poin_nilai = nilai_ke_poin(nilai)
    total_kredit += kredit
    total_poin_nilai += kredit * poin_nilai

# Hitung IPK
ipk = total_poin_nilai / total_kredit

# Cetak hasil
print("\nHasil Perhitungan IPK:")
for item in data:
    kredit = item['kredit']
    nilai = item['nilai']
    poin_nilai = nilai_ke_poin(nilai)
    print(f"{item['mata_pelajaran']}: {kredit} kredit, nilai {nilai}, poin nilai {kredit} × {poin_nilai} = {kredit * poin_nilai}")

print(f"Total Kredit: {total_kredit}")
print(f"Total Poin Nilai: {total_poin_nilai}")
print(f"IPK: {ipk:.2f}")
