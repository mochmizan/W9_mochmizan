#Soal 5
from collections import namedtuple

kirim = namedtuple("pengiriman", ["resi", "barang", "berat", "tujuan"])
barang1 = kirim("A032", "Ijazah", 0.3, "Jawa Tengah")

print("RESI     :", barang1.resi)
print("BARANG   :", barang1.barang)
print("BERAT    :", barang1.berat)
print("TUJUAN   :", barang1.tujuan)
