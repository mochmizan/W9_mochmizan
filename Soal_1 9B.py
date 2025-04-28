#Soal 1 9B
from collections import namedtuple

Koordinat = namedtuple('field', ['x', 'y'])
titik1 = Koordinat(2, 4)

#Akses elemen menggunakan indeks
print("Field x dan y:", titik1[0], titik1[1])
#Akses elemen menggunakan nama atribut
print("Field x dan y:", titik1.x, titik1.y)
#Akses elemen menggunakan getattr
print("Field x dan y:",  getattr(titik1, "x"), getattr(titik1, "y"))
