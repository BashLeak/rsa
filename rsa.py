import math
import base64


ascii_deger = []
ascii_islem = []
ascii_son = ""

while True:

    metin = input("şifrelenecek metini giriniz: ")

    if (len(metin) != 0) and (metin.isspace()==False):

        for character in metin :
            ascii_deger.append(ord(character))
        break
    else:
        print("LÜTFEN BOŞ GEÇMEYİNİZ")

        continue

print ("iki adet asal sayı giriniz")

while True :
    try:
        p = input ("1. asal sayıyı giriniz")

        int_p = int(p)
        sayi2 = int(2)

        while sayi2 == 2:

            for i in range (2,int_p-1):
                if  (int_p % i) == 0 :
                    int_p = int(input("sayı asal değildir, lütfen asal bir sayı giriniz"))
                    sayi2 = int(2)
                    break

            else :
                sayi2 = int(1)
        break
    except:
        print("LÜTFEN BİR SAYI GİRİNİZ")




while True :
    try :
        q = input ("2.asal sayıyı giriniz")
        int_q = int(q)

        sayi2 = int(2)
        while sayi2 == 2:

            for i in range (2,int_q-1):
                if  (int_q % i) == 0 :
                    int_q = int(input("sayı asal değildir, lütfen asal bir sayı giriniz"))
                    sayi2 = int(2)
                    break
                elif (int_q == int_p):
                    int_q = int(input("sayılar birbirine eşit olamaz farklı bir sayı giriniz: "))
            else :
                sayi2 = int(1)
        break
    except:
        print("LÜTFEN BİR SAYI GİRİNİZ")

n = int_q * int_p
toti_n = (int_p-1)*(int_q-1)

while True :
    try:
        e = int(input("1 ve "+str(toti_n)+" arasında "+str(toti_n)+" ile arasında asal olan herhangi bir sayı girin"))

        dondur = int(2)

        while dondur == 2:
            if ((e%2 == toti_n%2) or (e%3 == toti_n%3) or (e%5 == toti_n%5)):
                e = int(input(str(toti_n)+" ile arasında asal olan bir sayı giriniz:"))
                dondur = int(2)
            elif (e<=1 or toti_n<=1):
                e = int(input(str(toti_n)+" ile arasında asal olan bir sayı giriniz:"))
                dondur = int(2)
            elif (e >= toti_n) :
                e = int(input(str(toti_n)+" ile arasında asal olan bir sayı giriniz:"))
                dondur = int(2)
            else :
                dondur = int(1)
        break
    except:
        print("lütfen bir sayı giriniz")

print("ortak anahtar "+str(e)+" dir")

for i in range(len(ascii_deger)):
    ascii_islem.append(pow(ascii_deger[i],e)%n)

for i in ascii_islem:
    ascii_son = ascii_son+str(i)


stringBytes = ascii_son.encode("utf8")
base64_bytes = base64.b64encode(stringBytes)
base64_ascii = base64_bytes.decode("utf8")

print("\n"+base64_ascii+"\n")
