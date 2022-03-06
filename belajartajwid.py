def belajar():
    while True:
        daftarpelajaran = [""] * (7)
        
        listpembelajaran = 6
        print("Pilih ilmu tajwid yang akan dipelajari.")
        for i in range(0, listpembelajaran + 1, 1):
            daftarpelajaran[0] = "[1] Hukum Nun Bersukun"
            daftarpelajaran[1] = "[2] Hukum Mim Bersukun"
            daftarpelajaran[2] = "[3] Hukum Mim dan Nun Bertasydid"
            daftarpelajaran[3] = "[4] Hukum Idgham"
            daftarpelajaran[4] = "[5] Hukum Lam Ta'rif"
            daftarpelajaran[5] = "[6] Hukum Qalqalah"
            daftarpelajaran[6] = "[7] Hukum Mad"
            print(daftarpelajaran[i])
        print("[0] Kembali")
        pilihan = int(input())
        if pilihan == 1:
            print("Hukum nun bersukun atau tanwin adalah empat hukum yang muncul tatkala nun bersukun atau tanwin menghadapi huruf hijaiyah.")
            print("Empat hukum tersebut ialah: Idzhar Halqi, Idgham, Iqlab, dan Ikhfa'.")
        else:
            if pilihan == 2:
                print("Hukum mim bersukun ialah tiga hukum yang muncul tatkala mim bersukun menghadapi huruf hijaiyah.")
                print("Tiga hukum itu diantaranya: Ikhfa Syafawi, Idgham Mimi, Idzhar Syafawi.")
            else:
                if pilihan == 3:
                    print("Jika kita membaca Al-Quran kemudian menemukan huruf mim dan nun yang bertasydid, maka disana terdapat hukum Ghunnah Musyaddadah. ")
                    print("Ghunnah menurut bahasa artinya sengau atau dengung (mendengung), musyaddadah artinya bertasydid atau memakai tasydid.")
                else:
                    if pilihan == 4:
                        print("Hukum idgham ialah tiga hukum yang muncul tatkala dua huruf yang sama, sejenis atau berdekatan makhraj atau sifat-sifatnya saling berhadapan. Tiga hukum itu ialah: Idgham Mutamatsilain, Idgham Mutajanisain, dan Idgham Mutaqaribain.")
                    else:
                        if pilihan == 5:
                            print("Hukum Lam Ta’rif membahas tentang alif lam ketika menghadapi huruf hijaiyah, baik yang tergolong huruf-huruf qamariyyah maupun huruf-huruf syamsiyyah.")
                        else:
                            if pilihan == 6:
                                print("Qalqalah menurut bahasa ialah bergerak atau bergetar. Sedangkan menurut istilah, qalqalah ialah suara tambahan (pantulan) yang kuat dan jelas yang terjadi pada huruf yang bersukun setelah menekan pada makhraj huruf tersebut. Huruf-huruf qalqalah ada 5, yaitu ق,ط ,ب ,ج ,dan د. Dalam ilmu tajwid, qalqalah terbagi menjadi dua, yaitu qalqalah shughra dan qalqalah kubra.")
                            else:
                                if pilihan == 7:
                                    print("Mad menurut bahasa ialah memanjangkan dan menambah. Sedangkan menurut istilah mad ialah memanjangkan suara dengan salah satu huruf dari huruf-huruf mad (ashli). Huruf mad seperti yang dimaksudkan dalam definisi diatas ada tiga, yaitu ا ,و dan ي . Mad terbagi atas dua bagian, yaitu:")
                                    print("Mad Ashli, yang dikenal dengan istilah mad thabi’i. Thabi’i secara bahasa artinya tabiat. Mad ashli diistilahkan pula dengan mad thabi’i karena seseorang yang mempunyai tabiat baik tidak mungkin akan mengurangi atau menambah panjang bacaan dari yang telah ditetapkan. Adapun cara membaca mad Ashli ialah dengan memanjangkan bacaan dua harakat (satu alif), baik disaat washal maupun waqaf.")
                                    print("Mad Far’i. Far’i secara bahasa ialah cabang. Sedangkan menurut istilah, mad far’i ialah mad yang merupakan hukum tambahan dari mad ashli (sebagai hukum asalnya), yang disebabakan oleh hamzah atau sukun. Hukum-hukum yang merupakan bagian dari mad far’i antara lain: Mad Wajib Muttashil, Mad Jaiz Munfashil, Mad Lazim Harfi Musyba, Mad Lazim Harfi Mukhafaf, Mad Lazim Kalimi Mutsaqal, Mad Lazim Kalimi Mukhafaf, Mad Badal, Mad Aridl Lissukun, Mad Iwadl, Mad Lin, Mad Shilah Qashirah, Mad Shilah Thawilah, Mad Tamkin, dan Mad Farqi.")
                                else:
                                    if pilihan == 0:
                                        main()
                                    else:
                                        print("Invalid input.")
        print("Lanjutkan pembelajaran?")
        print("[1] Ya")
        print("[2] Tidak")
        lanjut = int(input())
        if lanjut == 1:
            pass
        else:
            if lanjut == 2:
                main()
            else:
                print("Invalid.")

