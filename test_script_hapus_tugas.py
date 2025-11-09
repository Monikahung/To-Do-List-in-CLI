import unittest
from io import StringIO
from unittest.mock import patch
 
# Ubah import sesuai dengan nama berkas fungsi hapus_tugas berasal
from script import hapus_tugas
 
 
class TestHapusTugas(unittest.TestCase):
    def setUp(self):
        self.tugas = [
            {
                "id": 1,
                "title": "Tugas 1",
                "description": "Deskripsi 1",
                "status": "Belum Selesai",
                "estimasi_waktu_pengerjaan": 60,
            },
            {
                "id": 2,
                "title": "Tugas 2",
                "description": "Deskripsi 2",
                "status": "Belum Selesai",
                "estimasi_waktu_pengerjaan": 120,
            },
        ]
 
    def test_hapus_tugas_valid(self):
        input_values = ["1"]
        expected_output = """Daftar Tugas:
- 1. Tugas 1
  Deskripsi: Deskripsi 1
  Status: Belum Selesai
  Estimasi Waktu: 60 menit
--------------------
- 2. Tugas 2
  Deskripsi: Deskripsi 2
  Status: Belum Selesai
  Estimasi Waktu: 120 menit
--------------------
Tugas berhasil dihapus!
"""
 
        with patch("builtins.input", side_effect=input_values), patch(
            "sys.stdout", new_callable=StringIO
        ) as stdout:
            hapus_tugas(self.tugas)
            actual_output = stdout.getvalue()
 
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(len(self.tugas), 1)
        self.assertEqual(self.tugas[0]["id"], 2)
 
    def test_hapus_tugas_tidak_valid(self):
        input_values = ["3"]
        expected_output = """Daftar Tugas:
- 1. Tugas 1
  Deskripsi: Deskripsi 1
  Status: Belum Selesai
  Estimasi Waktu: 60 menit
--------------------
- 2. Tugas 2
  Deskripsi: Deskripsi 2
  Status: Belum Selesai
  Estimasi Waktu: 120 menit
--------------------
ID tugas tidak ditemukan.
"""
 
        with patch("builtins.input", side_effect=input_values), patch(
            "sys.stdout", new_callable=StringIO
        ) as stdout:
            hapus_tugas(self.tugas)
            actual_output = stdout.getvalue()
 
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(len(self.tugas), 2)
 
 
if __name__ == "__main__":
    unittest.main()