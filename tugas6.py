# ==============================
# IMPORT & SETUP
# ==============================
import numpy as np
import pandas as pd
import os

np.random.seed(42)


# ==============================
# NUMPY – DATA & STATISTIK
# ==============================
nilai_ujian = np.random.randint(50, 100, size=10)

rata = np.mean(nilai_ujian)
median = np.median(nilai_ujian)
std = np.std(nilai_ujian)
nilai_min = np.min(nilai_ujian)
nilai_max = np.max(nilai_ujian)


# ==============================
# PANDAS – DATAFRAME
# ==============================
data = {
    "nama": ["Arif", "Budi", "Citra", "Dedi", "Eka"],
    "nim": ["001", "002", "003", "004", "005"],
    "nilai": nilai_ujian[:5]  # ambil 5 data dari numpy
}

df = pd.DataFrame(data)

# Tambah kolom status
df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")


# ==============================
# FILE I/O – SIMPAN KE TXT
# ==============================
def tulis_ringkasan(path="ringkasan_tugas6.txt"):
    with open(path, "w") as f:
        f.write("=== RINGKASAN NUMPY ===\n")
        f.write(f"Rata-rata: {rata}\n")
        f.write(f"Median: {median}\n")
        f.write(f"Standar Deviasi: {std}\n")
        f.write(f"Nilai Minimum: {nilai_min}\n")
        f.write(f"Nilai Maksimum: {nilai_max}\n\n")

        f.write("=== RINGKASAN DATAFRAME ===\n")
        f.write(f"Jumlah data: {len(df)}\n")
        f.write(f"Jumlah LULUS: {len(df[df['status'] == 'LULUS'])}\n")
        f.write(f"Jumlah TIDAK LULUS: {len(df[df['status'] == 'TIDAK LULUS'])}\n")


# ==============================
# OOP – CLASS GRADEBOOK
# ==============================
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return round(self.df["nilai"].mean(), 2)

    def pass_rate(self, threshold: float = 70.0) -> float:
        total = len(self.df)
        lulus = len(self.df[self.df["nilai"] >= threshold])
        return round((lulus / total) * 100, 2) if total > 0 else 0.0

    def save_summary(self, path: str):
        with open(path, "a") as f:
            f.write("\n=== RINGKASAN GRADEBOOK ===\n")
            f.write(f"Rata-rata nilai: {self.average()}\n")
            f.write(f"Persentase lulus: {self.pass_rate()}%\n")

    def __str__(self) -> str:
        return f"GradeBook(jumlah_data={len(self.df)}, rata_rata={self.average()})"


# ==============================
# DEMO
# ==============================
if __name__ == "__main__":

    print("=== NUMPY ===")
    print("Data nilai:", nilai_ujian)
    print("Rata-rata:", rata)
    print("Median:", median)
    print("Standar Deviasi:", std)
    print("Min:", nilai_min)
    print("Max:", nilai_max)

    print("\n=== PANDAS ===")
    print(df.head())

    print("\n=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)

    print(gb)
    print("Average:", gb.average())
    print("Pass Rate:", gb.pass_rate(), "%")

    # Simpan ke file
    tulis_ringkasan()
    gb.save_summary("ringkasan_tugas6.txt")

    print("\nRingkasan berhasil disimpan ke 'ringkasan_tugas6.txt'")