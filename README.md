# Praktikum Struktur Data dan Algoritma - Chapter 5

Repositori ini berisi kumpulan implementasi kode dengan bahasa pemrograman Python untuk menyelesaikan berbagai studi kasus pada materi pencarian (*searching*) dan pengurutan (*sorting*). 

Setiap file di dalam repositori ini merupakan solusi dari praktikum yang berfokus pada analisis kompleksitas waktu, optimasi algoritma dasar, dan manipulasi struktur data array/list.

## 📂 Daftar File dan Penjelasan

Berikut adalah rincian dari setiap file yang ada di dalam repositori ini:

### 1. `soal_1_modified_binary_search.py`
**Deskripsi:** Implementasi algoritma *Binary Search* yang dimodifikasi untuk menghitung total kemunculan (*occurrences*) dari sebuah nilai target di dalam array yang sudah terurut.
* **Mekanisme:** Pencarian dilakukan dua kali secara logaritmik untuk menemukan indeks kemunculan paling kiri (pertama) dan indeks kemunculan paling kanan (terakhir) dari elemen target.
* **Kompleksitas Waktu:** `O(log n)`

### 2. `soal_2_bubble_sort_analysis.py`
**Deskripsi:** Modifikasi dari algoritma pengurutan *Bubble Sort* konvensional untuk mengukur efisiensi langkah yang dilakukan.
* **Fitur Utama:**
  - Dilengkapi dengan *early termination* yang akan langsung menghentikan proses iterasi jika terdeteksi bahwa array sudah dalam keadaan terurut pada suatu *pass*.
  - Melacak dan mengembalikan data analisis berupa array terurut, total perbandingan (*comparisons*), total pertukaran elemen (*swaps*), dan jumlah iterasi utama (*passes*).

### 3. `soal_3_hybrid_sort.py`
**Deskripsi:** Implementasi fungsi pengurutan *hybrid* yang secara dinamis memilih algoritma pengurutan berdasarkan jumlah elemen.
* **Fitur Utama:**
  - Menerapkan *Insertion Sort* jika panjang sub-array kurang dari atau sama dengan nilai *threshold* (default: 10 elemen).
  - Menerapkan *Selection Sort* jika panjang sub-array lebih besar dari *threshold*.
  - Dilengkapi dengan pengujian komparatif untuk membandingkan total operasi antara metode *hybrid*, *pure insertion*, dan *pure selection* pada berbagai ukuran array acak.

### 4. `soal_4_merge_three_lists.py`
**Deskripsi:** Algoritma untuk menggabungkan tiga buah *list* yang sudah terurut menjadi satu *list* baru yang terurut secara keseluruhan.
* **Mekanisme:** Penggabungan diselesaikan murni dalam satu fase iterasi menggunakan teknik tiga *pointer* yang berjalan bersamaan di masing-masing *list*. Pendekatan ini menghindari pemanggilan fungsi *merge* dua *list* secara bertahap yang kurang efisien.
* **Kompleksitas Waktu:** `O(n)`

### 5. `soal_5_inversions_counter.py`
**Deskripsi:** Program untuk menghitung jumlah *inversion* dalam sebuah array (yaitu kondisi di mana terdapat pasangan indeks `i < j` namun nilai `arr[i] > arr[j]`). Jumlah ini menjadi metrik seberapa acak suatu array.
* **Fitur Utama:**
  - Menyediakan pendekatan `countInversionsNaive` (*Brute Force*) dengan iterasi bersarang.
  - Menyediakan pendekatan `countInversionsSmart` dengan memodifikasi fase *merge* pada *Merge Sort* untuk menghitung *inversion* secara instan.
  - Menyertakan pengujian perbandingan waktu eksekusi untuk mendemonstrasikan signifikansi perbedaan performa antara `O(n^2)` dan `O(n log n)` pada array berukuran besar.