def hasilNilai(hasilakhir):
    # Jawaban: b, a, b, c, a, c, c, b, a, a
    print("Latihan telah selesai.")
    print("Skor yang anda dapatkan adalah: " + str(hasilakhir))
    print("[1] Ulangi latihan")
    print("[0] Kembali ke menu utama")
    pilihan = int(input())
    if pilihan == 1:
        latihan()
    else:
        if pilihan == 0:
            main()
        else:
            print("Invalid input.")

def hitungNilai(nilai, hasilakhir):
    hasil = hasilakhir + nilai
    
    return hasil

def info():
    print("Hubungi kami jika ada suatu masalah dalam aplikasi Ilmu Tajwid di kontak tertera.")
    print("E-mail: rayyangaming@gmail.com")
    main()

def latihan():
    jawaban = [0] * (3)
    daftarjawaban = [""] * (3)
    
    print("1). الَّذِيْنَ اَنْعَمْتَ عَلَيْهِمْ. Di bagian potongan ayat manakah terdapat hukum bacaan Idzhar?")
    print("a. االَّذِيْنَ")
    jawaban[0] = 1
    daftarjawaban[0] = "االَّذِيْنَ"
    print("b. اَنْعَمْتَ")
    jawaban[1] = 2
    daftarjawaban[1] = "اَنْعَمْتَ"
    print("c. عَلَيْهِم")
    jawaban[2] = 3
    daftarjawaban[2] = "عَلَيْهِم"
    pilihan = input()
    pilihanjwb = ord(pilihan) - ord("a") + 1
    if pilihanjwb > 3:
        print("Error input.")
        latihan()
    a = jawaban[0]
    b = jawaban[1]
    c = jawaban[2]
    nilaitengah = jawaban[1]
    if nilaitengah == pilihanjwb:
        pilihanjwb = ord("a") + 1
        pilihan = chr(pilihanjwb)
        print("Benar. Jawabannya adalah: " + pilihan + ". " + daftarjawaban[1])
    else:
        if nilaitengah > pilihanjwb:
            nilaitengah = nilaitengah - 1
            if nilaitengah == pilihanjwb:
                pilihanjwb = ord("a") + 1
                pilihan = chr(pilihanjwb)
                print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[1])
        else:
            if nilaitengah < pilihanjwb:
                nilaitengah = nilaitengah + 1
                if nilaitengah == pilihanjwb:
                    pilihanjwb = ord("a") + 1
                    pilihan = chr(pilihanjwb)
                    print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[1])
            else:
                print("Invalid.")
    jawabanbenar = jawaban[1]
    if nilaitengah == jawabanbenar:
        nilai = 2
    else:
        nilai = 0
    hasilakhir = 0
    hasilakhir = hitungNilai(nilai, hasilakhir)
    latihan2(hasilakhir)

