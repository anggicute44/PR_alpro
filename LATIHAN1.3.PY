import math


S_awal = 200_000_000  
S_akhir = 400_000_000 
bunga_persen = 0.1          
bunga_pertahun = 1            


t = math.log(S_akhir / S_awal) / (bunga_pertahun * math.log(1 + bunga_persen / bunga_pertahun))


print(f"Waktu yang dibutuhkan: {t:} tahun")
