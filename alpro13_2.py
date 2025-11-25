#PROGRAM PERPUSTAKAAN SEDERHANA
import os

#Data awal
perpus = {
    'F001' : {
        'judul' : 'Belajar Python',
        'penulis' : 'Emannuel Henji',
        'tahun' : 2025,
        'status' : 'TERSEDIA',
        'peminjam' : ''
    },
    'F002' : {
        'judul' : 'Cara Jago Seperti MU',
        'penulis' : 'Ruben Amorim',
        'tahun' : 2025,
        'status' : 'TERSEDIA',
        'peminjam' : ''
    }
}

#fungsi tampilkan semua data buku
def tampilkan_buku():
    print(f"{'key':<7} {'judul':<20} {'penulis':<20} {'tahun':<5} {'status':<10} {'peminjam':<20}")
    for key,value in perpus.items():
        judul = perpus[key]['judul']
        penulis = perpus[key]['penulis']
        tahun = perpus[key]['tahun']
        status = perpus[key]['status']
        peminjam = perpus[key]['peminjam']

        print(f"{key:<7} {judul:<20} {penulis:<20} {tahun:<5} {status:<10} {peminjam:<20}")

#fungsi untuk pinjam buku
def pinjam_buku(judul,nama,status='DIPINJAM'):
    ditemukan = False
    for key,value in perpus.items():
        if value['judul'] == judul and value['status'] == 'TERSEDIA':
            ditemukan = True
            judul = perpus[key]['judul']
            penulis = perpus[key]['penulis']
            perpus[key]['status'] = status
            perpus[key]['peminjam'] = nama
            os.system('cls')
            print(f'Anda berhasil meminjam buku {judul} karya {penulis}')
            break
    if ditemukan == False:
        print('Maaf buku tidak ada / tidak dapat dipinjam') 

#fungsi kembalikan buku
def kembalikan_buku(judul,nama,status='TERSEDIA'):
    ditemukan = False
    for key,value in perpus.items():
        if value['judul'] == judul and value['status'] == 'DIPINJAM' and value['peminjam'] == nama:
            ditemukan = True
            judul = perpus[key]['judul']
            penulis = perpus[key]['penulis']
            perpus[key]['status'] = status
            perpus[key]['peminjam'] = ''
            print(f'Anda berhasil mengembalikan {judul} karya {penulis}')
            tampilkan_buku()
            break
    if ditemukan == False:
        print('Maaf data pinjaman tidak ditemukan') 

#fungsi untuk mencari buku berdasarkan judul
def cari_judul(judul):
    ditemukan = False
    print(f"{'key':<7} {'judul':<20} {'penulis':<20} {'tahun':<5} {'status':<10} {'peminjam':<20}")
    for key,value in perpus.items():
        if value['judul'] == judul:
            ditemukan = True
            judul = perpus[key]['judul']
            penulis = perpus[key]['penulis']
            tahun = perpus[key]['tahun']
            status = perpus[key]['status']
            peminjam = perpus[key]['peminjam']
            print(f"{key:<7} {judul:<20} {penulis:<20} {tahun:<5} {status:<10} {peminjam:<20}")
            
    if ditemukan == False:
        print('Maaf data buku tidak ditemukan')

#fungsi untuk mencari buku berdasarkan penulis
def cari_penulis(penulis):
    ditemukan = False
    print(f"{'key':<7} {'judul':<20} {'penulis':<20} {'tahun':<5} {'status':<10} {'peminjam':<20}")
    for key,value in perpus.items():
        if value['penulis'] == penulis:
            ditemukan = True
            judul = perpus[key]['judul']
            penulis = perpus[key]['penulis']
            tahun = perpus[key]['tahun']
            status = perpus[key]['status']
            peminjam = perpus[key]['peminjam']
            print(f"{key:<7} {judul:<20} {penulis:<20} {tahun:<5} {status:<10} {peminjam:<20}")
            
    if ditemukan == False:
        print('Maaf data buku tidak ditemukan')

#fungsi untuk tampilkan buku yang dipinjam
def buku_dipinjam():
    ditemukan = False
    print(f"{'key':<7} {'judul':<20} {'penulis':<20} {'tahun':<5} {'status':<10} {'peminjam':<20}")
    for key,value in perpus.items():
        if value['status'] == 'DIPINJAM':
            ditemukan = True
            judul = perpus[key]['judul']
            penulis = perpus[key]['penulis']
            tahun = perpus[key]['tahun']
            status = perpus[key]['status']
            peminjam = perpus[key]['peminjam']

            print(f"{key:<7} {judul:<20} {penulis:<20} {tahun:<5} {status:<10} {peminjam:<20}")
    if ditemukan == False:
        print('Maaf data buku tidak ditemukan')

#PAGE HEAD
print('='*30)
print(f'{"PROGRAM PERPUSTAKAAN SEDERHANA":^30}')
print(f'{"oleh Emannuel Henji":^30}')
print('='*30)

#Perulangan program utama
while True:
    print('Apa yang anda perlukan?')
    print('1. Pinjam Buku \n2. Kembalikan Buku \n3. Cari Buku Berdasarkan Judul \n4. Cari Buku Berdasarkan Penulis \n5. Tampilkan Buku Yang Dipinjam \n6. Tampilkan Semua Buku \n7. Tutup Program')
    do = input('Masukkan angka (1-7) : ')
    os.system('cls')
    match do:
        case '1':
            tampilkan_buku()
            judul = input('Masukkan Judul Buku : ')
            nama = input('Masukkan Nama Anda : ')
            pinjam_buku(judul,nama)
        case '2':
            judul = input('Masukkan Judul Buku : ')
            nama = input('Masukkan Nama Anda : ')
            kembalikan_buku(judul,nama)
        case '3':
            judul = input('Masukkan Judul Buku : ')
            cari_judul(judul)
        case '4':
            penulis = input('Masukkan Nama Penulis : ')
            cari_penulis(penulis)
        case '5':
            buku_dipinjam()
        case '6':
            tampilkan_buku()
        case '7':
            break
        case _:
            print('Input tidak valid!')

#Program Selesai
os.system('cls')
print('Program Selesai, \nTerimakasih Telah Menggunakan!')
