def lihat_tugas(tugas):
    if not tugas:
        print("Tidak ada tugas yang tersedia.")
        return
 
    print("Daftar Tugas:")
    for tugas_item in tugas:
        print(f"- {tugas_item['id']}. {tugas_item['title']}")
        print(f"  Deskripsi: {tugas_item['description']}")
        print(f"  Status: {tugas_item['status']}")
        print(f"  Estimasi Waktu: {tugas_item['estimasi_waktu_pengerjaan']} menit")
        print("-" * 20)  # Garis pemisah antar tugas
 
def tambah_tugas(tugas):
    while True:
        title = input("Masukkan judul tugas: ")
        if title:  # Judul tidak boleh kosong
            break
        print("Judul tugas tidak boleh kosong. Silakan coba lagi.")
 
    while True:
        description = input("Masukkan deskripsi tugas: ")
        if description:  # Deskripsi tidak boleh kosong
            break
        print("Deskripsi tugas tidak boleh kosong. Silakan coba lagi.")
 
    while True:
        status = input("Masukkan status tugas (Selesai/Belum Selesai): ").lower()
        if status in ["selesai", "belum selesai"]:
            break
        print("Status tugas harus 'Selesai' atau 'Belum Selesai'. Silakan coba lagi.")
 
    while True:
        try:
            estimasi_waktu = int(input("Masukkan estimasi waktu pengerjaan (menit): "))
            if estimasi_waktu > 0:  # Estimasi waktu harus lebih dari 0
                break
            print("Estimasi waktu harus lebih dari 0. Silakan coba lagi.")
        except ValueError:
            print("Estimasi waktu harus berupa angka. Silakan coba lagi.")
 
    new_task = {
        "id": len(tugas) + 1,  # Auto-increment ID
        "title": title,
        "description": description,
        "status": status,
        "estimasi_waktu_pengerjaan": estimasi_waktu
    }
    tugas.append(new_task)
    print("Tugas berhasil ditambahkan!")
 
def tandai_selesai(tugas):
    try:
        id_tugas = int(input("Masukkan ID tugas yang ingin ditandai selesai: "))
    except ValueError:
        print("ID tugas harus berupa angka.")
        return
 
    for tugas_item in tugas:
        if tugas_item["id"] == id_tugas:
            tugas_item["status"] = "Selesai"
            print("Tugas berhasil diperbarui menjadi selesai!")
            return
    print("ID tugas tidak ditemukan.")
 
def hapus_tugas(tugas):
    lihat_tugas(tugas)
    try:
        id_tugas = int(input("Masukkan ID tugas yang ingin dihapus: "))
    except ValueError:
        print("ID tugas harus berupa angka.")
        return
 
    for tugas_item in tugas:
        if tugas_item["id"] == id_tugas:
            tugas.remove(tugas_item)
            print("Tugas berhasil dihapus!")
            return
    print("ID tugas tidak ditemukan.")
 
# List untuk menyimpan tugas
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
 
def menu():
    print("Selamat Datang di Aplikasi To-Do List")
    print("1. Lihat Semua Tugas")
    print("2. Tambah Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")
 
def main():
 
    while True:
        menu()
        choice = input("Masukkan pilihan Anda: ")
 
        if choice == '1':
            # Logika untuk menampilkan tugas
            lihat_tugas(tugas)
        elif choice == '2':
            # Logika untuk menambahkan tugas
            tambah_tugas(tugas)
        elif choice == '3':
            # Logika untuk menandai tugas selesai
            tandai_selesai(tugas)
        elif choice == '4':
            # Logika untuk menghapus tugas
            hapus_tugas(tugas)
        elif choice == '5':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
 
if __name__ == "__main__":
    main()