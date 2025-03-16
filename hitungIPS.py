def hitungIPS():
  print('Program penghitung IPS Mahasiswa')
  jumlah_matkul = int(input('Berapa jumlah mata kuliah?'))

  total_bobot = 0
  sks_per_matkul = 3

  for i in range(1, jumlah_matkul + 1):
    while True:
      nilai = input(f'Nilai MK ke{i}: ')
      if nilai in ['A', 'B', 'C', 'D']:
        break
      else:
        print('Nilai harus menggunakan huruf kapital')
    if nilai == 'A':
      bobot = 4
    elif nilai == 'B':
      bobot = 3
    elif nilai == 'C':
      bobot = 2
    elif nilai == 'D':
      bobot = 1

    total_bobot += bobot * sks_per_matkul
  ips = total_bobot / (jumlah_matkul * sks_per_matkul)
  print(f'Nilai IPS anda semester ini {ips:.2f}')

hitungIPS()