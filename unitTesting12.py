import unittest
from collections import deque

# =========================
# SISTEM ANTRIAN
# =========================

antrian = deque()


def tambah_mahasiswa(nomor, nama):
    data = {
        "nomor": nomor,
        "nama": nama
    }
    antrian.append(data)


def layani_mahasiswa():
    if len(antrian) == 0:
        return "Queue kosong"
    else:
        mahasiswa = antrian.popleft()
        return mahasiswa["nama"]


def lihat_terdepan():
    if len(antrian) == 0:
        return "Queue kosong"
    else:
        return antrian[0]["nama"]


def cek_antrian_kosong():
    if len(antrian) == 0:
        return "Queue kosong"
    else:
        return "Queue masih memiliki data"


# =========================
# UNIT TESTING QUEUE
# =========================

class TestAntrian(unittest.TestCase):

    # 1. Penambahan data
    def test_penambahan_data(self):
        antrian.clear()

        tambah_mahasiswa("001", "Fajar")

        self.assertEqual(antrian[0]["nama"], "Fajar")

    # 2. Penghapusan data
    def test_penghapusan_data(self):
        antrian.clear()

        tambah_mahasiswa("001", "Fajar")

        hasil = layani_mahasiswa()

        self.assertEqual(hasil, "Fajar")

    # 3. Melihat data terdepan
    def test_melihat_data_terdepan(self):
        antrian.clear()

        tambah_mahasiswa("001", "Fajar")
        tambah_mahasiswa("002", "Bima")

        hasil = layani_mahasiswa()

        self.assertEqual(hasil, "Fajar")

        hasil_depan = lihat_terdepan()

        self.assertEqual(hasil_depan, "Bima")

    # 4. Memeriksa kondisi kosong
    def test_memeriksa_kondisi_kosong(self):
        antrian.clear()

        hasil = cek_antrian_kosong()

        self.assertEqual(hasil, "Queue kosong")


if __name__ == "__main__":
    unittest.main()