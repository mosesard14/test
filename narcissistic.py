bilangan = int(input("Masukkan bilangan :"))

if bilangan > 0 and  bilangan < 10:
    print(f"{bilangan} Narcissistic")
elif bilangan >= 10 and bilangan < 100:
    puluhan = bilangan // 10
    satuan = bilangan % 10
    hasil = puluhan ** 2  + satuan ** 2
    if hasil == bilangan:
        print("Narcissistic")
    else:
        print("Bukan narcissistic")
elif bilangan >= 100 and bilangan < 1000:
    ratusan = bilangan // 100
    puluhan = (bilangan // 10) % 10
    satuan = bilangan % 10 
    hasil = ratusan ** 3 + puluhan ** 3 + satuan ** 3 
    if hasil == bilangan:
        print("bilangan Narcissistic")
    else: 
        print("bukan Narcissistic")