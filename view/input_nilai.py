from Model.daftar_nilai import tambah_data, hapus_data, ubah_data

def masukan_data():

    print("=== Silahkan masukan data ===")
    print()
    nama = input("Silahkan masukan nama :")
    nim = int(input("Silahkan Masukan NIM : "))
    tugas = int(input("Silahkan Masukan Nilai Tugas :"))
    uts = int(input("Silahkan Masukan Nilai UTS :"))
    uas = int(input("Silahkan Masukan Nilai UAS :"))
    akhir =(float(tugas) * 0.3) + (float(uts) * 0.35) + (float(uas) * 0.35)
    tambah_data(nama, nim, tugas, uts, uas, akhir)

def mencari_ubah():
    ubah_data(input("Masukan data yang ingin di ubah: "))

    print("=== Silahkan masukan data baru ===")
    print()
    nama = input("Silahkan masukan nama :")
    nim = int(input("Silahkan Masukan NIM : "))
    tugas = int(input("Silahkan Masukan Nilai Tugas :"))
    uts = int(input("Silahkan Masukan Nilai UTS :"))
    uas = int(input("Silahkan Masukan Nilai UAS :"))
    akhir = (float(tugas) * 0.3) + (float(uts) * 0.35) + (float(uas) * 0.35)
    tambah_data(nama, nim, tugas, uts, uas, akhir)


def mencari_hapus():
    hapus_data(input("Masukan nama untuk menghapus data : "))


