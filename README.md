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
Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): 2000
Saldo saat ini: Rp2000
ON:
Lintasan DFA: q0 → q1

Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): 2000
Saldo saat ini: Rp4000
ON: Minuman A, Minuman B
Lintasan DFA: q0 → q1 → q2

Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): B
Lintasan DFA: q0 → q1 → q2
Minuman B dapat dibeli. Status: ACCEPTED.
Kembalian: 0
Terima kasih! Silakan ambil minuman Anda.
```

## Catatan
- Program hanya menerima nominal uang tertentu.
- Batas maksimum saldo adalah Rp10.000.
- Program akan berhenti setelah minuman berhasil dibeli.

## Lisensi
Program ini bebas digunakan dan dimodifikasi sesuai kebutuhan.

