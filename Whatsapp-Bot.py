from selenium import webdriver
import time
import smtplib
import os
from subprocess import call
from getpass import getpass as gizle
from datetime import datetime as zaman
import locale
from selenium.webdriver.firefox.service import Service

print("""
███████╗███████╗██████╗ ██╗   ██╗██████╗ ██╗  ██╗
██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚██╗██╔╝
█████╗  ███████╗██████╔╝ ╚████╔╝ ██████╔╝ ╚███╔╝ 
██╔══╝  ╚════██║██╔═══╝   ╚██╔╝  ██╔══██╗ ██╔██╗ 
███████╗███████║██║        ██║   ██║  ██║██╔╝ ██╗
╚══════╝╚══════╝╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
https://github.com/espyrx/                    coded by espyrx""")

dil = int(input("1) Türkçe\n2) English\n==> "))
if not bool(dil):
    print("Boş Bırakılamaz. /// cannot be left blank.")
    quit()
elif bool(dil):
    pass

if dil == 1:
    dizin = os.getcwd()
    geck = os.path.isfile("{}/geckodriver".format(os.getcwd()))
    if bool(geck):
        pass
    elif not bool(geck):
        print("geckodriver bulunamadı. \nLütfen sisteminize uygun dosyası indirip tekrar deneyin.")
        quit()

    dizin1 = "{}/geckodriver".format(dizin)

    locale.setlocale(locale.LC_ALL, '')
    suan = zaman.now()
    w = zaman.strftime(suan, '%d/%m/%Y %X')

    dizin1 = Service("{}/geckodriver".format(dizin))

    tarayici = webdriver.Firefox(service=dizin1)
    tarayici.get("https://web.whatsapp.com/")
    kontrol=True
    kontrol2=True
    kontrol3=False
    v = "çevrimdışı"
    c = "çevrimiçi"
    def temizle():
        os.system("clear")

    temizle()
    print("ilk iş olarak whatsapp web'e giriş yapmayı unutmayın.")
    time.sleep(5)
    temizle()


    q = input(str("kimi kontrol edeceksiniz?(Hata almamak için tam isim giriniz)\n==> "))
    if not bool(q):
        print("boş bırakılamaz.")
        quit()
    else:
        pass


    isim = tarayici.find_element_by_xpath("//div[contains(@class,'_13NKt copyable-text')]").send_keys(q)
    time.sleep(2)
    tik = tarayici.find_element_by_xpath("//span[contains(@class,'ggj6brxn gfz4du6o')]").click()
    temizle()

    x = input("Sesli bildirim almak ister misiniz? E/H \n==> ")
    if not bool(x):
        print("Bir seçim yapmanız gerekiyor.")
        quit
    elif x == "e" or x == "E":
        pass
    elif x == "h" or x == "H":
        pass
    else:
        print("Evet veya Hayır seçeneğini seçmeniz gerekiyor.")
        quit()



    temizle()


    z = input("Mail bildirimi almak ister misiniz? E/H \n==> ")
    if not bool(z):
        print("Bir seçim yapmanız gerekiyor.")
        quit()
    elif z == "e" or z == "E":
        pass
    elif z == "h" or z == "H":
        pass
    else:
        print("Evet veya Hayır seçeneğini seçmeniz gerekiyor.")
        quit()



    if z == "E" or z == "e":
        temizle()
        gonderici = input("Gönderici Mail adresi? \n(Mail ayarlarınızdan daha az güvenli uygulama erişimini açmanız gerekmektedir.)\n==> ")
        if not bool(gonderici):
            print("Boş bırakılamaz.")
            quit()
        else:
            pass
        temizle()
        sgonderici = gizle("Gönderici mail şifresi?(şifreniz görünmeyecektir siz yazmaya devam edin.) \n==> ")
        if not bool(sgonderici):
            print("Boş bırakılamaz.")
            quit()
        else:
            pass
        temizle()
        alicimail = input("Alıcı mail adresi? \n==> ")
        if not bool(alicimail):
            print("Boş bırakılamaz.")
            quit()
        else:
            pass
    elif z == "H" or  z == "h":
        pass
    else:
        print("Hatalı seçim yaptınız.")
        quit()


    def mail(mesaj):
        baslik = "WhatsApp-Bot"
        content = "Subject: {0}\n\n{1}".format(baslik,mesaj)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gonderici,sgonderici)
        server.sendmail(gonderici,alicimail,content.encode("utf-8"))

    temizle()



    while True:
        if x == "E" or x == "e":
            try:
                tarayici.find_element_by_xpath("//span[text()='çevrimiçi']")
                if kontrol==True:
                    print(c)
                    call(["espeak", "-v", "tr", c])
                    print(50*"-")
                    baslangic = time.time()
                    if z == "e" or z == "E":
                        try:
                            mail("Çevrimiçi!")
                        except Exception as p:
                            print(p)
                            quit()
                    kontrol=False
                    kontrol2=True
                    kontrol3=True
            except:
                kontrol=True
                if kontrol2==True:
                    if kontrol3==True:
                        bitis=int(time.time() - baslangic)
                        print(v,",", bitis, "saniye çevrimiçi kaldı."," /// ", w)
                        print(50*"-")
                        baslangic=time.time()
                        if z == "e" or z == "E":
                            try:
                                msg = (v, bitis, "saniye çevrimiçi kaldı.")
                                mail(msg)
                            except Exception as p:
                                print(p)
                                quit()
                        kontrol2=True
                        kontrol=True
                        kontrol3=False
        elif x == "h" or z == "H":
            try:
                tarayici.find_element_by_xpath("//span[text()='çevrimiçi']")
                if kontrol==True:
                    baslangic = time.time()
                    print(c)
                    print(50*"-")
                    if z == "e" or z == "E":
                        try:
                            mail("Çevrimiçi!")
                        except Exception as p:
                            print(p)
                            quit()
                    kontrol=False
                    kontrol2=True
                    kontrol3=True
            except:
                kontrol=True
                if kontrol2==True:
                    if kontrol3==True:
                        bitis=int(time.time() - baslangic)
                        print(v,",", bitis, "saniye çevrimiçi kaldı.")
                        print(50*"-")
                        if z == "e" or z == "E":
                            try:
                                msg = (v, bitis, "saniye çevrimiçi kaldı.")
                                mail(msg)
                            except Exception as p:
                                print(p)
                                quit()
                        kontrol2=False
                        kontrol3=True
        else:
            print("Hatalı seçim yaptınız.")
            quit()
