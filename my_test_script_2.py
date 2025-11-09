# test_app.py

import unittest
from unittest.mock import patch

# Mengimpor fungsi yang akan diuji dari file utama
from script import tambah_tugas

class TestTambahTugas(unittest.TestCase):
    """Kelas untuk menguji fungsi tambah_tugas yang diimpor."""

    def setUp(self):
        """
        Siapkan data awal untuk pengujian. 
        PENTING: Kita menggunakan list terpisah agar pengujian tidak memengaruhi
        list 'tugas' yang ada di app_tugas.py secara permanen.
        """
        self.tugas_test_data = [
            {"id": 1, "title": "Tugas A", "status": "selesai", "description": "D", "estimasi_waktu_pengerjaan": 10},
            {"id": 2, "title": "Tugas B", "status": "belum selesai", "description": "D", "estimasi_waktu_pengerjaan": 20}
        ]
        self.initial_len = len(self.tugas_test_data)

    @patch('builtins.input')
    def test_a_tambah_tugas_valid(self, mock_input):
        """Menguji skenario input valid."""
        
        # Input: title, description, status, estimasi_waktu
        mock_input.side_effect = ["Tugas Sempurna", "Deskripsi Lulus", "selesai", "90"]
        
        # Panggil fungsi yang diuji dengan data uji
        tambah_tugas(self.tugas_test_data)
        
        # Assertions
        self.assertEqual(len(self.tugas_test_data), self.initial_len + 1, "Jumlah tugas harus bertambah 1.")
        self.assertEqual(self.tugas_test_data[-1]['id'], self.initial_len + 1, "ID harus auto-increment yang benar.")
        self.assertEqual(self.tugas_test_data[-1]['title'], "Tugas Sempurna")
        self.assertEqual(self.tugas_test_data[-1]['estimasi_waktu_pengerjaan'], 90)

    @patch('builtins.input')
    def test_b_tambah_tugas_validasi_gagal_lalu_berhasil(self, mock_input):
        """Menguji skenario input yang salah dan kemudian benar."""
        
        # Urutan input yang akan di-mock:
        mock_input.side_effect = [
            # 1. Judul kosong (Gagal) -> 2. Judul valid (Berhasil)
            "", "Tugas Validasi", 
            # 3. Deskripsi kosong (Gagal) -> 4. Deskripsi valid (Berhasil)
            "", "Deskripsi Valid",
            # 5. Status salah (Gagal) -> 6. Status valid (Berhasil)
            "di tengah", "belum selesai", 
            # 7. Estimasi non-angka (Gagal) -> 8. Estimasi <= 0 (Gagal) -> 9. Estimasi valid (Berhasil)
            "bukan angka", "0", "120"
        ]
        
        # Panggil fungsi yang diuji
        tambah_tugas(self.tugas_test_data)
        
        # Assertions
        self.assertEqual(len(self.tugas_test_data), self.initial_len + 1, "Tugas harus berhasil ditambahkan.")
        self.assertEqual(self.tugas_test_data[-1]['title'], "Tugas Validasi")
        self.assertEqual(self.tugas_test_data[-1]['estimasi_waktu_pengerjaan'], 120)

if __name__ == '__main__':
    unittest.main()