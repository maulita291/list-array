  
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 20:07:54 2021
@author: maulita
"""

"""
Cek nilai Menggunakan Loop 
" Loop CEK Program Bengkel Motor UD.Matahari
" loop run program (ok)
"""
#CEK Program Bengkel Motor UD.Matahari
ulangprog = "y"
while ulangprog=="y" or ulangprog=="Y":
    print ("**********************************************")
    print("<<         BENGKEL MOTOR UD.MATAHARI         >>")
    print("<<            CEK BIAYA TRANSAKSI            >>")
    print ("**********************************************")
    print(" Kode = a = Duration SW20 1L")
    print(" Kode = b = Castrol Magnatec 1L")
    print(" Kode = c = Federal Supreme XX 1L")
    print(" Kode = d = Yamalube 1L")
    print(" Kode = e = Shell 1L")
    print (">>>masukan sesuai kode jika kode salah program berakhir")
    print ("--------------------------------------------------------")

    OliMotor = ['Duration SW20 1L','Castrol Magnetic 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L']
    harga = [53000,50000,54000,45000,46000]
    PPN = 1/100
    
    pilihan = input(">> Masukkan Kode untuk melihat rincian biaya = ")
    #identifikasi pilihan
    if pilihan=="a":
        idx = 0
    elif pilihan=="b":
        idx = 1
    elif pilihan=="c":
        idx = 2
    elif pilihan=="d":
        idx = 3
    elif pilihan=="e":
        idx = 4
    else:
        idx = 5
        print("---------------------KODE SALAH---------------------")
        print(">>>           Masukan Kode Yang Sesuai           <<<")
        break 
   
    #cetak tampilan layar
    print(">>> Nama Merk Oli Motor = " + OliMotor[idx])
    print(">>> Harga Oli Motor 1L = Rp " + str(harga[idx])) 

    #input jumlah Oli motor
    jumlahbeli=int(input("masukan jumlah Oli Motor yang dibeli = " ))  
    #hitung transksi
    harga = harga[idx]
    totalharga = harga * jumlahbeli
    #tampilkan total Harga
    print(">>> Total Harga     = Rp " + str(totalharga))
    
    #jika pembelian minimal 200rb diberikan diskon 5%
    if totalharga > 200000: 
        setelahdiskon =totalharga-5/100*totalharga   
        print("diskon 5% jika pembelian minimum 200rb = Rp " , str(setelahdiskon))
    
    #dikenakan PPN 1% setiap pembelian
        HargasesudahPPN = totalharga*PPN+setelahdiskon
    #tampilkan harga sesudah PPN
        print(">>> total harga dikenakan Pajak PPN 1% = Rp " + str(HargasesudahPPN))

        
    ulangprog = input(">> Cek Transaksi lagi ? y/t = ")  
    if ulangprog=="t" or ulangprog=="T":
        break 