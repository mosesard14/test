def faktorial(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    
    
bil = int(input("Masukkan bilangan :"))
print(f"Hasil dari faktorial {bil} adalah = {faktorial(bil)}")