def latihan10(hasilakhir):
    jawaban = [0] * (3)
    daftarjawaban = [""] * (3)
    
    print("                                                                                                         ")
    print("10). قُلُوْبَهُمْ قٰسِيَةً. Hukum bacaan terdapat dalam bagian ayat tersebut adalah...")
    print("a. Idzhar Syafawi")
    jawaban[0] = 1
    daftarjawaban[0] = "Idzhar Syafawi"
    print("b. Ikhfa' Syafawi")
    jawaban[1] = 2
    daftarjawaban[1] = "Ikhfa' Syafawi"
    print("c. Iqlab")
    jawaban[2] = 3
    daftarjawaban[2] = "Iqlab"
    pilihan = input()
    pilihanjwb = ord(pilihan) - ord("a") + 1
    if pilihanjwb > 3:
        print("Error input.")
        latihan10(hasilakhir)
    a = jawaban[0]
    b = jawaban[1]
    c = jawaban[2]
    nilaitengah = jawaban[1]
    if nilaitengah == pilihanjwb:
        pilihanjwb = ord("a")
        pilihan = chr(pilihanjwb)
        print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[0])
    else:
        if nilaitengah > pilihanjwb:
            nilaitengah = nilaitengah - 1
            if nilaitengah == pilihanjwb:
                pilihanjwb = ord("a")
                pilihan = chr(pilihanjwb)
                print("Benar. Jawabannya adalah: " + pilihan + ". " + daftarjawaban[0])
        else:
            if nilaitengah < pilihanjwb:
                nilaitengah = nilaitengah + 1
                if nilaitengah == pilihanjwb:
                    pilihanjwb = ord("a")
                    pilihan = chr(pilihanjwb)
                    print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[0])
            else:
                print("Invalid.")
    jawabanbenar = jawaban[0]
    if nilaitengah == jawabanbenar:
        nilai = 2
    else:
        nilai = 0
    hasilakhir = hitungNilai(nilai, hasilakhir)
    hasilNilai(hasilakhir)

def latihan2(hasilakhir):
    jawaban = [0] * (3)
    daftarjawaban = [""] * (3)
    
    print("                                                                                                         ")
    print("2). شَعَاۤىِٕرَ اللّٰهِ. Di dalam potongan ayat tersebut terdapat mad...")
    print("a. Mad Wajib Muttashil")
    jawaban[0] = 1
    daftarjawaban[0] = "Mad Wajib Muttashil"
    print("b. Mad Jaiz Munfashil")
    jawaban[1] = 2
    daftarjawaban[1] = "Mad Jaiz Munfashil"
    print("c. Mad Aridl Lissukun")
    jawaban[2] = 3
    daftarjawaban[2] = "Mad Aridl Lissukun"
    pilihan = input()
    pilihanjwb = ord(pilihan) - ord("a") + 1
    if pilihanjwb > 3:
        print("Error input.")
        latihan2(hasilakhir)
    a = jawaban[0]
    b = jawaban[1]
    c = jawaban[2]
    nilaitengah = jawaban[1]
    if nilaitengah == pilihanjwb:
        pilihanjwb = ord("a")
        pilihan = chr(pilihanjwb)
        print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[0])
    else:
        if nilaitengah > pilihanjwb:
            nilaitengah = nilaitengah - 1
            if nilaitengah == pilihanjwb:
                pilihanjwb = ord("a")
                pilihan = chr(pilihanjwb)
                print("Benar. Jawabannya adalah: " + pilihan + ". " + daftarjawaban[0])
        else:
            if nilaitengah < pilihanjwb:
                nilaitengah = nilaitengah + 1
                if nilaitengah == pilihanjwb:
                    pilihanjwb = ord("a")
                    pilihan = chr(pilihanjwb)
                    print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[0])
            else:
                print("Invalid.")
    jawabanbenar = jawaban[0]
    if nilaitengah == jawabanbenar:
        nilai = 2
    else:
        nilai = 0
    hasilakhir = hitungNilai(nilai, hasilakhir)
    latihan3(hasilakhir)

def latihan3(hasilakhir):
    jawaban = [0] * (3)
    daftarjawaban = [""] * (3)
    
    print("                                                                                                         ")
    print("Secara bahasa, Ikhfa’ artinya ...")
    print("a. Menggantikan")
    jawaban[0] = 1
    daftarjawaban[0] = "Menggantikan"
    print("b. Menyamarkan")
    jawaban[1] = 2
    daftarjawaban[1] = "Menyamarkan"
    print("c. Memasukkan")
    jawaban[2] = 3
    daftarjawaban[2] = "Memasukkan"
    pilihan = input()
    pilihanjwb = ord(pilihan) - ord("a") + 1
    if pilihanjwb > 3:
        print("Error input.")
        latihan3(hasilakhir)
    a = jawaban[0]
    b = jawaban[1]
    c = jawaban[2]
    nilaitengah = jawaban[1]
    if nilaitengah == pilihanjwb:
        pilihanjwb = ord("a") + 1
        pilihan = chr(pilihanjwb)
        print("Benar. Jawabannya adalah: " + pilihan + ". " + daftarjawaban[1])
    else:
        if nilaitengah > pilihanjwb:
            nilaitengah = nilaitengah - 1
            if nilaitengah == pilihanjwb:
                pilihanjwb = ord("a") + 1
                pilihan = chr(pilihanjwb)
                print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[1])
        else:
            if nilaitengah < pilihanjwb:
                nilaitengah = nilaitengah + 1
                if nilaitengah == pilihanjwb:
                    pilihanjwb = ord("a") + 1
                    pilihan = chr(pilihanjwb)
                    print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[1])
            else:
                print("Invalid.")
    jawabanbenar = jawaban[1]
    if nilaitengah == jawabanbenar:
        nilai = 2
    else:
        nilai = 0
    hasilakhir = hitungNilai(nilai, hasilakhir)
    latihan4(hasilakhir)

