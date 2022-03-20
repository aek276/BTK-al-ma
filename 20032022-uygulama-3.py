import  os

try:
    for i in range(1,100):
    os.mkdir("C:/Users/egitim.sinif2/Desktop/ahmetkaya"+str(i))
except:
    print(Dosya var zaten)