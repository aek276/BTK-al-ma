#kullanıcıdan isim, soyisim, telefon numarası alarak bir listeye atayımız.
bilgiler=[]#boş liste tanımlar
isim=input("isminiz:")
soyad=input("soyadınız:")
telno=(input("telefon numarası:"))
bilgiler.append(isim)
bilgiler.append(soyad)
bilgiler.append(telno)
print(bilgiler)
print("Adı:",bilgiler[0])
print("Soyadı:",bilgiler[1])
print("Telefon No:",bilgiler[2])