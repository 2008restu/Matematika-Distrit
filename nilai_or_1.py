motor = False
angkot = True

# model logika
bisa_berangkat = motor or angkot

# output
if bisa_berangkat:
    print("mahasiswa BISA berangkat ke kampus")
else:
    print("mahasiswa TIDAK memiliki transportasi")