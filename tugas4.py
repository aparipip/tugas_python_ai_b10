# ==============================
# LIST – AKSES & MANIPULASI
# ==============================
print("=== LIST ===")
data = ["Arif", 20, 3.5, "Surabaya", True, 100]

print("List awal:", data)

# Akses elemen
print("Elemen pertama:", data[0])
print("Elemen terakhir:", data[-1])

# Slicing
print("Slicing [1:5]:", data[1:5])
print("Slicing [::2]:", data[::2])

# Manipulasi
print("\nSebelum manipulasi:", data)

data.append("Mahasiswa")
print("Setelah append:", data)

data.insert(1, "INSERTED")
print("Setelah insert:", data)

data.extend(["Tambahan1", "Tambahan2"])
print("Setelah extend:", data)

data.pop()
print("Setelah pop:", data)

data.remove("INSERTED")
print("Setelah remove:", data)


# ==============================
# TUPLE – IMMUTABILITY & UNPACKING
# ==============================
print("\n=== TUPLE ===")
tpl = ("A", "B", "C", "D", "E")

print("Tuple:", tpl)
print("Panjang tuple:", len(tpl))
print("Akses indeks ke-2:", tpl[2])

# Unpacking
a, b, c, *rest = tpl
print("Unpacking:")
print("a =", a)
print("b =", b)
print("c =", c)
print("rest =", rest)


# ==============================
# SET – OPERASI HIMPUNAN
# ==============================
print("\n=== SET ===")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Duplikat otomatis hilang
set_duplikat = {1, 1, 2, 2, 3}
print("Set tanpa duplikat:", set_duplikat)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)


# ==============================
# DICTIONARY – KEY/VALUE
# ==============================
print("\n=== DICTIONARY ===")
mahasiswa = {
    "nama": "Arif",
    "nim": "23081010192",
    "angkatan": 2023,
    "kota": "Surabaya"
}

print("Data awal:", mahasiswa)

# Tambah key
mahasiswa["prodi"] = "Informatika"

# Ubah nilai
mahasiswa["kota"] = "Sidoarjo"

# Hapus key
del mahasiswa["angkatan"]

print("Data setelah manipulasi:", mahasiswa)

print("Keys:", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items:", mahasiswa.items())

print("\nIterasi dictionary:")
for key, value in mahasiswa.items():
    print(f"{key}: {value}")


# ==============================
# NESTED STRUCTURES
# ==============================
print("\n=== NESTED STRUCTURE ===")
buku = [
    {"judul": "Python Dasar", "penulis": "Andi", "tahun": 2020},
    {"judul": "AI Modern", "penulis": "Budi", "tahun": 2023},
    {"judul": "Data Science", "penulis": "Citra", "tahun": 2021},
    {"judul": "Machine Learning", "penulis": "Dedi", "tahun": 2024},
]

print("Daftar Judul Buku:")
for b in buku:
    print("-", b["judul"])

# Filter buku tahun >= 2022
buku_baru = [b for b in buku if b["tahun"] >= 2022]
print("\nBuku terbit >= 2022:")
for b in buku_baru:
    print("-", b["judul"])


# ==============================
# COMPREHENSION & UTILITAS
# ==============================
print("\n=== COMPREHENSION ===")

# List comprehension
angka = list(range(1, 21))
genap = [x for x in angka if x % 2 == 0]
kuadrat = [x**2 for x in angka]

print("Angka genap:", genap)
print("Kuadrat:", kuadrat)

# Dict comprehension
dict_angka = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}
print("Dict genap/ganjil:", dict_angka)

# Set comprehension
kalimat = "Halo Dunia Python"
huruf_unik = {c.lower() for c in kalimat if c.isalpha()}
print("Huruf unik:", huruf_unik)


# ==============================
# KEANGGOTAAN & PENCARIAN
# ==============================
print("\n=== KEANGGOTAAN ===")

# Cek di list
print("Apakah 'Arif' ada di list?", "Arif" in data)

# Cek di set
print("Apakah 3 ada di set1?", 3 in set1)

# Pencarian posisi
if "Arif" in data:
    print("Posisi 'Arif':", data.index("Arif"))
else:
    print("'Arif' tidak ditemukan")