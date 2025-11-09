import unittest
from io import StringIO
from unittest.mock import patch
 
# Ubah import sesuai dengan nama berkas fungsi tambah_tugas berasal
from script import tambah_tugas
 
 
class TestTambahTugas(unittest.TestCase):
    def setUp(self):
        self.tugas = []
 
    def test_tambah_tugas_valid(self):
        input_values = ["Tugas 1", "Deskripsi 1", "Selesai", "60"]
        expected_output = "Tugas berhasil ditambahkan!\n"
 
        with patch("builtins.input", side_effect=input_values), patch(
            "sys.stdout", new_callable=StringIO
        ) as stdout:
            tambah_tugas(self.tugas)
            actual_output = stdout.getvalue()
 
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(len(self.tugas), 1)
        self.assertEqual(self.tugas[0]["title"], "Tugas 1")
 
 
if __name__ == "__main__":
    unittest.main()