elif dil == 2:
    dizin = os.getcwd()
    geck = os.path.isfile("{}/geckodriver".format(os.getcwd()))
    if bool(geck):
        pass
    elif not bool(geck):
        print("geckodriver not found. \nplease download the appropriate file for your system.")
        quit()

    dizin1 = "{}/geckodriver".format(dizin)

    locale.setlocale(locale.LC_ALL, '')
    suan = zaman.now()
    w = zaman.strftime(suan, '%d/%m/%Y %X')

    dizin1 = Service("{}/geckodriver".format(dizin))

    tarayici = webdriver.Firefox(service=dizin1)
    tarayici.get("https://web.whatsapp.com/")
    kontrol=True
    kontrol2=True
    kontrol3=False
    v = "Offline"
    c = "Online"
    def temizle():
        os.system("clear")

    temizle()
    print("firstly login on WhatsApp Web.")
    time.sleep(5)
    temizle()


    q = input(str("Who will you control?(Please enter full name to avoid errors.)\n==> "))
    if not bool(q):
        print("cannot be left blank.")
        quit()
    else:
        pass


    isim = tarayici.find_element_by_xpath("//div[contains(@class,'_13NKt copyable-text')]").send_keys(q)
    time.sleep(2)
    tik = tarayici.find_element_by_xpath("//span[contains(@class,'ggj6brxn gfz4du6o')]").click()
    temizle()

    x = input("Would you like to receive sound notification? Y/N \n==> ")
    if not bool(x):
        print("You have to make a choice.")
        quit
    elif x == "y" or x == "Y":
        pass
    elif x == "n" or x == "N":
        pass
    else:
        print("You have to choose Yes or No.")
        quit()



    temizle()


    z = input("Would you like to receive e-mail notification? Y/N \n==> ")
    if not bool(z):
        print("You have to make a choice.")
        quit()
    elif z == "y" or z == "Y":
        pass
    elif z == "y" or z == "Y":
        pass
    else:
        print("You have to choose Yes or No.")
        quit()



    if z == "Y" or z == "y":
        temizle()
        gonderici = input("Sender E-mail address? \n(You need to enable less secure app access in your Mail settings.)\n==> ")
        if not bool(gonderici):
            print("cannot be left blank.")
            quit()
        else:
            pass
        temizle()
        sgonderici = gizle("Sender E-mail Password?(Your password will not appear, just keep typing.) \n==> ")
        if not bool(sgonderici):
            print("cannot be left blank.")
            quit()
        else:
            pass
        temizle()
        alicimail = input("Recipient e-mail address? \n==> ")
        if not bool(alicimail):
            print("cannot be left blank.")
            quit()
        else:
            pass
    elif z == "N" or  z == "n":
        pass
    else:
        print("You made the wrong choice.")
        quit()


    def mail(mesaj):
        baslik = "WhatsApp-Bot"
        content = "Subject: {0}\n\n{1}".format(baslik,mesaj)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gonderici,sgonderici)
        server.sendmail(gonderici,alicimail,content.encode("utf-8"))

    temizle()



    while True:
        if x == "Y" or x == "y":
            try:
                tarayici.find_element_by_xpath("//span[text()='online']")
                if kontrol==True:
                    print(c)
                    call(["espeak", "-v", "en", c])
                    print(50*"-")
                    baslangic = time.time()
                    if z == "y" or z == "Y":
                        try:
                            mail("Online!")
                        except Exception as p:
                            print(p)
                            quit()
                    kontrol=False
                    kontrol2=True
                    kontrol3=True
            except:
                kontrol=True
                if kontrol2==True:
                    if kontrol3==True:
                        bitis=int(time.time() - baslangic)
                        print(v,",", "Stayed online for", bitis, "seconds."," /// ", w)
                        print(50*"-")
                        baslangic=time.time()
                        if z == "y" or z == "Y":
                            try:
                                msg = (v, "Stayed online for", bitis, "seconds.")
                                mail(msg)
                            except Exception as p:
                                print(p)
                                quit()
                        kontrol2=True
                        kontrol=True
                        kontrol3=False
        elif x == "n" or z == "N":
            try:
                tarayici.find_element_by_xpath("//span[text()='online']")
                if kontrol==True:
                    baslangic = time.time()
                    print(c)
                    print(50*"-")
                    if z == "y" or z == "Y":
                        try:
                            mail("Online!")
                        except Exception as p:
                            print(p)
                            quit()
                    kontrol=False
                    kontrol2=True
                    kontrol3=True
            except:
                kontrol=True
                if kontrol2==True:
                    if kontrol3==True:
                        bitis=int(time.time() - baslangic)
                        print(v,",", "Stayed online for", bitis, "seconds.")
                        print(50*"-")
                        if z == "e" or z == "E":
                            try:
                                msg = (v, "Stayed online for", bitis, "seconds.")
                                mail(msg)
                            except Exception as p:
                                print(p)
                                quit()
                        kontrol2=False
                        kontrol3=True
        else:
            print("You made the wrong choice.")
            quit()
