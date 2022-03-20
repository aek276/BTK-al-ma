import random
zorluk = input("Bir seviye seçiniz (kolay/orta/zor): ".upper()# lower yazıyı küçüğe upper büyüğe çevirir

    if zorluk =="kolay":
            tuttugumsayi = random.randint(1,10)
        elif zorluk == "orta":
            tuttugumsayi = random.randint(1,50)
        elif zorluk == "zor":
            tuttugumsayi = random.randint(1,100)

        else:
            print("Yanlıs seviye girildi")

while True:
    a = int(input("Sayıyı tahmin et."))
    if a==tuttugumsayi:
      print("sayıyı buldunuz")
      break
    elif a > tuttugumsayi:
        print("Sayınız Küçültün")
    elif a < tuttugumsayi:
        print("Sayınız büyütün")
