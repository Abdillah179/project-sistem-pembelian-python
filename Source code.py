from platform import system
import time
from datetime import datetime
now = datetime.now()
d3 = now.strftime("%d %B %y %H:%m:%S")
import os
os.system("cls")

def garis ():
    print("=" * 150)
garis()
garis()
print("                                                SELAMAT DATANG DI TOKO SEPATU SPORTSTATION")
garis()
garis()
# Input Awalan
garis()
nama_pembeli = input("Nama Pembeli : ")
no_hp = input("Masukkan No. Handphone anda : ")
garis()

# List
list_nama_barang = []
list_harga = []
list_ukuran = []
list_warna = []
list_warna_barang = []
total = 0

# Perulangan dan percabangan
while True:
    print("===========================DAFTAR SEPATU PRIA DAN WANITA==========================") 
    print()
    print("1.  New Balance 520v7 Men's Running Shoes (KHUSUS PRIA)")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [Blue]")
    print("    Harga : Rp629.000-")
    print()
    print("2.  Adidas Response Run Men's Running Shoes (KHUSUS PRIA) ")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [White]")
    print("    Harga : Rp850.000-")
    print()
    print("3.  Adidas Run Falcon 2.0 Men's Running Shoes (KHUSUS PRIA) ")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [White]")
    print("    Harga : Rp680.000-")
    print()
    print("4.  Adidas Duramo 10 Men's Running shoes (KHUSUS PRIA) ")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [Black]")
    print("    Harga : Rp900.000-")
    print()
    print("5.  Diadora Fast Men's Basketball Shoes (KHUSUS PRIA) ")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [Black]")
    print("    Harga : Rp699.000-")
    print()
    print("6.  Astec Gary Men's Basketball Shoes (KHUSUS PRIA) ")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [White Black]")
    print("    Harga : Rp559.000-")
    print()
    print("7.  Skechers Go Walk Flex Men's Walking Shoes (KHUSUS PRIA) ")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [Black]")
    print("    Harga : Rp799.000-")
    print()
    print("8.  Skechers Go Walk Air 2.0 Men's Walking Shoes (KHUSUS PRIA) ")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [Navy]")
    print("    Harga : Rp785.000-")
    print()
    print("9.  Astec Fonterra Men's Badminton Shoes (KHUSUS PRIA) ")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [Black]")
    print("    Harga : Rp449.000-")
    print()
    print("10. Adidas Ligra 7 Men's Bdminton Shoes (KHUSUS PRIA) ")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [White]")
    print("    Harga : Rp900.000-")
    print()
    print("11. Diadora ERVE Women's Running Shoes (KHUSUS WANITA) ")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [Pink]")
    print("    Harga : Rp559.000-")
    print()
    print("12. Diadora ERISO Women's Running Shoes (KHUSUS WANITA) ")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [Blue]")
    print("    Harga : Rp459.000-") 
    print()
    print("13. ASTEC GAIA Women's Walking Shoes (KHUSUS WANITA) ")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [Black]")
    print("    Harga : Rp398.000-")
    print()
    print("14. ASTEC FENIX Women's Walking shoes (KHUSUS WANITA) ")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [White]")
    print("    Harga : Rp459.000-")
    print()
    print("15. ASTEC FONTERRA Women's Badminton Shoes (KHUSUS WANITA) ")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [Red]")
    print("    Harga : Rp499.000-")
    print()
    print("16. Skechers Skech-Air Dynamight Women's Fitness Shoes (KHUSUS WANITA) ")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [Black]")
    print("    Harga : Rp799.000-")
    print()
    print("17. Airwalk Rocio Women's Snekers (KHUSUS WANITA) ")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [Purple]")
    print("    Harga : Rp287.000-")
    print()
    print("18. Airwalk Sharon Women's Sneakers (KHUSUS WANITA) ")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [White]")
    print("    Harga : Rp279.000-")
    print()
    print("19. Diadora Falcon Women Tennis Shoes (KHUSUS WANITA) ")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [Blue]")
    print("    Harga : Rp659.000-")
    print()
    print("20. Skechers Golf Max Fairway 3 Women Golf Shoes (KHUSUS WANITA) ")
    print("    Ukuran [38/39/40/41/42/43/44/45]")
    print("    Warna  [Black]")
    print("    Harga : Rp419.000-")
    print()
    garis()

    pilihan_sepatu = input("MASUKKAN NOMOR BARANG YANG INGIN DIBELI: ")
    if pilihan_sepatu == "1" or pilihan_sepatu == "New Balance 520v7 Men's Running Shoes":
        nama_barang = "New Balance 520v7 Men's Running Shoes"
        list_nama_barang.append(nama_barang)
        harga = 629000
        list_harga.append(harga)
        total += 629000 
        warna_barang = "Blue"
        list_warna_barang.append(warna_barang)
    elif pilihan_sepatu == "2" or pilihan_sepatu == "Adidas Response Run Men's Running Shoes":
        nama_barang = "Adidas Response Run Men's Running Shoes"
        list_nama_barang.append(nama_barang)
        harga = 850000
        list_harga.append(harga)
        total += 850000
        warna_barang = "White"
        list_warna_barang.append(warna_barang)
    elif pilihan_sepatu == "3" or pilihan_sepatu == "Adidas Run Falcon 2.0 Men's Running Shoes ":
        nama_barang = "Adidas Run Falcon 2.0 Men's Running Shoes "
        list_nama_barang.append(nama_barang)
        harga = 680000
        list_harga.append(harga)
        total += 680000
        warna_barang = "White"
        list_warna_barang.append(warna_barang)
    elif pilihan_sepatu == "4" or pilihan_sepatu == "Adidas Duramo 10 Men's Running shoes":
        nama_barang = "Adidas Duramo 10 Men's Running shoes"
        list_nama_barang.append(nama_barang)
        harga = 900000
        list_harga.append(harga)
        total += 900000
        warna_barang = "Black"
        list_warna_barang.append(warna_barang)
    elif pilihan_sepatu == "5" or pilihan_sepatu == "Diadora Fast Men's Basketball Shoes":
        nama_barang = " Diadora Fast Men's Basketball Shoes"
        list_nama_barang.append(nama_barang)
        harga = 669000
        list_harga.append(harga)
        total += 669000
        warna_barang = "Black"
        list_warna_barang.append(warna_barang)
    elif pilihan_sepatu == "6" or pilihan_sepatu == "Astec Gary Men's Basketball Shoes":
        nama_barang = "Astec Gary Men's Basketball Shoes"
        list_nama_barang.append(nama_barang)
        harga = 559000
        list_harga.append(harga)
        total += 559000
        warna_barang = "White Black"
        list_warna_barang.append(warna_barang)
    elif pilihan_sepatu == "7" or pilihan_sepatu == "Skechers Go Walk Flex Men's Walking Shoes":
        nama_barang = "Skechers Go Walk Flex Men's Walking Shoes"
        list_nama_barang.append(nama_barang)
        harga = 799000
        list_harga.append(harga)
        total += 799000
        warna_barang = "Black"
        list_warna_barang.append(warna_barang)
    elif pilihan_sepatu == "8" or pilihan_sepatu == "Skechers Go Walk Air 2.0 Men's Walking Shoes":
        nama_barang = "Skechers Go Walk Air 2.0 Men's Walking Shoes"
        list_nama_barang.append(nama_barang)
        harga = 785000
        list_harga.append(harga)
        total += 785000
        warna_barang = "Navy"
        list_warna_barang.append(warna_barang)
    elif pilihan_sepatu == "9" or pilihan_sepatu == "Astec Fonterra Men's Badminton Shoes":
        nama_barang = "Astec Fonterra Men's Badminton Shoes"
        list_nama_barang.append(nama_barang)
        harga = 449000
        list_harga.append(harga)
        total += 449000
        warna_barang = "Black"
        list_warna_barang.append(warna_barang)
    elif pilihan_sepatu == "10" or pilihan_sepatu == "Adidas Ligra 7 Men's Bdminton Shoes":
        nama_barang = "Adidas Ligra 7 Men's Bdminton Shoes"
        list_nama_barang.append(nama_barang)
        harga = 900000
        list_harga.append(harga)
        total += 900000
        warna_barang = "White"
        list_warna_barang.append(warna_barang)
    elif pilihan_sepatu == "11" or pilihan_sepatu == "Diadora ERVE Women's Running Shoes":
        nama_barang = "Diadora ERVE Women's Running Shoes"
        list_nama_barang.append(nama_barang)
        harga = 559000
        list_harga.append(harga)
        total += 559000
        warna_barang = "Pink"
        list_warna_barang.append(warna_barang)
    elif pilihan_sepatu == "12" or pilihan_sepatu == "Diadora ERISO Women's Running Shoes":
        nama_barang = "Diadora ERISO Women's Running Shoes"
        list_nama_barang.append(nama_barang)
        harga = 459000
        list_harga.append(harga)
        total += 459000
        warna_barang = "Blue"
        list_warna_barang.append(warna_barang)
    elif pilihan_sepatu == "13" or pilihan_sepatu == "ASTEC GAIA Women's Walking Shoes ":
        nama_barang = "ASTEC GAIA Women's Walking Shoes "
        list_nama_barang.append(nama_barang)
        harga = 398000
        list_harga.append(harga)
        total += 398000
        warna_barang = "Black"
        list_warna_barang.append(warna_barang)
    elif pilihan_sepatu == "14" or pilihan_sepatu == "ASTEC FENIX Women's Walking shoes":
        nama_barang = "ASTEC FENIX Women's Walking shoes "
        list_nama_barang.append(nama_barang)
        harga = 459000
        list_harga.append(harga)
        total += 459000
        warna_barang = "White"
        list_warna_barang.append(warna_barang)
    elif pilihan_sepatu == "15" or pilihan_sepatu == "ASTEC FONTERRA Women's Badminton Shoes":
        nama_barang = "ASTEC FONTERRA Women's Badminton Shoes "
        list_nama_barang.append(nama_barang)
        harga = 499000
        list_harga.append(harga)
        total += 499000
        warna_barang = "Red"
        list_warna_barang.append(warna_barang)
    elif pilihan_sepatu == "16" or pilihan_sepatu == "Skechers Skech-Air Dynamight Women's Fitness Shoes":
        nama_barang = "Skechers Skech-Air Dynamight Women's Fitness Shoes "
        list_nama_barang.append(nama_barang)
        harga = 799000
        list_harga.append(harga)
        total += 799000
        warna_barang = "Black"
        list_warna_barang.append(warna_barang)
    elif pilihan_sepatu == "17" or pilihan_sepatu == "Airwalk Rocio Women's Snekers ":
        nama_barang = "Airwalk Rocio Women's Snekers  "
        list_nama_barang.append(nama_barang)
        harga = 287000
        list_harga.append(harga)
        total += 287000
        warna_barang = "Purple"
        list_warna_barang.append(warna_barang)
    elif pilihan_sepatu == "18" or pilihan_sepatu == "Airwalk Sharon Women's Sneakers ":
        nama_barang = "Airwalk Sharon Women's Sneakers   "
        list_nama_barang.append(nama_barang)
        harga = 279000
        list_harga.append(harga)
        total += 279000
        warna_barang = "White"
        list_warna_barang.append(warna_barang)
    elif pilihan_sepatu == "19" or pilihan_sepatu == "Diadora Falcon Women Tennis Shoes":
        nama_barang = "Diadora Falcon Women Tennis Shoes"
        list_nama_barang.append(nama_barang)
        harga = 659000
        list_harga.append(harga)
        total += 659000
        warna_barang = "Blue"
        list_warna_barang.append(warna_barang)
    elif pilihan_sepatu == "20" or pilihan_sepatu == "Skechers Golf Max Fairway 3 Women Golf Shoes ":
        nama_barang = "Skechers Golf Max Fairway 3 Women Golf Shoes "
        list_nama_barang.append(nama_barang)
        harga = 419000
        list_harga.append(harga)
        total += 419000
        warna_barang = "Black"
        list_warna_barang.append(warna_barang)
    else:
        while True:
            print("Barang yang anda pilih tidak tersedia, silahkan masukkan kembali barang yang lainnya")
            pilihan_sepatu = input("MASUKKAN NOMOR BARANG YANG INGIN DIBELI: ")
            if pilihan_sepatu == "1" or pilihan_sepatu == "New Balance 520v7 Men's Running Shoes":
                nama_barang = "New Balance 520v7 Men's Running Shoes"
                list_nama_barang.append(nama_barang)
                harga = 629000
                list_harga.append(harga)
                total += 629000 
                warna_barang = "Blue"
                list_warna_barang.append(warna_barang)
            elif pilihan_sepatu == "2" or pilihan_sepatu == "Adidas Response Run Men's Running Shoes":
                nama_barang = "Adidas Response Run Men's Running Shoes"
                list_nama_barang.append(nama_barang)
                harga = 850000
                list_harga.append(harga)
                total += 850000
                warna_barang = "White"
                list_warna_barang.append(warna_barang)
            elif pilihan_sepatu == "3" or pilihan_sepatu == "Adidas Run Falcon 2.0 Men's Running Shoes ":
                nama_barang = "Adidas Run Falcon 2.0 Men's Running Shoes "
                list_nama_barang.append(nama_barang)
                harga = 680000
                list_harga.append(harga)
                total += 680000
                warna_barang = "White"
                list_warna_barang.append(warna_barang)
            elif pilihan_sepatu == "4" or pilihan_sepatu == "Adidas Duramo 10 Men's Running shoes":
                nama_barang = "Adidas Duramo 10 Men's Running shoes"
                list_nama_barang.append(nama_barang)
                harga = 900000
                list_harga.append(harga)
                total += 900000
                warna_barang = "Black"
                list_warna_barang.append(warna_barang)
            elif pilihan_sepatu == "5" or pilihan_sepatu == "Diadora Fast Men's Basketball Shoes":
                nama_barang = " Diadora Fast Men's Basketball Shoes"
                list_nama_barang.append(nama_barang)
                harga = 669000
                list_harga.append(harga)
                total += 669000
                warna_barang = "Black"
                list_warna_barang.append(warna_barang)
            elif pilihan_sepatu == "6" or pilihan_sepatu == "Astec Gary Men's Basketball Shoes":
                nama_barang = "Astec Gary Men's Basketball Shoes"
                list_nama_barang.append(nama_barang)
                harga = 559000
                list_harga.append(harga)
                total += 559000
                warna_barang = "White Black"
                list_warna_barang.append(warna_barang)
            elif pilihan_sepatu == "7" or pilihan_sepatu == "Skechers Go Walk Flex Men's Walking Shoes":
                nama_barang = "Skechers Go Walk Flex Men's Walking Shoes"
                list_nama_barang.append(nama_barang)
                harga = 799000
                list_harga.append(harga)
                total += 799000
                warna_barang = "Black"
                list_warna_barang.append(warna_barang)
            elif pilihan_sepatu == "8" or pilihan_sepatu == "Skechers Go Walk Air 2.0 Men's Walking Shoes":
                nama_barang = "Skechers Go Walk Air 2.0 Men's Walking Shoes"
                list_nama_barang.append(nama_barang)
                harga = 785000
                list_harga.append(harga)
                total += 785000
                warna_barang = "Navy"
                list_warna_barang.append(warna_barang)
            elif pilihan_sepatu == "9" or pilihan_sepatu == "Astec Fonterra Men's Badminton Shoes":
                nama_barang = "Astec Fonterra Men's Badminton Shoes"
                list_nama_barang.append(nama_barang)
                harga = 449000
                list_harga.append(harga)
                total += 449000
                warna_barang = "Black"
                list_warna_barang.append(warna_barang)
            elif pilihan_sepatu == "10" or pilihan_sepatu == "Adidas Ligra 7 Men's Bdminton Shoes":
                nama_barang = "Adidas Ligra 7 Men's Bdminton Shoes"
                list_nama_barang.append(nama_barang)
                harga = 900000
                list_harga.append(harga)
                total += 900000
                warna_barang = "White"
                list_warna_barang.append(warna_barang)
            elif pilihan_sepatu == "11" or pilihan_sepatu == "Diadora ERVE Women's Running Shoes":
                nama_barang = "Diadora ERVE Women's Running Shoes"
                list_nama_barang.append(nama_barang)
                harga = 559000
                list_harga.append(harga)
                total += 559000
                warna_barang = "Pink"
                list_warna_barang.append(warna_barang)
            elif pilihan_sepatu == "12" or pilihan_sepatu == "Diadora ERISO Women's Running Shoes":
                nama_barang = "Diadora ERISO Women's Running Shoes"
                list_nama_barang.append(nama_barang)
                harga = 459000
                list_harga.append(harga)
                total += 459000
                warna_barang = "Blue"
                list_warna_barang.append(warna_barang)
            elif pilihan_sepatu == "13" or pilihan_sepatu == "ASTEC GAIA Women's Walking Shoes ":
                nama_barang = "ASTEC GAIA Women's Walking Shoes "
                list_nama_barang.append(nama_barang)
                harga = 398000
                list_harga.append(harga)
                total += 398000
                warna_barang = "Black"
                list_warna_barang.append(warna_barang)
            elif pilihan_sepatu == "14" or pilihan_sepatu == "ASTEC FENIX Women's Walking shoes":
                nama_barang = "ASTEC FENIX Women's Walking shoes "
                list_nama_barang.append(nama_barang)
                harga = 459000
                list_harga.append(harga)
                total += 459000
                warna_barang = "White"
                list_warna_barang.append(warna_barang)
            elif pilihan_sepatu == "15" or pilihan_sepatu == "ASTEC FONTERRA Women's Badminton Shoes":
                nama_barang = "ASTEC FONTERRA Women's Badminton Shoes "
                list_nama_barang.append(nama_barang)
                harga = 499000
                list_harga.append(harga)
                total += 499000
                warna_barang = "Red"
                list_warna_barang.append(warna_barang)
            elif pilihan_sepatu == "16" or pilihan_sepatu == "Skechers Skech-Air Dynamight Women's Fitness Shoes":
                nama_barang = "Skechers Skech-Air Dynamight Women's Fitness Shoes "
                list_nama_barang.append(nama_barang)
                harga = 799000
                list_harga.append(harga)
                total += 799000
                warna_barang = "Black"
                list_warna_barang.append(warna_barang)
            elif pilihan_sepatu == "17" or pilihan_sepatu == "Airwalk Rocio Women's Snekers ":
                nama_barang = "Airwalk Rocio Women's Snekers  "
                list_nama_barang.append(nama_barang)
                harga = 287000
                list_harga.append(harga)
                total += 287000
                warna_barang = "Purple"
                list_warna_barang.append(warna_barang)
            elif pilihan_sepatu == "18" or pilihan_sepatu == "Airwalk Sharon Women's Sneakers ":
                nama_barang = "Airwalk Sharon Women's Sneakers   "
                list_nama_barang.append(nama_barang)
                harga = 279000
                list_harga.append(harga)
                total += 279000
                warna_barang = "White"
                list_warna_barang.append(warna_barang)
            elif pilihan_sepatu == "19" or pilihan_sepatu == "Diadora Falcon Women Tennis Shoes":
                nama_barang = "Diadora Falcon Women Tennis Shoes"
                list_nama_barang.append(nama_barang)
                harga = 659000
                list_harga.append(harga)
                total += 659000
                warna_barang = "Blue"
                list_warna_barang.append(warna_barang)
            elif pilihan_sepatu == "20" or pilihan_sepatu == "Skechers Golf Max Fairway 3 Women Golf Shoes ":
                nama_barang = "Skechers Golf Max Fairway 3 Women Golf Shoes "
                list_nama_barang.append(nama_barang)
                harga = 419000
                list_harga.append(harga)
                total += 419000
                warna_barang = "Black"
                list_warna_barang.append(warna_barang)
            break
    ukuran_sepatu = input("MASUKkAN UKURAN BARANG [38/39/40/41/42/43/44/45] : ")
    if ukuran_sepatu == "38" or ukuran_sepatu == "Tiga delapan" or ukuran_sepatu == "Tiga Delapan" or ukuran_sepatu == "TIGA DELAPAN":
        ukuran = "38"
        list_ukuran.append(ukuran)
    elif ukuran_sepatu == "39" or ukuran_sepatu == "Tiga sembilan" or ukuran_sepatu == "Tiga Sembilan" or ukuran_sepatu == "TIGA SEMBILAN":
        ukuran = "39"
        list_ukuran.append(ukuran)
    elif ukuran_sepatu == "40" or ukuran_sepatu == "Empat puluh" or ukuran_sepatu == "Empat Puluh" or ukuran_sepatu == "EMPAT PULUH":
        ukuran = "40"
        list_ukuran.append(ukuran)
    elif ukuran_sepatu == "41" or ukuran_sepatu == "Empat satu" or ukuran_sepatu == "Empat Satu" or ukuran_sepatu == "EMPAT SATU": 
        ukuran = "41"
        list_ukuran.append(ukuran)
    elif ukuran_sepatu == "42" or ukuran_sepatu == "Empat dua" or ukuran_sepatu == "Empat Dua" or ukuran_sepatu == "EMPAT DUA": 
        ukuran = "42"
        list_ukuran.append(ukuran)
    elif ukuran_sepatu == "43" or ukuran_sepatu == "Empat tiga" or ukuran_sepatu == "Empat Tiga" or ukuran_sepatu == "EMPAT TIGA": 
        ukuran = "43"
        list_ukuran.append(ukuran)
    elif ukuran_sepatu == "44" or ukuran_sepatu == "Empat empat" or ukuran_sepatu == "Empat Empat" or ukuran_sepatu == "EMPAT EMPAT": 
        ukuran = "44"
        list_ukuran.append(ukuran)
    elif ukuran_sepatu == "45" or ukuran_sepatu == "Empat lima" or ukuran_sepatu == "Empat Lima" or ukuran_sepatu == "EMPAT LIMA": 
        ukuran = "45"
        list_ukuran.append(ukuran)
    else:
        while True:
            print("Maaf ukuran sepatu tidak tersedia, Silahkan masukkan kembali ukuran sepatu yang lainnya")
            ukuran_sepatu = input("MASUKKAN UKURAN BARANG [38/39/40/41/42/43/44/45] : ")
            if ukuran_sepatu == "38" or ukuran_sepatu == "Tiga delapan" or ukuran_sepatu == "Tiga Delapan" or ukuran_sepatu == "TIGA DELAPAN":
                ukuran = "38"
                list_ukuran.append(ukuran)
            elif ukuran_sepatu == "39" or ukuran_sepatu == "Tiga sembilan" or ukuran_sepatu == "Tiga Sembilan" or ukuran_sepatu == "TIGA SEMBILAN":
                ukuran = "39"
                list_ukuran.append(ukuran)
            elif ukuran_sepatu == "40" or ukuran_sepatu == "Empat puluh" or ukuran_sepatu == "Empat Puluh" or ukuran_sepatu == "EMPAT PULUH":
                ukuran = "40"
                list_ukuran.append(ukuran)
            elif ukuran_sepatu == "41" or ukuran_sepatu == "Empat satu" or ukuran_sepatu == "Empat Satu" or ukuran_sepatu == "EMPAT SATU": 
                ukuran = "41"
                list_ukuran.append(ukuran)
            elif ukuran_sepatu == "42" or ukuran_sepatu == "Empat dua" or ukuran_sepatu == "Empat Dua" or ukuran_sepatu == "EMPAT DUA": 
                ukuran = "42"
                list_ukuran.append(ukuran)
            elif ukuran_sepatu == "43" or ukuran_sepatu == "Empat tiga" or ukuran_sepatu == "Empat Tiga" or ukuran_sepatu == "EMPAT TIGA": 
                ukuran = "43"
                list_ukuran.append(ukuran)
            elif ukuran_sepatu == "44" or ukuran_sepatu == "Empat empat" or ukuran_sepatu == "Empat Empat" or ukuran_sepatu == "EMPAT EMPAT": 
                ukuran = "44"
                list_ukuran.append(ukuran)
            elif ukuran_sepatu == "45" or ukuran_sepatu == "Empat lima" or ukuran_sepatu == "Empat Lima" or ukuran_sepatu == "EMPAT LIMA": 
                ukuran = "45"
                list_ukuran.append(ukuran)
            break
    lanjut = input("Ingin belanja lagi [ya/tidak] : ")
    if lanjut == "t" or lanjut == "T" or lanjut == "Tidak" or lanjut == "tidak" or lanjut == "tdk":
        print("")
        break
    

