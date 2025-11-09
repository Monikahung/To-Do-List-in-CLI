# To-Do List CLI

To-Do List CLI adalah aplikasi berbasis command-line yang memungkinkan pengguna untuk mengelola daftar tugas dengan mudah. Aplikasi ini mendukung penambahan, penghapusan, dan pembaruan status tugas.



## Fitur

- Lihat Semua Tugas: Menampilkan daftar tugas beserta ID, judul, deskripsi, status, dan estimasi waktu pengerjaan.

- Tambah Tugas: Memungkinkan pengguna untuk menambahkan tugas baru ke dalam daftar.

- Tandai Tugas Selesai: Mengubah status tugas menjadi "Selesai".

- Hapus Tugas: Menghapus tugas dari daftar.



## Instalasi

Pastikan Anda memiliki Python 3 terinstal di sistem Anda. Setelah itu, unduh source code aplikasi proyek ini, lalu jalankan aplikasi dengan command ```python todo.py```



## Cara Penggunaan

Setelah menjalankan aplikasi, Anda akan melihat menu berikut:

```

Selamat Datang di Aplikasi To-Do List

1. Lihat Semua Tugas

2. Tambah Tugas

3. Tandai Tugas Selesai

4. Hapus Tugas

5. Keluar

```

Pilih opsi yang diinginkan dengan memasukkan nomor yang sesuai.



### Menambahkan Tugas

1. Pilih opsi Tambah Tugas.

2. Masukkan judul, deskripsi, status ("Selesai" atau "Belum Selesai"), dan estimasi waktu pengerjaan dalam menit.

3. Tugas akan ditambahkan ke daftar.



### Menandai Tugas Selesai

1. Pilih opsi Tandai Tugas Selesai.

2. Masukkan ID tugas yang ingin diperbarui.

3. Status tugas akan diubah menjadi "Selesai".



### Menghapus Tugas

1. Pilih opsi Hapus Tugas.

2. Masukkan ID tugas yang ingin dihapus.

3. Tugas akan dihapus dari daftar.



## Struktur Data

Setiap tugas direpresentasikan dalam dictionary dengan format berikut:

```python

{

    "id": 1,

    "title": "Mengerjakan PR Matematika",

    "description": "Halaman 20-25",

    "status": "Belum Selesai",

    "estimasi_waktu_pengerjaan": 30

}

```

ID tugas dihasilkan secara otomatis (auto-increment) untuk mempermudah pengelolaan.



???? Selamat menggunakan To-Do List CLI! Jika ada pertanyaan atau saran, silakan hubungi kami. Happy coding! ????