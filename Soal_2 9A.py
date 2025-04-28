#Soal 2 9A
from datetime import date

class datadiri:
  def __init__(self, nama, umur, provinsi, no_telp):
    self.nama = nama
    self.umur = umur
    self.provinsi = provinsi
    self.no_telp = no_telp

  @classmethod
  def umur_dari_tahun_lahir(cls, nama, tahun_lahir, provinsi, no_telp):
    return cls(nama, date.today().year - tahun_lahir, provinsi, no_telp)

  @staticmethod
  def cek_umur(nama, umur):
    if (umur > 17):
      return print(nama, "sudah cukup umur untuk melakukan pinjaman!")
    else:
      return print(nama, "belum cukup umur untuk melakukan pinjaman!")

  @property
  def cek_dewasa(self):
    if (self.umur > 21):
      return print("Dewasa")
    else:
      return print("Di bawah umur")

Tia = datadiri.umur_dari_tahun_lahir('Tia', 1996, 'Jawa Timur', '081666')
datadiri.cek_umur('Yoyok Nurrohman', 22)
Tia.cek_dewasa
