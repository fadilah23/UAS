

while True:
    print("==========================")
    print("=======Daftar Menu=======")
    print("==========================")
    print()
    print("1.Tambah data(t)")
    print("2.Ubah data(u)")
    print("3.Hapus data(h)")
    print("4.Cari data(c)")
    print("5.Lihat semua data(l)")
    print("6.Keluar(k)")
    print()

    pilihan = input("Silahkan pilih menu: ")

    if pilihan == "t":
        from view.input_nilai import masukan_data
        masukan_data()


    elif pilihan == "u":
        from view.input_nilai import mencari_ubah
        mencari_ubah()

    elif pilihan == "h":
        from view.input_nilai import mencari_hapus
        mencari_hapus()

    elif pilihan == 'c':
        from Model.daftar_nilai import cari_data
        cari_data()

    elif pilihan == "l":
        from view.view_nilai import lihat_data
        lihat_data()

    elif pilihan == "k":
        print("Terima Kasih Telah menggunakan Program ini ")
        break

    else :
        print("Masukan Pilihan menu yang benar ")