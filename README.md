# Vending Machine DFA

Program ini mensimulasikan vending machine menggunakan *Deterministic Finite Automaton (DFA)* untuk menangani input uang dan pembelian minuman.

## Persyaratan
- Python 3.x
- File konfigurasi `DFA.txt` untuk mendefinisikan transisi DFA

## Cara Menjalankan
1. Pastikan Python telah terinstal di sistem.
2. Pastikan file `vendingmachine_DFA.py` dan `DFA.txt` berada dalam direktori yang sama.
3. Jalankan perintah berikut di terminal atau command prompt:
   ```sh
   python vendingmachine_DFA.py
   ```

## Cara Menggunakan
- Masukkan uang dengan nominal: `1000`, `2000`, `5000`, atau `10000`.
- Pilih minuman dengan memasukkan huruf yang sesuai:
  - `A` (Rp3000)
  - `B` (Rp4000)
  - `C` (Rp6000)
- Program akan menampilkan saldo saat ini dan minuman yang tersedia.
- Jika saldo mencukupi, minuman akan diberikan dan kembalian ditampilkan jika ada.
- Jika saldo tidak mencukupi, status akan menunjukkan *REJECTED*.

## Contoh Penggunaan
```
- Kasus tidak ada kembalian

Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): 1000
Saldo saat ini: Rp1000
Lintasan DFA: S0 → S1000
Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): 2000
ON: Minuman A
Saldo saat ini: Rp3000
Lintasan DFA: S0 → S1000 → S3000
Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): A
Lintasan DFA: S0 → S1000 → S3000
Minuman A dapat dibeli. Status: ACCEPTED.
Terima kasih! Silakan ambil minuman Anda.

Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): 2000
Saldo saat ini: Rp2000
Lintasan DFA: S0 → S2000
Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): 2000
ON: Minuman A, Minuman B
Saldo saat ini: Rp4000
Lintasan DFA: S0 → S2000 → S4000
Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): B
Lintasan DFA: S0 → S2000 → S4000
Minuman B dapat dibeli. Status: ACCEPTED.
Terima kasih! Silakan ambil minuman Anda.

Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): 5000
ON: Minuman A, Minuman B
Saldo saat ini: Rp5000
Lintasan DFA: S0 → S5000
Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): 1000
ON: Minuman A, Minuman B, Minuman C
Saldo saat ini: Rp6000
Lintasan DFA: S0 → S5000 → S6000
Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): C
Lintasan DFA: S0 → S5000 → S6000
Minuman C dapat dibeli. Status: ACCEPTED.
Terima kasih! Silakan ambil minuman Anda.

- Kasus dengan kembalian

Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): 5000
ON: Minuman A, Minuman B
Saldo saat ini: Rp5000
Lintasan DFA: S0 → S5000
Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): B
Lintasan DFA: S0 → S5000
Minuman B dapat dibeli. Status: ACCEPTED.
Kembalian: 1000
Terima kasih! Silakan ambil minuman Anda.

Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): 5000
ON: Minuman A, Minuman B
Saldo saat ini: Rp5000
Lintasan DFA: S0 → S5000
Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): 1000
ON: Minuman A, Minuman B, Minuman C
Saldo saat ini: Rp6000
Lintasan DFA: S0 → S5000 → S6000
Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): B
Lintasan DFA: S0 → S5000 → S6000
Minuman B dapat dibeli. Status: ACCEPTED.
Kembalian: 2000
Terima kasih! Silakan ambil minuman Anda.

- Kasus jika format input tidak sesuai dengan syarat
Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): 10000
ON: Minuman A, Minuman B, Minuman C
Saldo saat ini: Rp10000
Lintasan DFA: S0 → S10000
Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): c
Pilihan minuman tidak valid. Status: REJECTED
Lintasan DFA: S0 → S10000

Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): 100000
Harap masukkan nominal yang dapat diterima! (Pecahan 1000, 2000, 5000 atau 10000)
Current state: S10000
Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): # meminta memasukkan kembali dengan input yang sesuai

```

## Catatan
- Program hanya menerima nominal uang tertentu.
- Batas maksimum saldo adalah Rp10.000.
- Program akan berhenti setelah minuman berhasil dibeli.
- Jika format input tidak sesuai, maka program akan menampilkan output: "Pilihan minuman tidak valid. Status: REJECTED" atau "Harap masukkan nominal yang dapat diterima! (Pecahan 1000, 2000, 5000 atau 10000)"

## Lisensi
Program ini bebas digunakan dan dimodifikasi sesuai kebutuhan.

