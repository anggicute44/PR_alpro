
emas1= float(input("Masukkan jumlah gram emas awal: "))
harga_awal = float(input("Masukkan harga beli per gram awal: "))
hargasekarang1 = float(input("Masukkan harga emas setelah kenaikan pertama: "))


modal_awal = emas1 * harga_awal
nilai_sekarang1 = emas1 * hargasekarang1


keuntungan1rp = nilai_sekarang1 - modal_awal
keuntungan1_persen = (keuntungan1rp / modal_awal) * 100

emasTambah = float(input("Masukkan jumlah gram emas yang dibeli lagi: "))
harga_tambah = hargasekarang1  
harga_sekarang2 = float(input("Masukkan harga emas setelah kenaikan kedua: "))


modal_tambah = emasTambah * harga_tambah
total_modal = modal_awal + modal_tambah
total_gram = emas1 + emasTambah
nilai_sekarang2 = total_gram * harga_sekarang2


keuntungan2rp = nilai_sekarang2 - total_modal
keuntungan2persen = (keuntungan2rp / total_modal) * 100

print("inputan pembelian emas pertama:")
print(f"Keuntungan dalam Rupiah: Rp{keuntungan1rp:}")
print(f"Keuntungan dalam Persen: {keuntungan1_persen:}%")

print("inputan pembelian emas kedua setelah membeli tambahan emas:")
print(f"Keuntungan dalam Rupiah: Rp{keuntungan2rp:}")
print(f"Keuntungan dalam Persen: {keuntungan2persen:}%")
