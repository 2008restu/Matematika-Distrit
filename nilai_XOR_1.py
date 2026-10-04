organisasi = True
ukm = False

# model logika XOR
pilihan = organisasi ^ ukm

# output
if pilihan:
    print("pilihan DITERIMA")
else:
    print("pilih SALAH SATU saja")