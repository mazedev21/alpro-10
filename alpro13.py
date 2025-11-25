#PENGELOLAAN BARANG
import os

#dict kosong untuk menyimpan data
data_barang = {}

#menghitung panjang data pada dict data_barang
angka = len(data_barang) #untuk buat kode angka setelah huruf

#fungsi tambah barang
def tambah():
  global angka

  #buat kode
  huruf = 'A'
  angka += 1
  kode = huruf + str(angka)

  #tambahkan barang
  barang = {
      'nama' : input('Masukkan nama barang: '),
      'harga' : int(input('Masukkan harga: ')),
      'stok' : int(input('Masukkan jumlah stok tersedia: '))
  }

  data_barang.update({kode:barang})
  tampilkan(data_barang)

#fungsi hapus barang
def hapus(kode_barang):
  del data_barang[kode_barang]
  print('Data berhasil Dihapus!')
  tampilkan(data_barang)

#fungsi cari barang berdasarkan nama
def cari(nama_barang):
    ditemukan = False
    print('='*57)
    print(f"{'KODE':<7} {'Nama Barang':<20} {'Harga':<15} {'Stok':<15}")
    print('='*57)
    for kode, value in data_barang.items():
      if value['nama'] == nama_barang:
        nama_barang = data_barang[kode]['nama']
        harga_barang = data_barang[kode]['harga']
        stok_barang  = data_barang[kode]['stok']
        print(f"{kode:<7} {nama_barang:<20} {harga_barang:<15} {stok_barang:<15}")
        ditemukan = True
        break
    if ditemukan == False:
      print('Data Tidak Ditemukan')
    print('='*57)

#fungsi tampilkan semua barang
def tampilkan(dictionary):
  print('='*57)
  print(f"{'KODE':<7} {'Nama Barang':<20} {'Harga':<15} {'Stok':<15}")
  print('='*57)
  if len(dictionary)  == 0:
    print('Maaf belum ada data barang yang anda masukkan')
  else:
    for kode in dictionary :
      nama_barang = dictionary[kode]['nama']
      harga_barang = dictionary[kode]['harga']
      stok_barang  = dictionary[kode]['stok']

      print(f"{kode:<7} {nama_barang:<20} {harga_barang:<15} {stok_barang:<15}")
  print('='*57)  

def stok():
    print('='*57)
    print(f"{'KODE':<7} {'Nama Barang':<20} {'Harga':<15} {'Stok':<15}")
    print('='*57)
    ditemukan = False
    for kode, value in data_barang.items():
      if value['stok'] < 5:
        nama_barang = data_barang[kode]['nama']
        harga_barang = data_barang[kode]['harga']
        stok_barang  = data_barang[kode]['stok']
        ditemukan = True
        print(f"{kode:<7} {nama_barang:<20} {harga_barang:<15} {stok_barang:<15}")
    if ditemukan == False:
      print('Tidak ada barang yang stok < 5')
    print('='*57)
    
#fungsi untuk ambil harga pada dict
def ambilharga(item):
  return item[1]['harga']

#sort barang berdasarkan harga (mahal => murah)
def SortHarga(dictionary, reverse=True):
  sorted_barang = sorted(dictionary.items(), key=ambilharga, reverse=reverse)
  return dict(sorted_barang)


#PAGE HEAD
print('='*30)
print(f'{"PROGRAM PENGELOLAAN BARANG SEDERHANA":^30}')
print(f'{"oleh Emannuel Henji":^30}')
print('='*30)

#Perulangan Program Utama
while True:
  print('\n')
  print('Apa yang anda perlukan? \n1. Tambah Barang \n2. Hapus Barang \n3. Cari Barang Berdasarkan Nama \n4. Tampilkan Barang \n5. Tampilkan Barang (Stok < 5) \n6. Tampilkan Barang (Mahal -> Murah) \n7. Tutup Aplikasi')
  operasi = input('Apa yang akan anda lakukan (1-7): ')
  os.system('cls')

  #pencocokan untuk operasi
  match operasi:
    case '1':
      tambah()
    case '2':
      tampilkan(data_barang)
      kode_barang = input('Masukkan Kode Barang yang ingin dihapus: ')
      hapus(kode_barang)
    case '3':
      nama_barang = input('Masukkan nama barang yang dicari: ')
      cari(nama_barang)
    case '4':
      tampilkan(data_barang)
    case '5':
      stok()
    case '6':
      sort_harga = SortHarga(data_barang)
      tampilkan(sort_harga)
    case '7':
      break
    case _:
      print('Pilihan tidak valid')

#program selesai
os.system('cls')
print('Program Selesai, \nTerimakasih Telah Menggunakan!')