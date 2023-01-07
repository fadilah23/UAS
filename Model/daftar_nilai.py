
database = {}

def tambah_data(nama, nim, tugas, uas, uts, akhir):
    database[nama] = nama, nim, tugas, uas, uts, akhir

def hapus_data(nama):

    if nama in database.keys():
        del database[nama]
        print("Data {} telah dihapus ".format(nama))
        return True
    else:
        print("| Data {} tidak ditemukan |".format(nama))
        return False

def ubah_data(nama):
    if nama in database.keys():
        del database[nama]

def cari_data():
    from view.view_nilai import cari
    cari(input("Masukan nama yang ingi di cari : "))












