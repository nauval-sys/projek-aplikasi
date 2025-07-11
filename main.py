from data_handler import baca_data
from transaksi_ops import (
    buat_transaksi,
    lihat_transaksi,
    edit_transaksi,
    hapus_transaksi
)
from laporan_ops import tampilkan_laporan

def menu_utama():
    data = baca_data()
    while True:
        print("\n=== Aplikasi Catatan Keuangan ===")
        print("1. Tambah Transaksi")
        print("2. Lihat Transaksi")
        print("3. Edit Transaksi")
        print("4. Hapus Transaksi")
        print("5. Laporan")
        print("6. Keluar")
        pilih = input("Pilih menu (1-6): ")

        if pilih == "1":
            buat_transaksi(data)
        elif pilih == "2":
            lihat_transaksi(data)
        elif pilih == "3":
            edit_transaksi(data)
        elif pilih == "4":
            hapus_transaksi(data)
        elif pilih == "5":
            tampilkan_laporan(data)
        elif pilih == "6":
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("❌ Pilihan salah.")

if __name__ == "__main__":
    menu_utama()