# Output Program
print()
print("=" * 70)
print("                           TOKO SEPATU SPORSTATION")
print("=" * 70)
print()
print("                            " + str(nama_pembeli))
print("                           " + str(no_hp))
print()
print("Daftar Belanjaan :")
print("=" * 200)
print("Nama barang : ", list_nama_barang)
print("Ukuran : ",list_ukuran)
print("Warna : ",list_warna_barang)
print("Harga : ", list_harga)
print("Total : ",total)
print("=" * 200)

# Total Jumlah Harga Seluruh Barang Belanjaan

print("Total belanja : Rp" + str(total))

# Pemberian Diskon
if total >= 780000:
    print()
    print("Selamat!")
    print("Anda Mendapatkan Diskon 20%")
    diskon = total * 20 / 100
else:
    diskon = 0
print()

jumlah_bayar = total - diskon

print("Total Akhir : Rp" + str(jumlah_bayar))
print("-" * 70)

# Pembayaran
Ubyr = int(input("Bayar : Rp"))

# Uang Kembalian
if Ubyr > jumlah_bayar:
    print("Sisa uang kembali : ",Ubyr-jumlah_bayar)
elif Ubyr == jumlah_bayar:
    print("uang anda pas")
else:
    print("uang yang anda bayarkan kurang : ",Ubyr-jumlah_bayar)

print()
print("                     Terima Kasih sudah berbelanja :)")
garis()
print("Tanggal Pembelian : ",d3)