# Soal 1 : Knight's Tour

Teori Graf B - Kelompok 11

| Nama | NRP |
| -- | -- |
| Bintang Ilham Pabeta | 5025241152 |
| Delta Bintang Permana | 5025241154 |

## Overview

Program ini menyelesaikan masalah **Knight's Tour** menggunakan heuristik **Warnsdorff’s Rule** serta backtracking, kemudian menampilkan animasi pergerakan kuda.

Berikut penjelasan fungsi-fungsi utamanya.

---

## `is_valid_move(x, y, board)`

Memeriksa apakah langkah kuda menuju `(x, y)` valid.

* Koordinat harus berada di dalam papan.
* Kotak tersebut harus belum dikunjungi (`-1`).

Return:

* `True` jika valid.
* `False` jika tidak valid.

---

## `count_valid_moves(x, y, x_moves, y_moves, board)`

Menghitung berapa banyak langkah valid yang dapat dilakukan dari posisi `(x, y)`.
Digunakan sebagai bagian dari heuristik Warnsdorff untuk memilih langkah yang paling "sempit" dulu.

---

## `get_warnsdorff_moves(x, y, x_moves, y_moves, board)`

Menghasilkan daftar semua langkah valid dari posisi saat ini, lengkap dengan jumlah langkah lanjutan yang mungkin.

Langkah-langkah:

1. Cek semua 8 kemungkinan langkah kuda.
2. Jika valid, hitung jumlah langkah lanjutan (`count_valid_moves`).
3. Sortir berdasarkan jumlah langkah lanjutan (ascending).

Mengembalikan list tuple `(new_x, new_y)` yang telah diurutkan.

---

## `solve_knight_tour(board, x, y, move_count, x_moves, y_moves, path, is_closed, max_iterations)`

Fungsi backtracking utama untuk mencari solusi Knight's Tour.

Alur:

1. **Basis** → jika semua kotak telah dikunjungi:

   * Jika `is_closed == True`, periksa apakah bisa kembali ke posisi awal.
   * Jika open tour, cukup return sukses.

2. Ambil semua langkah valid berdasarkan Warnsdorff.

3. Coba satu per satu:

   * Tandai posisi baru.
   * Rekursif ke langkah berikutnya.
   * Jika gagal, lakukan **backtrack**.

Return:

* `True` jika solusi ditemukan.
* `False` jika tidak.

---

## `animate_knight(path, size)`

Menganimasikan perjalanan kuda menggunakan `matplotlib.animation.FuncAnimation`.

* Menggambar papan grid.
* Memperbarui posisi kuda frame demi frame.

---

## `visualize_knight_tour(path, size)`

Menampilkan rute akhir kuda dalam bentuk grafik statik.

---

## `knight_tour()`

Fungsi utama yang:

1. Menerima input jenis tour (open/closed) dan posisi awal.
2. Menginisialisasi papan.
3. Memulai pencarian dengan `solve_knight_tour`.
4. Menampilkan hasil atau pesan kegagalan.