def latihan4(hasilakhir):
    jawaban = [0] * (3)
    daftarjawaban = [""] * (3)
    
    print("                                                                                                         ")
    print("Apabila nun sukun atau tanwin bertemu dengan huruf lam (ل), maka hukum bacaannya adalah...")
    print("a. Ikhfa'")
    jawaban[0] = 1
    daftarjawaban[0] = "Ikhfa'"
    print("b. Iqlab")
    jawaban[1] = 2
    daftarjawaban[1] = "Iqlab"
    print("c. Idgham Bilaghunnah")
    jawaban[2] = 3
    daftarjawaban[2] = "Idgham Bilaghunnah"
    pilihan = input()
    pilihanjwb = ord(pilihan) - ord("a") + 1
    if pilihanjwb > 3:
        print("Error input.")
        latihan4(hasilakhir)
    a = jawaban[0]
    b = jawaban[1]
    c = jawaban[2]
    nilaitengah = jawaban[1]
    if nilaitengah == pilihanjwb:
        pilihanjwb = ord("a") + 2
        pilihan = chr(pilihanjwb)
        print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[2])
    else:
        if nilaitengah > pilihanjwb:
            nilaitengah = nilaitengah - 1
            if nilaitengah == pilihanjwb:
                pilihanjwb = ord("a") + 2
                pilihan = chr(pilihanjwb)
                print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[2])
        else:
            if nilaitengah < pilihanjwb:
                nilaitengah = nilaitengah + 1
                if nilaitengah == pilihanjwb:
                    pilihanjwb = ord("a") + 2
                    pilihan = chr(pilihanjwb)
                    print("Benar. Jawabannya adalah: " + pilihan + ". " + daftarjawaban[2])
            else:
                print("Invalid.")
    jawabanbenar = jawaban[2]
    if nilaitengah == jawabanbenar:
        nilai = 2
    else:
        nilai = 0
    hasilakhir = hitungNilai(nilai, hasilakhir)
    latihan5(hasilakhir)

def latihan5(hasilakhir):
    jawaban = [0] * (3)
    daftarjawaban = [""] * (3)
    
    print("                                                                                                         ")
    print("5). فَوَيْلٌ لِّلْمُصَلِّيْنَ. Hukum bacaan yang terdapat dalam ayat di samping adalah....")
    print("a. Idgham Bilaghunnah")
    jawaban[0] = 1
    daftarjawaban[0] = "Idgham Bilaghunnah"
    print("b. Idgham Bighunnah")
    jawaban[1] = 2
    daftarjawaban[1] = "Idgham Bighunnah"
    print("c. Ikhfa' Syafawi")
    jawaban[2] = 3
    daftarjawaban[2] = "Ikhfa' Syafawi"
    pilihan = input()
    pilihanjwb = ord(pilihan) - ord("a") + 1
    if pilihanjwb > 3:
        print("Error input.")
        latihan5(hasilakhir)
    a = jawaban[0]
    b = jawaban[1]
    c = jawaban[2]
    nilaitengah = jawaban[1]
    if nilaitengah == pilihanjwb:
        pilihanjwb = ord("a")
        pilihan = chr(pilihanjwb)
        print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[0])
    else:
        if nilaitengah > pilihanjwb:
            nilaitengah = nilaitengah - 1
            if nilaitengah == pilihanjwb:
                pilihanjwb = ord("a")
                pilihan = chr(pilihanjwb)
                print("Benar. Jawabannya adalah: " + pilihan + ". " + daftarjawaban[0])
        else:
            if nilaitengah < pilihanjwb:
                nilaitengah = nilaitengah + 1
                if nilaitengah == pilihanjwb:
                    pilihanjwb = ord("a")
                    pilihan = chr(pilihanjwb)
                    print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[0])
            else:
                print("Invalid.")
    jawabanbenar = jawaban[0]
    if nilaitengah == jawabanbenar:
        nilai = 2
    else:
        nilai = 0
    hasilakhir = hitungNilai(nilai, hasilakhir)
    latihan6(hasilakhir)

