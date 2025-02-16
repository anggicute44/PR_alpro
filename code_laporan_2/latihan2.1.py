
tinggi = float(input("Masukkan tinggi badan dalam satuan (cm): "))
tinggi_m = tinggi / 100  
bmi = float(input("Masukkan nilai BMI yang diharapkan: "))
beratbadan = bmi * (tinggi_m ** 2)
print(f"Berat badan untuk BMI {bmi}: {beratbadan:} kg")
