#KARŞILAŞTIRMA OPERATÖRLERİ
"""
<  : Küçüktür
>  : Büyüktür
<= : Küçük eşit
>= : Büyük eşit
== : Eşittir
!= : Eşit değildir
"""
cinsiyet=input("Bir harf giriniz:")

if cinsiyet=="e" or cinsiyet=="E":#or: 2 şarttan biri doğru ise çalışır.
    print("Cinsiyet olarak Erkek girdiniz")
    print("if içerisinden selamlar")
elif cinsiyet=="k" or "K":#2. veya daha sonraki şartları eklemek için elif kullanılır
    print("Cinsiyet olarak Kadın girdiniz")
    print("Şuanda elif bloğu içinden mesaj veriyorum")
else: #şartların dışında herhamgi birşey girilirse çalışır
    print("Ben sana e ya da k gir demdedim mi?")
    print("Şuanda if dışındasın")
