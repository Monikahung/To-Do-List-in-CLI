# --- FUNGSI UNTUK MELIHAT DAFTAR TUGAS ---
def lihat_tugas(tugas):
    # Fungsi ini bertugas untuk mencetak semua tugas yang ada dalam list 'tugas'.
    
    # Periksa apakah list tugas kosong.
    if not tugas:
        # Jika kosong, cetak pesan bahwa tidak ada tugas.
        print("Tidak ada tugas yang tersedia.")
        return # Keluar dari fungsi.
    
    print("Daftar Tugas:")
    # Melakukan perulangan untuk menampilkan detail dari setiap kamus (tugas_item) dalam list 'tugas'.
    for tugas_item in tugas:
        # Menggunakan f-string (f"...") untuk format cetak yang lebih mudah.
        # Mencetak ID dan judul tugas.
        print(f"- {tugas_item['id']}. {tugas_item['title']}")
        # Mencetak deskripsi dengan indentasi.
        print(f"  Deskripsi: {tugas_item['description']}")
        # Mencetak status tugas.
        print(f"  Status: {tugas_item['status']}")
        # Mencetak estimasi waktu pengerjaan.
        print(f"  Estimasi Waktu: {tugas_item['estimasi_waktu_pengerjaan']} menit")
        # Mencetak garis pemisah untuk keterbacaan.
        print("-" * 20)

# --- FUNGSI UNTUK MENAMBAH TUGAS BARU ---
def tambah_tugas(tugas):
    # Fungsi ini bertugas untuk mengambil input dari pengguna dan
    # menambahkan tugas baru ke dalam list 'tugas' yang sudah ada.
    # Parameter 'tugas' adalah list yang berisi dictionary-dictionary tugas.

    while True:
        # Mulai perulangan 'while True' untuk terus meminta input
        # sampai pengguna memasukkan judul yang valid.
        title = input("Masukkan judul tugas: ")
        
        # Periksa apakah 'title' tidak kosong (yaitu, pengguna tidak hanya menekan Enter)
        if title:
            break # Jika judul ada, keluar dari perulangan
        
        # Jika judul kosong, cetak pesan error dan perulangan akan diulang
        print("Judul tugas tidak boleh kosong. Silakan coba lagi.")

    while True:
        # Perulangan yang sama untuk memastikan 'description' tidak kosong.
        description = input("Masukkan deskripsi tugas: ")
        
        if description:
            break # Jika deskripsi ada, keluar dari perulangan
        
        print("Deskripsi tugas tidak boleh kosong. Silakan coba lagi.")

    while True:
        # Perulangan untuk memvalidasi input 'status'.
        # .lower() memastikan input dikonversi ke huruf kecil,
        # sehingga 'Selesai', 'selesai', atau 'SELESAI' akan diterima.
        status = input("Masukkan status tugas (Selesai/Belum Selesai): ").lower()
        
        # Periksa apakah status yang dimasukkan ada di dalam list yang diizinkan.
        if status in ["selesai", "belum selesai"]:
            break # Jika status valid, keluar dari perulangan
        
        print("Status tugas harus 'Selesai' atau 'Belum Selesai'. Silakan coba lagi.")

    while True:
        # Perulangan untuk memvalidasi 'estimasi_waktu_pengerjaan'.
        try:
            # Menggunakan 'try-except' untuk menangani kesalahan jika pengguna
            # memasukkan teks alih-alih angka (ValueError).
            estimasi_waktu = int(input("Masukkan estimasi waktu pengerjaan (menit): "))
            
            # Periksa apakah estimasi waktu adalah angka positif (lebih dari 0).
            if estimasi_waktu > 0:
                break # Jika angka valid, keluar dari perulangan
            
            print("Estimasi waktu harus lebih dari 0. Silakan coba lagi.")
        
        except ValueError:
            # Blok 'except' menangkap kesalahan jika int() tidak dapat
            # mengubah input menjadi angka.
            print("Estimasi waktu harus berupa angka. Silakan coba lagi.")

    # Setelah semua input tervalidasi, buat dictionary baru untuk tugas.
    new_task = {
        # 'id' diatur sebagai panjang list 'tugas' ditambah 1.
        # Ini memastikan ID selalu bertambah (auto-increment)
        # selama tidak ada tugas yang dihapus.
        "id": len(tugas) + 1,
        "title": title,
        "description": description,
        # Menyimpan status yang sudah dikonversi ke huruf kecil.
        "status": status,
        # Menyimpan estimasi waktu yang sudah dijamin berupa bilangan bulat positif.
        "estimasi_waktu_pengerjaan": estimasi_waktu
    }
    
    # Tambahkan (append) dictionary tugas baru ke list 'tugas'.
    tugas.append(new_task)
    
    # Beri tahu pengguna bahwa operasi telah berhasil.
    print("Tugas berhasil ditambahkan!")

