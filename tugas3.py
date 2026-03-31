# ==============================
# Deklarasi Variabel & Tipe Data
# ==============================
nama = "Arif"          # string
umur = 20              # integer
tinggi = 170.5         # float
is_student = True      # boolean
hobi = ["Coding", "Gaming", "Membaca", "Olahraga", "Musik"]  # list

# ==============================
# Manipulasi String
# ==============================
print("=== Manipulasi String ===")
kalimat = "Halo, saya " + nama
print(kalimat)

print("Panjang string:", len(kalimat))
print("Huruf besar:", kalimat.upper())
print("Huruf kecil:", kalimat.lower())

# ==============================
# Operasi Matematika Sederhana
# ==============================
print("\n=== Operasi Matematika ===")
a = 10
b = 3

print("Penjumlahan:", a + b)
print("Pengurangan:", a - b)
print("Perkalian:", a * b)
print("Pembagian:", a / b)
print("Pembagian bulat:", a // b)
print("Sisa bagi:", a % b)

# ==============================
# List dan Akses Elemen
# ==============================
print("\n=== List ===")
print("List awal:", hobi)

print("Elemen pertama:", hobi[0])

hobi.append("Traveling")
print("Setelah tambah:", hobi)

hobi.remove("Gaming")
print("Setelah hapus:", hobi)

# ==============================
# Input dari User
# ==============================
print("\n=== Input User ===")
nama_user = input("Masukkan nama Anda: ")
umur_user = input("Masukkan umur Anda: ")
umur_user = int(umur_user) 

print("Halo, nama saya", nama_user, "dan umur saya", umur_user, "tahun.")