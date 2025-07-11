def tampilkan_laporan(records):
    total_in = 0
    total_out = 0
    pengeluaran_kat = {}

    for rec in records:
        nominal = int(rec["nominal"])
        if rec["jenis"] == "pemasukan":
            total_in += nominal
        elif rec["jenis"] == "pengeluaran":
            total_out += nominal
            k = rec["kategori"]
            pengeluaran_kat[k] = pengeluaran_kat.get(k, 0) + nominal

    saldo = total_in - total_out

    print("\n📊 Ringkasan Keuangan")
    print(f"Pemasukan: Rp{total_in}")
    print(f"Pengeluaran: Rp{total_out}")
    print(f"Saldo: Rp{saldo}")
    if pengeluaran_kat:
        print("Rincian Pengeluaran per Kategori:")
        for k, v in pengeluaran_kat.items():
            print(f"- {k}: Rp{v}")
