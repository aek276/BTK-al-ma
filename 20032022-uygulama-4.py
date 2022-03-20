import  os
try:
    os.mkdir("elma")
except FileExistsError:
    print("Oluşturmak istediğiniz dosya hali hazırda zaten var ")