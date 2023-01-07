from Model.daftar_nilai import database
from tabulate import tabulate


def lihat_data():
    print(tabulate(database.values(), headers=["Nama" ,"NIM" ,"Tugas" ,"UTS" ,"UAS" ,"Akhir"], tablefmt = "fancy_grid" ))

def cari(nama):
    Data_cari = {}
    for key, value in database.items():
        if nama in value:
            Data_cari[key] = value

    print(tabulate(Data_cari.values(), headers=["Nama", "NIM", "Tugas", "UTS", "UAS", "AKHIR"], tablefmt="fancy_grid"))

