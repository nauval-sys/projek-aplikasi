from data_handler import simpan_data

def buat_transaksi(records):
    tgl = input("Tanggal (YYYY-MM-DD): ")
    tipe = input("Tipe transaksi (pemasukan/pengeluaran): ").strip().lower()
    kat = input("Kategori: ")
    nominal = input("Nominal: ")

    baru = {
        "tanggal": tgl,
        "jenis": tipe,
        "kategori": kat,
        "nominal": nominal
    }
    records.append(baru)
    simpan_data(records)
    print("✅ Transaksi berhasil ditambahkan.")

def lihat_transaksi(records):
    if not records:
        print("Belum ada transaksi.")
        return

    print("\nFilter:")
    print("1. Semua")
    print("2. Berdasarkan Bulan")
    print("3. Berdasarkan Tahun")
    opsi = input("Pilih (1-3): ")

    if opsi == "1":
        hasil = records
    elif opsi == "2":
        periode = input("Masukkan periode (YYYY-MM): ")
        hasil = [r for r in records if r["tanggal"].startswith(periode)]
    elif opsi == "3":
        tahun = input("Masukkan tahun (YYYY): ")
        hasil = [r for r in records if r["tanggal"].startswith(tahun)]
    else:
        print("Pilihan tidak valid.")
        return

    if not hasil:
        print("Tidak ditemukan data sesuai filter.")
        return

    print("\nTransaksi:")
    for idx, r in enumerate(hasil, start=1):
        print(f"{idx}. {r['tanggal']} | {r['jenis']} | {r['kategori']} | Rp{r['nominal']}")

def edit_transaksi(records):
    lihat_transaksi(records)
    try:
        nomor = int(input("Nomor transaksi yang ingin diedit: ")) - 1
        lama = records[nomor]
    except:
        print("Nomor tidak valid.")
        return

    print("Data saat ini:")
    for k, v in lama.items():
        print(f"{k.capitalize()}: {v}")

    print("Masukkan data baru (biarkan kosong jika tidak ingin diubah):")
    tgl = input("Tanggal: ") or lama["tanggal"]
    tipe = input("Jenis: ") or lama["jenis"]
    kat = input("Kategori: ") or lama["kategori"]
    nominal = input("Nominal: ") or lama["nominal"]

    records[nomor] = {
        "tanggal": tgl,
        "jenis": tipe,
        "kategori": kat,
        "nominal": nominal
    }
    simpan_data(records)
    print("✅ Transaksi berhasil diperbarui.")

def hapus_transaksi(records):
    lihat_transaksi(records)
    try:
        idx = int(input("Nomor transaksi yang ingin dihapus: ")) - 1
        del records[idx]
        simpan_data(records)
        print("🗑️ Transaksi dihapus.")
    except:
        print("Nomor tidak valid.")
