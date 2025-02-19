#Soal 3
class persegi:
  def __init__(self, sisi):
    self.sisi = int(sisi)

  def luas(self):
    return (self.sisi**2)

  def keliling(self):
    return (self.sisi*4)

n = int(input("Masukkan sisi Persegi: "))
print("Luas Persegi:", persegi(n).luas())
print("Keliling Persegi:", persegi(n).keliling())
