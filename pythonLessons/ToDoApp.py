task = [] # Boş liste buraya Ekliyoruz!

def add_task():
    eklenen_task = input("Lütfen Görev Ekleyiniz: ")
    task.append(eklenen_task)
    print("Görev başariyla eklendi!")

def show_task():
    if len(task) == 0:
        print("Görev Listesi Boş!")
    else:
        i = 1
        for x in task:
            print(f"{i}. {x}\n")
            i += 1

def delete_task():
    try:
        silinen_task = int(input("Lütfen Silinecek Görev Numarasını Giriniz: "))
        if silinen_task < 1 or silinen_task > len(task):
            print("Geçersiz Görev Numarası!")
        else:
            task.pop(silinen_task - 1)
            print("Görev Başarıyla Silindi!")
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz!")

while True:
    print("""
          1 - Görev Ekle
          2 - Görevleri Göster
          3 - Görev Sil
          4 - Çıkış
          """)
    try:
        secim = int(input("Seçiminiz:"))

        if secim == 1:
            add_task()
        elif secim == 2:
            show_task()
        elif secim == 3:
            delete_task()
        elif secim == 4:
            print("Çıkış yapılıyor...")
            break
        else:
            print("Lütfen Menüden Geçerli Sekmeleri Seçiniz!")
    except ValueError:
         print("Lütfen geçerli bir sayı girin!")
         continue  # Menüye tekrar dön
    
       
        
    
    
    
            
        
     





        


    


    



    


    
