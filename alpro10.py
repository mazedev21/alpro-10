##PROGRAM PERHITUNGAN SEDERHANA##

##BAGIAN 1 : IMPORT MODULE
import math

##BAGIAN 2: FUNCTION PERHITUNGAN
#FUNGSI UNTUK PERHITUNGAN
def luas_pp(p,l): #luas persegi panjang
  return p*l #kembalikan hasil p*l ke fungsi luas_pp
def vol_balok(p,l,t): #volume balok
  return p*l*t #kembalikan hasil p*l*t ke fungsi vol_balok
def luas_lingkaran(r): #luas lingkaran
  return math.pi * r**2 #kembalikan hasil pi*r**2 ke fungsi luas_lingkaran
def vol_bola(r): #volume bola
  return 4/3 * math.pi * r**3 #kembalikan hasil 4/3*pi*r**3 ke fungsi vol_bola

##BAGIAN 3 : FUNCTION OPERASI
#FUNGSI UNTUK CEK OPERASI YANG DIPILIH
def operasi(op):
  if op == 1: #1 -> operasi luas persegi panjang
    print('##LUAS PERSEGI PANJANG##')
    hitung = 'luas persegi panjang' #set variabel hitung dengan value 'luas persegi panjang'
    panjang = float(input('Masukkan panjang: ')) #input panjang lalu set ke float
    lebar = float(input('Masukkan lebar: ')) #input lebar lalu set ke float
    hasil = luas_pp(panjang,lebar) #buat variabel hasil dengan value panggil fungsi luas_pp dengan parameter panjang,lebar
    return hitung,hasil #kembalikan hitung,hasil ke fungsi operasi

  elif op == 2: #2 -> operasi volume balok
    print('##VOLUME BALOK##')
    hitung = 'volume balok' #buat variabel hitung dengan value 'volume balok'
    panjang = float(input('Masukkan panjang: ')) #input panjang lalu set ke float
    lebar = float(input('Masukkan lebar: ')) #input lebar lalu set ke float
    tinggi = float(input('Masukkan tinggi: ')) #input tinggi lalu set ke float
    hasil = vol_balok(panjang,lebar,tinggi) #buat variabel hasil dengan value panggil fungsi vol_balok dengan parameter panjang,lebar,tinggi
    return hitung,hasil #kembalikan hitung,hasil ke fungsi operasi

  elif op == 3: #3 -> operasi luas lingkaran
    print('##LUAS LINGKARAN##')
    hitung = 'luas lingkaran' #buat variabel hitung dengan value 'luas lingkaran'
    jari = float(input('Masukkan jari-jari lingkaran: ')) #input jari-jari lalu set ke float
    hasil = luas_lingkaran(jari) #buat variabel hasil dengan value panggil fungsi luas_ligkaran dengan parameter jari (jari-jari)
    return hitung,hasil #kembalikan hitung,hasil ke fungsi operasi

  elif op == 4: #4 -> operasi volume bola
    print('##VOLUME BOLA##')
    hitung = 'volume bola' #buat variabel hitung dengan value 'luas lingkaran'
    jari = float(input('Masukkan jari-jari bola: ')) #input jari-jari lalu set ke float
    hasil = vol_bola(jari) #buat variabel hasil dengan value panggil fungsi vol_bola dengan parameter jari (jari-jari)
    return hitung,hasil #kembalikan hitung,hasil ke fungsi operasi

##BAGIAN 4 : FORM INPUT
#PAGE HEAD
print('='*30)
print(f'{"PROGRAM PERHITUNGAN SEDERHANA":^30}')
print(f'{"oleh Emannuel Henji":^30}')
print('='*30)

#FORM INPUT
while True: #selama true
  #PILIHAN PERHITUNGAN
  print('Perhitungan yang bisa dilakukan: \n1. Luas Persegi Panjang \n2. Volume Balok \n3. Luas Lingkaran \n4. Volume Bola')
  while True: #selama true #nested loop
    try: #jalankan program
      operation = int(input('Anda Ingin melakukan perhitungan apa? (1/2/3/4): ')) #input mau perhitungan apa
      if operation in [1,2,3,4]: #jika nilai operation adalah 1,2,3,4
        break #hentikan nested loop
      #jika bukan 1,2,3,4, tampilkan 'Operasi Tidak Tersedia\nGunakan operasi yang tersedia' di terminal
      print('Operasi Tidak Tersedia\nGunakan operasi yang tersedia') 

    except ValueError: #jika program mengalami value error
      print('Hanya bisa menerima input angka') #tampilkan 'Hanya bisa menerima input angka' di terminal

  print('\n')

  ##BAGIAN 5 : CALL FUNCTION
  #eksekusi function operasi
  count,result = operasi(operation) #panggil fungsi operasi dengan value operation

  ##BAGIAN 6 : HASIL PERHITUNGAN
  #logika untuk satuan
  if operation in [1,3]: #jika value operation adalah 1 atau 3
    satuan = 'cm²' #set value variabel satuan dengan 'cm²'
  else: #jika tidak 1 atau 3
    satuan = 'cm³' #set value variabel satuan dengan 'cm³'

  #keluarkan hasil perhitungan ke terminal
  print(f'Hasil perhitungan {count} adalah : {round(result,2)} {satuan}')
  print('\n')

  ##BAGIAN 7 : INPUT OPSI BERHENTI ATAU LANJUT
  #PILIHAN APAKAH INGIN MELAKUKAN PERHITUNGAN LAGI
  while True: #selama true #nested loop
      isDone = input('Apakah anda ingin melakukan perhitungan lagi? (y/n): ').lower() #Masukkan y/n, ubah inputan menjadi huruf kecil
      if isDone in ['y','n']: #jika value isDone adalah y atau n
        break #hentikan nested loop
      #jika tidak y atau n, tampilkan 'Hanya bisa menerima input "y" atau "n"' di terminal
      print('Hanya bisa menerima input "y" atau "n"') 

  if isDone == 'n': #jika value isDone adalah 'n'
    break #hentikan perulangan utama

  print('\n') #buat baris baru

#tampilkan 'Terimakasih telah menggunakan.....\nSampai jumpa lagi.....' di terminal
print('Terimakasih telah menggunakan.....\nSampai jumpa lagi.....')