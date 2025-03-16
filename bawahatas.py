bawah = int(input('bawah: '))
atas = int(input('atas: '))
def ganjil(bawah, atas):
    if bawah < atas:
        hasil = bawah + 1 if bawah % 2 == 0 else bawah
        while hasil < atas:
            print(hasil, end=', ' if hasil + 2 < atas else '.')
            hasil += 2
    else:
        hasil = bawah - 1 if bawah % 2 == 0 else bawah
        while hasil > atas:
            print(hasil, end=', ' if hasil - 2 > atas else '.')
            hasil -= 2
ganjil(bawah, atas)