def latihan6(hasilakhir):
    jawaban = [0] * (3)
    daftarjawaban = [""] * (3)
    
    print("                                                                                                         ")
    print("6). وَالْمُتَرَدِّيَةُ. Hukum bacaan yang tepat dalam bagian ayat di samping adalah....")
    print("a. Idgham Syamsiyyah")
    jawaban[0] = 1
    daftarjawaban[0] = "Idgham Syamsiyyah"
    print("b. Idgham Bilaghunnah")
    jawaban[1] = 2
    daftarjawaban[1] = "Idgham Bilaghunnah"
    print("c. Idzhar Qamariyyah")
    jawaban[2] = 3
    daftarjawaban[2] = "Idzhar Qamariyyah"
    pilihan = input()
    pilihanjwb = ord(pilihan) - ord("a") + 1
    if pilihanjwb > 3:
        print("Error input.")
        latihan6(hasilakhir)
    a = jawaban[0]
    b = jawaban[1]
    c = jawaban[2]
    nilaitengah = jawaban[1]
    if nilaitengah == pilihanjwb:
        pilihanjwb = ord("a") + 2
        pilihan = chr(pilihanjwb)
        print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[2])
    else:
        if nilaitengah > pilihanjwb:
            nilaitengah = nilaitengah - 1
            if nilaitengah == pilihanjwb:
                pilihanjwb = ord("a") + 2
                pilihan = chr(pilihanjwb)
                print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[2])
        else:
            if nilaitengah < pilihanjwb:
                nilaitengah = nilaitengah + 1
                if nilaitengah == pilihanjwb:
                    pilihanjwb = ord("a") + 2
                    pilihan = chr(pilihanjwb)
                    print("Benar. Jawabannya adalah: " + pilihan + ". " + daftarjawaban[2])
            else:
                print("Invalid.")
    jawabanbenar = jawaban[2]
    if nilaitengah == jawabanbenar:
        nilai = 2
    else:
        nilai = 0
    hasilakhir = hitungNilai(nilai, hasilakhir)
    latihan7(hasilakhir)

def latihan7(hasilakhir):
    jawaban = [0] * (3)
    daftarjawaban = [""] * (3)
    
    print("                                                                                                         ")
    print("7). وَالنَّطِيْحَةُ. Hukum bacaan yang terdapat dalam bagian ayat di samping adalah....")
    print("a. Idzhar Qamariyyah")
    jawaban[0] = 1
    daftarjawaban[0] = "Idzhar Qamariyyah"
    print("b. Idgham Bilaghunnah")
    jawaban[1] = 2
    daftarjawaban[1] = "Idgham Bilaghunnah"
    print("c. Idgham Syamsiyyah")
    jawaban[2] = 3
    daftarjawaban[2] = "Idgham Syamsiyyah"
    pilihan = input()
    pilihanjwb = ord(pilihan) - ord("a") + 1
    if pilihanjwb > 3:
        print("Error input.")
        latihan7(hasilakhir)
    a = jawaban[0]
    b = jawaban[1]
    c = jawaban[2]
    nilaitengah = jawaban[1]
    if nilaitengah == pilihanjwb:
        pilihanjwb = ord("a") + 2
        pilihan = chr(pilihanjwb)
        print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[2])
    else:
        if nilaitengah > pilihanjwb:
            nilaitengah = nilaitengah - 1
            if nilaitengah == pilihanjwb:
                pilihanjwb = ord("a") + 2
                pilihan = chr(pilihanjwb)
                print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[2])
        else:
            if nilaitengah < pilihanjwb:
                nilaitengah = nilaitengah + 1
                if nilaitengah == pilihanjwb:
                    pilihanjwb = ord("a") + 2
                    pilihan = chr(pilihanjwb)
                    print("Benar. Jawabannya adalah: " + pilihan + ". " + daftarjawaban[2])
            else:
                print("Invalid.")
    jawabanbenar = jawaban[2]
    if nilaitengah == jawabanbenar:
        nilai = 2
    else:
        nilai = 0
    hasilakhir = hitungNilai(nilai, hasilakhir)
    latihan8(hasilakhir)

