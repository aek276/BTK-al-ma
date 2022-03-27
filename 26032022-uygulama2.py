#kendisine gönderilen kullanıcı adı ve şifreyi kontrol ederek
#sonucunda true ya da false gönderen fonksiyonun python kodu
#kullanıcıadı: admin , şifre: 123456 olamlı
def kontrol(kullanici,sifre):
    if kullanici=="admin" and sifre=="123456" :

    else :
        return False
kullanici=input("Kullanıcı Adınız:")
sifre=input("Şifreniz:")
sonuc=kontrol(kullanici,sifre)
if sonuc==True:
    print("Doğru girdiniz")
else :
    print("Kullanıcı adı veya Şifre hatalı")