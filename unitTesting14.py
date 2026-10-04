import unittest

undo_stack = []


def simpan_aktivitas(aktivitas):
    undo_stack.append(aktivitas)


def undo():
    if len(undo_stack) == 0:
        return "Tidak ada aktivitas"
    else:
        return undo_stack.pop()


def lihat_aktivitas_terakhir():
    if len(undo_stack) == 0:
        return "Belum ada aktivitas"
    else:
        return undo_stack[-1]


def cek_undo_kosong():
    if len(undo_stack) == 0:
        return "Stack kosong"
    else:
        return "Stack masih memiliki aktivitas"


# =========================
# UNIT TESTING UNDO
# =========================

class TestUndo(unittest.TestCase):

    # 1. Tambah mahasiswa Citra
    def test_tambah_mahasiswa_citra(self):
        undo_stack.clear()

        simpan_aktivitas("Menambahkan mahasiswa Citra")

        self.assertEqual(
            undo_stack[-1],
            "Menambahkan mahasiswa Citra"
        )

    # 2. Undo aktivitas terakhir
    def test_undo_aktivitas_terakhir(self):
        undo_stack.clear()

        simpan_aktivitas("Menambahkan mahasiswa Citra")

        hasil = undo()

        self.assertEqual(
            hasil,
            "Menambahkan mahasiswa Citra"
        )

    # 3. Aktivitas terakhir
    def test_aktivitas_terakhir(self):
        undo_stack.clear()

        simpan_aktivitas("Menambahkan mahasiswa Citra")

        self.assertEqual(
            lihat_aktivitas_terakhir(),
            "Menambahkan mahasiswa Citra"
        )

    # 4. Stack kosong
    def test_stack_kosong(self):
        undo_stack.clear()

        self.assertEqual(
            cek_undo_kosong(),
            "Stack kosong"
        )


if __name__ == "__main__":
    unittest.main()