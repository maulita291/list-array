# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 20:05:46 2021
@author: maulita
"""

"""
Cek nilai Menggunakan Loop 
" Loop CEK TRANSAKSI BIAYA EKSPEDISI
" loop run program (ok)
"""
#CEK TRANSAKSI BIAYA EKSPEDISI LORENA MALANG
ulangprog = "y"
while ulangprog=="y" or ulangprog=="Y":
    print ("<><><><><><><><><><><><><><><><><><><><><><><>")
    print("><    PERUSAHAAN EKSPEDISI LORENA MALANG    ><")
    print("><         TRANSKASI BIAYA EKSPEDISI        ><")
    print ("<><><><><><><><><><><><><><><><><><><><><><><>")
    print(" Kode = a = Surabaya")
    print(" Kode = b = Bandung")
    print (">>>masukan sesuai kode jika kode salah program berakhir")
    print("--biaya kirim ditentukan berdasarkan jarak per km nya--")
    print ("--------------------------------------------------------")

    kota = ['surabaya','bandung']
    jarak = [169,452]
    ongkirperkm = [2500,4000]
    
    pilihan = input(">> Masukkan Kode Tujuan Pengiriman = ")
    #identifikasi pilihan
    if pilihan=="a":
        idx = 0
    elif pilihan=="b":
        idx = 1
    else:
        idx = 2
        print("---------------------KODE SALAH---------------------")
        print(">>> Masukan Kode Yang Sesuai dengan pilihan kota <<<")
        break 
        
    #cetak tampilan layar
    print(">>> Pilihan Tujuan = " + kota[idx])
    print(">>> Jarak          = " + str(jarak[idx]) + " km")
    print(">>> Ongkir per km  = Rp. " + str(ongkirperkm[idx]))

    #hitung transksi
    fixjarak = jarak[idx]
    fixongkirkm = ongkirperkm[idx]
    totongkir = fixjarak * fixongkirkm

    #tampilkan total ongkir
    print(">>>-------------------------------------")
    print(">>> Total Biaya     = Rp." + str(totongkir))

    ulangprog = input(">> Cek Transaksi pengiriman lagi ? y/t = ")  
    if ulangprog=="t" or ulangprog=="T":
        break 