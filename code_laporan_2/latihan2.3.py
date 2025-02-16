print("Mengatur keuangan Budi")
Gajiperjam = int(input("gaji per jam: "))
jamkerjasetiapminggu = int(input("Jumlah jam kerja dalam 1 minggu: "))
gajisetiapminggu = jamkerjasetiapminggu * Gajiperjam
aagajibudi = 5 * gajisetiapminggu

bbbgajibudi = aagajibudi - (aagajibudi * (100 / 14))
uangpakain = bbbgajibudi * (100 / 10)
uangalattulis = bbbgajibudi * (100 / 1)
hasil = bbbgajibudi - uangpakain - uangalattulis

untuksedekah = hasil * (100 / 25)
untukanakyatim = untuksedekah * (100 / 30)
untukkaumdhufa = untuksedekah * (100 / 70)

pajakpendapatan = int(aagajibudi)
pajakpotonganpendapatan = int(bbbgajibudi)
uangpakain = int(uangpakain)
uangalattulis = int(uangalattulis)
untuksedekah = int(untuksedekah)
untukanakyatim = int(untukanakyatim)
untukkaumdhufa = int(untukkaumdhufa)

print("\n=== Hasil Perhitungan Keuangan Budi ===")
print(f"Pajak Pendapatan: {pajakpendapatan}")
print(f"Pajak Setelah Potongan: {pajakpotonganpendapatan}")
print(f"Uang untuk pakaian: {uangpakain}")
print(f"Uang untuk alat tulis: {uangalattulis}")
print(f"Uang untuk sedekah: {untuksedekah}")
print(f"Uang untuk anak yatim: {untukanakyatim}")
print(f"Uang untuk kaum dhuafa: {untukkaumdhufa}")
