# --- test_tugas.py ---

import io
from contextlib import redirect_stdout
# Mengimpor fungsi yang akan diuji dari file tugas_module.py
from script import lihat_tugas

def jalankan_test_lihat_tugas_otomatis():
    """
    Menjalankan serangkaian test case untuk fungsi lihat_tugas
    dan membandingkan output yang dicetak dengan output yang diharapkan.
    """
    print("=========================================")
    print("  MEMULAI PENGUJIAN OTOMATIS lihat_tugas")
    print("=========================================")
    
    # ----------------------------------------------------
    # TEST CASE 1: Daftar Tugas Kosong
    # ----------------------------------------------------
    nama_test = "Daftar Kosong"
    tugas_kosong = []
    
    # Output yang diharapkan:
    expected_output_1 = "Tidak ada tugas yang tersedia.\n"
    
    # Menangkap output aktual
    f = io.StringIO()
    with redirect_stdout(f):
        lihat_tugas(tugas_kosong)
    actual_output_1 = f.getvalue()
    
    # Membandingkan dan mencetak hasil
    print(f"\n--- TEST CASE 1: {nama_test} ---")
    if actual_output_1 == expected_output_1:
        print(f"✅ LULUS: Output sesuai harapan.")
    else:
        print(f"❌ GAGAL: Output tidak sesuai.")
        print(f"   Diharapkan: {repr(expected_output_1)}")
        print(f"   Aktual:     {repr(actual_output_1)}")

    # ----------------------------------------------------
    # TEST CASE 2: Daftar dengan Satu Tugas (Normal)
    # ----------------------------------------------------
    nama_test = "Satu Tugas Normal"
    tugas_satu = [
        {
            "id": 101,
            "title": "Memperbarui CV",
            "description": "Menambahkan pengalaman proyek terbaru.",
            "status": "Belum Selesai",
            "estimasi_waktu_pengerjaan": 45
        }
    ]
    
    # Output yang diharapkan (harus sama persis termasuk spasi dan baris baru):
    # **PENTING: Pastikan spasi indentasi di sini sama persis dengan yang ada di fungsi lihat_tugas**
    expected_output_2 = (
        "Daftar Tugas:\n"
        "- 101. Memperbarui CV\n"
        "  Deskripsi: Menambahkan pengalaman proyek terbaru.\n"
        "  Status: Belum Selesai\n"
        "  Estimasi Waktu: 45 menit\n"
        "--------------------\n"
    )

    # Menangkap output aktual
    f = io.StringIO()
    with redirect_stdout(f):
        lihat_tugas(tugas_satu)
    actual_output_2 = f.getvalue()
    
    # Membandingkan dan mencetak hasil
    print(f"\n--- TEST CASE 2: {nama_test} ---")
    if actual_output_2 == expected_output_2:
        print(f"✅ LULUS: Output sesuai harapan.")
    else:
        print(f"❌ GAGAL: Output tidak sesuai.")
        print(f"   Diharapkan: {repr(expected_output_2)}")
        print(f"   Aktual:     {repr(actual_output_2)}")
        
    print("\n=========================================")
    print("          PENGUJIAN SELESAI")
    print("=========================================")

# Panggil fungsi pengujian untuk menjalankannya
if __name__ == "__main__":
    jalankan_test_lihat_tugas_otomatis()