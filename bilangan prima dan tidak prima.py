bil = int(input("Masukkan bilangan bulat: "))
def cek_prima(n):
    if n < 2:
        return False 
    for i in range(2, int(n**0.5) + 1):
        if n % 2 == 0:
            return False
    return True
        
if cek_prima(bil):
    print(f"{bil} bilangan prima")
else:
    print(f"{bil} bukan bilangan prima")