# --- FUNGSI UNTUK MENANDAI TUGAS SELESAI ---
def tandai_selesai(tugas):
    # Fungsi ini mengubah status tugas menjadi "Selesai" berdasarkan ID yang dimasukkan.
    try:
        # Coba ambil input ID dan ubah ke integer.
        id_tugas = int(input("Masukkan ID tugas yang ingin ditandai selesai: "))
    except ValueError:
        # Tangani jika input bukan angka.
        print("ID tugas harus berupa angka.")
        return
    
    # Lakukan perulangan melalui setiap tugas dalam list.
    for tugas_item in tugas:
        # Periksa apakah 'id' tugas saat ini cocok dengan ID yang dicari.
        if tugas_item["id"] == id_tugas:
            # Jika cocok, perbarui statusnya.
            tugas_item["status"] = "Selesai"
            print("Tugas berhasil diperbarui menjadi selesai!")
            return # Keluar dari fungsi segera setelah pembaruan.
            
    # Baris ini hanya dijalankan jika perulangan selesai tanpa menemukan ID (return tidak terpanggil).
    print("ID tugas tidak ditemukan.")

# --- FUNGSI UNTUK MENGHAPUS TUGAS ---
def hapus_tugas(tugas):
    # Fungsi ini menghapus tugas dari list berdasarkan ID.
    
    # Panggil 'lihat_tugas' agar pengguna tahu ID mana yang harus dimasukkan.
    lihat_tugas(tugas) 
    
    try:
        # Coba ambil input ID dan ubah ke integer.
        id_tugas = int(input("Masukkan ID tugas yang ingin dihapus: "))
    except ValueError:
        # Tangani jika input bukan angka.
        print("ID tugas harus berupa angka.")
        return
    
    # Lakukan perulangan melalui setiap tugas dalam list.
    for tugas_item in tugas:
        # Periksa apakah 'id' tugas saat ini cocok dengan ID yang dicari.
        if tugas_item["id"] == id_tugas:
            # Jika cocok, gunakan method .remove() untuk menghapus kamus dari list.
            tugas.remove(tugas_item)
            print("Tugas berhasil dihapus!")
            return # Keluar dari fungsi setelah penghapusan berhasil.
            
    # Baris ini hanya dijalankan jika ID tidak ditemukan.
    print("ID tugas tidak ditemukan.")

# --- DATA AWAL: LIST TUGAS ---
# Mendefinisikan list global yang akan menyimpan semua dictionary tugas.
tugas = [
    {
        "id": 1,
        "title": "Mengerjakan PR Matematika",
        "description": "Halaman 20-25",
        "status": "Belum Selesai",
        "estimasi_waktu_pengerjaan": 30
    },
    {
        "id": 2,
        "title": "Membeli bahan makanan",
        "description": "Daftar belanja ada di catatan",
        "status": "Selesai",
        "estimasi_waktu_pengerjaan": 60
    },
    {
        "id": 3,
        "title": "Mencuci mobil",
        "description": "Gunakan sabun khusus",
        "status": "Selesai",
        "estimasi_waktu_pengerjaan": 60
    },
    {
        "id": 4,
        "title": "Membaca buku",
        "description": "Bab 3 dan 4",
        "status": "Belum Selesai",
        "estimasi_waktu_pengerjaan": 45
    },
    {
        "id": 5,
        "title": "Menulis esai",
        "description": "Tema bebas, minimal 3 halaman",
        "status": "Selesai",
        "estimasi_waktu_pengerjaan": 60
    },
    {
        "id": 6,
        "title": "Pergi ke gym",
        "description": "Lakukan latihan kardio",
        "status": "Belum Selesai",
        "estimasi_waktu_pengerjaan": 45
    }
]

# --- FUNGSI UNTUK MENAMPILKAN MENU UTAMA ---
def menu():
    # Fungsi ini hanya bertugas menampilkan opsi menu kepada pengguna.
    print("Selamat Datang di Aplikasi To-Do List")
    print("1. Lihat Semua Tugas")
    print("2. Tambah Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")

# --- FUNGSI UTAMA (MAIN LOOP) ---
def main():
    # Fungsi utama yang menjalankan aplikasi dan menangani interaksi menu.
    
    while True: # Perulangan tanpa henti (infinite loop) hingga pengguna memilih keluar.
        menu() # Panggil fungsi untuk menampilkan menu.
        choice = input("Masukkan pilihan Anda: ") # Ambil pilihan dari pengguna.

        # Menggunakan struktur if/elif/else untuk menjalankan fungsi yang sesuai dengan pilihan.
        if choice == '1':
            # Pilihan 1: Menampilkan semua tugas.
            lihat_tugas(tugas)
        elif choice == '2':
            # Pilihan 2: Menambahkan tugas baru.
            tambah_tugas(tugas)
        elif choice == '3':
            # Pilihan 3: Menandai tugas sebagai selesai.
            tandai_selesai(tugas)
        elif choice == '4':
            # Pilihan 4: Menghapus tugas.
            hapus_tugas(tugas)
        elif choice == '5':
            # Pilihan 5: Keluar dari perulangan 'while True'.
            break
        else:
            # Jika pilihan tidak valid (bukan 1-5).
            print("Pilihan tidak valid. Silakan coba lagi.")

# --- TITIK AWAL EKSEKUSI PROGRAM ---
# Baris ini adalah konvensi standar Python.
# Ia memastikan bahwa fungsi 'main()' hanya dipanggil ketika skrip dijalankan secara langsung.
if __name__ == "__main__":
    main()