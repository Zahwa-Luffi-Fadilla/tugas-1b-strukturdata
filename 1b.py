from collections import deque


# =========================
# SISTEM ANTRIAN MAHASISWA
# =========================

antrian = deque()


def tambah_mahasiswa(nomor, nama):
    data = {
        "nomor": nomor,
        "nama": nama
    }
    antrian.append(data)
    print(f"Mahasiswa {nama} berhasil ditambahkan.")


def layani_mahasiswa():
    if len(antrian) == 0:
        print("Antrian kosong.")
    else:
        mahasiswa = antrian.popleft()
        print(f"Mahasiswa yang dilayani: {mahasiswa['nama']}")


def lihat_terdepan():
    if len(antrian) == 0:
        print("Antrian kosong.")
    else:
        print(f"Mahasiswa terdepan: {antrian[0]['nama']}")


def cek_antrian_kosong():
    if len(antrian) == 0:
        print("Antrian kosong.")
    else:
        print("Antrian masih memiliki data.")


# =========================
# FITUR UNDO
# =========================

undo_stack = []


def simpan_aktivitas(aktivitas):
    undo_stack.append(aktivitas)
    print(f"Aktivitas disimpan: {aktivitas}")


def undo():
    if len(undo_stack) == 0:
        print("Tidak ada aktivitas yang dapat dibatalkan.")
    else:
        aktivitas = undo_stack.pop()
        print(f"Undo: {aktivitas}")


def lihat_aktivitas_terakhir():
    if len(undo_stack) == 0:
        print("Belum ada aktivitas.")
    else:
        print(f"Aktivitas terakhir: {undo_stack[-1]}")


def cek_undo_kosong():
    if len(undo_stack) == 0:
        print("Stack Undo kosong.")
    else:
        print("Stack Undo masih memiliki aktivitas.")


# =========================
# SIMULASI ANTRIAN
# =========================

print("=== SIMULASI ANTRIAN ===")

tambah_mahasiswa("001", "Aulia")
tambah_mahasiswa("002", "Bima")
tambah_mahasiswa("003", "Citra")

lihat_terdepan()

layani_mahasiswa()

tambah_mahasiswa("004", "Dimas")

cek_antrian_kosong()


# =========================
# SIMULASI UNDO
# =========================

print("\n=== SIMULASI UNDO ===")

simpan_aktivitas("Menambahkan mahasiswa Aulia")
simpan_aktivitas("Menambahkan mahasiswa Bima")
simpan_aktivitas("Menghapus mahasiswa Aulia")
simpan_aktivitas("Menghapus mahasiswa Bima")

lihat_aktivitas_terakhir()

undo()

lihat_aktivitas_terakhir()

undo()

cek_undo_kosong()