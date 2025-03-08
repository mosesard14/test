def cek_angka(a, b, c):
    if a != b and a != c and b != c:
        if a + b == c or a + c == b or b + c == a:
            return True
        elif a != b or a != c or b != c:
            return True 
    return False
print(cek_angka(6345,3,6348))