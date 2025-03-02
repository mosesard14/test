try:
    bilangan = int(input("Masukkan bilangan: "))
    if bilangan > 0 and  bilangan < 10:
        print(f"{bilangan} adalah Narcissistic")
    elif bilangan >= 10 and bilangan < 100:
        puluhan = bilangan // 10
        satuan = bilangan % 10
        hasil = puluhan ** 2  + satuan ** 2
        if hasil == bilangan:
            print(f"{bilangan} adalah Narcissistic")
        else:
            print(f"{bilangan} Bukan narcissistic")
    elif bilangan >= 100 and bilangan < 1000:
        ratusan = bilangan // 100
        puluhan = (bilangan // 10) % 10
        satuan = bilangan % 10 
        hasil = ratusan ** 3 + puluhan ** 3 + satuan ** 3 
        if hasil == bilangan:
            print(f"{bilangan} adalah Narcissistic")
        else: 
            print(f"{bilangan} Bukan narcissistic")
except:
    print("Anda tidak memasukkan bilangan")