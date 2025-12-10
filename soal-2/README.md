# Soal 2 : Largest Monotonically Increasing Subsequence

Teori Graf B - Kelompok 11

| Nama | NRP |
| -- | -- |
| Bintang Ilham Pabeta | 5025241152 |
| Delta Bintang Permana | 5025241154 |

Penjelasan struktur data serta fungsi-fungsi dalam implementasi pencarian semua **Largest Increasing Subsequence (LIS)** menggunakan rekonstruksi tree berbasis rekursif.

## Konsep Utama

* LIS adalah subsekuens dari array yang nilainya **monoton naik** dan memiliki **panjang maksimum**.
* Solusi dibuat dengan:

  1. Menghitung DP panjang LIS pada setiap indeks.
  2. Membangun directed tree dari indeks-indeks yang dapat saling berhubungan.
  3. Melakukan DFS untuk mengumpulkan semua subsekuens yang valid.

## Struktur Data

### 1. `dp` (Dynamic Programming Array)

* `dp[i]` menyimpan **panjang LIS yang berakhir di indeks `i`**.
* Digunakan sebagai dasar untuk menentukan hubungan parent–child pada tree.

### 2. `children` (Adjacency List)

* Dictionary yang memetakan indeks ke daftar indeks yang bisa menjadi penerusnya.
* Indeks `j` menjadi child dari `i` jika:

  * `arr[j] > arr[i]`
  * `dp[j] == dp[i] + 1`
* Tree ini biasanya bukan binary tree; bisa bercabang banyak.

## Tahapan Fungsi

1. **Perhitungan DP LIS**

* Dua loop untuk menentukan `dp[i]`.
* Kompleksitas: `O(n^2)`.

2. **Membangun Tree LIS**

* Satu loop (dalam loop DP yang sama) untuk mengisi adjacency-list `children`.
* Node dengan `dp[i] == max_len` menjadi **root calon solusi**.

3. **Rekursi DFS**

* Dilakukan dari setiap root.
* Path disimpan jika panjang path sama dengan `max_len`.
* DFS ini mengekstraksi semua LIS yang mungkin.

## Output

* Berisi **semua LIS terbesar** dalam bentuk list of lists.