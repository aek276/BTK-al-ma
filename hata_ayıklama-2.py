try:
    sayi1=int(input("Bir sayı giriniz:"))
    sayi2=int(input("Bir sayı girin"))
    print("Sayılarınızın bölümü:",sayi1/sayi2)
except ValueError:
    print("Girdiğiniz değer int olmalı")
except ZeroDivisionError:
    print("Bir sayı sıfıra bölünemez")
except:
    print("Genel hata")