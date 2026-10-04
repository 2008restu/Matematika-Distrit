aktif = False
nilai_memenuhi = False
prasyarat = True

# model logika
lulus = aktif and nilai_memenuhi and prasyarat

# 0utput hasil seleksi
if lulus:
    print("Mahasiswa LULUS seleksi beasiswa")
else:
    print("Mahaiswa TIDAK LULUS seleksi beasiswa")
