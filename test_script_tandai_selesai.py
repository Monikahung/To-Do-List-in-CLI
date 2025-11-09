import unittest
from io import StringIO
from unittest.mock import patch
 
# Ubah import sesuai dengan nama berkas fungsi tandai_selesai berasal
from script import tandai_selesai
 
 
class TestTandaiSelesai(unittest.TestCase):
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
 
    def test_tandai_selesai_valid(self):
        input_values = ["1"]
        expected_output = "Tugas berhasil diperbarui menjadi selesai!\n"
 
        with patch("builtins.input", side_effect=input_values), patch(
            "sys.stdout", new_callable=StringIO
        ) as stdout:
            tandai_selesai(self.tugas)
            actual_output = stdout.getvalue()
 
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(self.tugas[0]["status"], "Selesai")
 
    def test_tandai_selesai_tidak_valid(self):
        input_values = ["3"]
        expected_output = "ID tugas tidak ditemukan.\n"
 
        with patch("builtins.input", side_effect=input_values), patch(
            "sys.stdout", new_callable=StringIO
        ) as stdout:
            tandai_selesai(self.tugas)
            actual_output = stdout.getvalue()
 
        self.assertEqual(actual_output, expected_output)
 
 
if __name__ == "__main__":
    unittest.main()