def latihan8(hasilakhir):
    jawaban = [0] * (3)
    daftarjawaban = [""] * (3)
    
    print("                                                                                                         ")
    print("8). Apabila mim sukun (مْ) bertemu dengan mim berharakat, maka hukum bacaannya adalah...")
    print("a. Idgham Bighunnah")
    jawaban[0] = 1
    daftarjawaban[0] = "Idgham Bighunnah"
    print("b. Idgham Mimi")
    jawaban[1] = 2
    daftarjawaban[1] = "Idgham Mimi"
    print("c. Idgham Syamsiyyah")
    jawaban[2] = 3
    daftarjawaban[2] = "Idgham Syamsiyyah"
    pilihan = input()
    pilihanjwb = ord(pilihan) - ord("a") + 1
    if pilihanjwb > 3:
        print("Error input.")
        latihan8(hasilakhir)
    a = jawaban[0]
    b = jawaban[1]
    c = jawaban[2]
    nilaitengah = jawaban[1]
    if nilaitengah == pilihanjwb:
        pilihanjwb = ord("a") + 2
        pilihan = chr(pilihanjwb)
        print("Benar. Jawabannya adalah: " + pilihan + ". " + daftarjawaban[1])
    else:
        if nilaitengah > pilihanjwb:
            nilaitengah = nilaitengah - 1
            if nilaitengah == pilihanjwb:
                pilihanjwb = ord("a") + 2
                pilihan = chr(pilihanjwb)
                print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[1])
        else:
            if nilaitengah < pilihanjwb:
                nilaitengah = nilaitengah + 1
                if nilaitengah == pilihanjwb:
                    pilihanjwb = ord("a") + 2
                    pilihan = chr(pilihanjwb)
                    print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[1])
            else:
                print("Invalid.")
    jawabanbenar = jawaban[1]
    if nilaitengah == jawabanbenar:
        nilai = 2
    else:
        nilai = 0
    hasilakhir = hitungNilai(nilai, hasilakhir)
    latihan9(hasilakhir)

def latihan9(hasilakhir):
    jawaban = [0] * (3)
    daftarjawaban = [""] * (3)
    
    print("                                                                                                         ")
    print("9). يٰٓاَيُّهَا. Mad yang terdapat dalam bagian ayat tersebut adalah...")
    print("a. Mad Jaiz Munfashil")
    jawaban[0] = 1
    daftarjawaban[0] = "Mad Jaiz Munfashil"
    print("b. Mad Wajib Muttashil")
    jawaban[1] = 2
    daftarjawaban[1] = "Mad Wajib Muttashil"
    print("c. Mad Lazim Kilmi Mukhoffaf")
    jawaban[2] = 3
    daftarjawaban[2] = "Mad Lazim Kilmi Mukhoffaf"
    pilihan = input()
    pilihanjwb = ord(pilihan) - ord("a") + 1
    if pilihanjwb > 3:
        print("Error input.")
        latihan9(hasilakhir)
    a = jawaban[0]
    b = jawaban[1]
    c = jawaban[2]
    nilaitengah = jawaban[1]
    if nilaitengah == pilihanjwb:
        pilihanjwb = ord("a")
        pilihan = chr(pilihanjwb)
        print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[0])
    else:
        if nilaitengah > pilihanjwb:
            nilaitengah = nilaitengah - 1
            if nilaitengah == pilihanjwb:
                pilihanjwb = ord("a")
                pilihan = chr(pilihanjwb)
                print("Benar. Jawabannya adalah: " + pilihan + ". " + daftarjawaban[0])
        else:
            if nilaitengah < pilihanjwb:
                nilaitengah = nilaitengah + 1
                if nilaitengah == pilihanjwb:
                    pilihanjwb = ord("a")
                    pilihan = chr(pilihanjwb)
                    print("Jawaban Anda salah. Yang benar adalah: " + pilihan + ". " + daftarjawaban[0])
            else:
                print("Invalid.")
    jawabanbenar = jawaban[0]
    if nilaitengah == jawabanbenar:
        nilai = 2
    else:
        nilai = 0
    hasilakhir = hitungNilai(nilai, hasilakhir)
    latihan10(hasilakhir)

def main():
    while True:
        print("Selamat datang di aplikasi Belajar Tajwid")
        print("[1] Belajar")
        print("[2] Latihan")
        print("[3] Info")
        print("[0] Keluar")
        pilihan = int(input())
        if pilihan == 1:
            belajar()
        else:
            if pilihan == 2:
                latihan()
            else:
                if pilihan == 3:
                    info()
                else:
                    if pilihan == 0:
                        print("Terima kasih telah menggunakan aplikasi kami :)")
                        exit()
                    else:
                        print("Invalid input.")
main()