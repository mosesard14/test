def kalkulatorRusak(angka1, angka2, angka3):
    if angka1 == 0 or angka2 == 0 or angka3 == 0:
        print('Error, angka tidak boleh 0')

    ang1 = angka1
    while ang1 >= 10:
        ang1 // 10
    return(ang1)

    ang2 = angka2
    while ang2 >= 10:
        ang2 // 10
    return(ang2)

    ang3= angka3
    while ang3 >= 10:
        ang3 // 10
    return(ang3)

    hasil = ang1 * ang2 * ang3 
print
