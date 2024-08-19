
# HAVA-SU-ATEŞ-TOPRAK (4 ELEMENT) OYUNU
# Oyun,kullanıcı ve bilgisayar arasında gerçekleşecektir.
# 3 turdan oluşacaktır.3 turu kazanan oyunu kazanır.
# Oyun berabere kalabilir,kullanıcı kazanabilir veya bilgisayar kazanabilir.        




#3 turu kazanan galip olur. 4 elementten birini seçmek zorundasınız , farklı bir şey yazarsanız bilgisayar puan alır.

print("Seçenekler : Hava ,Su, Toprak ,Ateş")


import random 
secenekler = ["toprak","hava","ateş","su"]
devammı_tamammı = ["evet","hayır"]
tur_sayısı =0
oynanan_oyun_sayısı=0
bilgisayar_puanı = 0
kullanıcı_puanı = 0


      
while bilgisayar_puanı < 3 and kullanıcı_puanı<3:
    
    bilgisayar_secimi = random.choice(secenekler)
    kullanıcı_secimi = input(" kullanıcı seçimi   :")
    print("Bilgisayarın seçimi   :",bilgisayar_secimi)
    
    
    if  kullanıcı_secimi not in secenekler:
        
        print("Lütfen tekrar giriniz  : ")
      
    if bilgisayar_secimi == kullanıcı_secimi:
            print("bilgisayar skoru :" + str(bilgisayar_puanı) + "\n" + "kullanıcı skoru  :"  + str(kullanıcı_puanı))
            print("Berabere")
            tur_sayısı +=1
            
    elif kullanıcı_secimi == "toprak":
            if bilgisayar_secimi == "hava":
                bilgisayar_puanı +=1
                print("bilgisayar skoru :"  + str(bilgisayar_puanı) + "\n" + "kullanıcı skoru :" + str(kullanıcı_puanı))
                print("kazanan bilgisayar.Hava ,toprağı dağıtır.")
                tur_sayısı +=1
            if bilgisayar_secimi == "ateş":
                kullanıcı_puanı +=1
                print("bilgisayar skoru :"  + str(bilgisayar_puanı) + "\n" + "kullanıcı skoru :" + str(kullanıcı_puanı))       
                print("Kazanan kullanıcı .Toprak, ateşi engeller.")
                tur_sayısı +=1
                print("Tur sayısı :",tur_sayısı)
            if bilgisayar_secimi == "su":
                kullanıcı_puanı +=1
                print("bilgisayar skoru :"  + str(bilgisayar_puanı) + "\n" + "kullanıcı skoru :" + str(kullanıcı_puanı))
                print("kazanan kullanıcı .Toprak ,suyu emer.")
                tur_sayısı +=1
                 

    elif  kullanıcı_secimi == "hava":
          
            if bilgisayar_secimi == "toprak":
                kullanıcı_puanı +=1
                print("bilgisayar skoru :"  + str(bilgisayar_puanı) + "\n" + "kullanıcı skoru :" + str(kullanıcı_puanı))
                print("Kazanan kullanıcı .Hava ,toprağı dağıtır.")
                tur_sayısı += 1
            if bilgisayar_secimi == "ateş":
                kullanıcı_puanı +=1
                print("ilgisayar skoru :"  + str(bilgisayar_puanı) + "\n" + "kullanıcı skoru :" + str(kullanıcı_puanı))
                print("kazanan kullanıcı ,hava ateşi dağıtır.")
                tur_sayısı += 1
            if  bilgisayar_secimi == "su":
                kullanıcı_puanı +=1
                print("bilgisayar skoru :"  + str(bilgisayar_puanı) + "\n" + "kullanıcı skoru :" + str(kullanıcı_puanı))
                print("Kazanan kullanıcı .Hava ,suyu buharlaştırır.")
                tur_sayısı     

    elif kullanıcı_secimi == "su":
            if bilgisayar_secimi == "toprak":
                bilgisayar_puanı +=1
                print("Kazanan bilgisayar .Toprak suyu emer.")
                print("Bilgisayar skoru :" + str(bilgisayar_puanı) + "\n" + "kullanıcı skoru :" + str(kullanıcı_puanı) )
                tur_sayısı +=1
            if bilgisayar_secimi == "hava":
                bilgisayar_puanı +=1 
                print("Kazanan bilgisayar .Hava ,toprağı dağıtır.")
                print("Bilgisayar skoru :" + str(bilgisayar_puanı) + "\n" + "kullanıcı skoru :" + str(kullanıcı_puanı) )
                tur_sayısı +=1
            if  bilgisayar_secimi == "ateş":
                kullanıcı_puanı +=1
                print("Bilgisayar skoru :" + str(bilgisayar_puanı) + "\n" + "kullanıcı skoru :" + str(kullanıcı_puanı) )
                print("Kazanan kullanıcı .Su,ateşi söndürür")
                tur_sayısı +=1
    else:         
            if bilgisayar_secimi == "toprak":
                bilgisayar_puanı +=1
                print("bilgisayar skoru :"  + str(bilgisayar_puanı) + "\n" + "kullanıcı skoru :" + str(kullanıcı_puanı))
                print("Kazanan bilgisayar .Toprak, ateşi engeller.")
                tur_sayısı +=1
            if bilgisayar_secimi == "hava":
                bilgisayar_puanı +=1
                print("bilgisayar skoru :"  + str(bilgisayar_puanı) + "\n" + "kullanıcı skoru :" + str(kullanıcı_puanı))
                print("kazanan bilgisayar. hava, ateşi dağıtır.")
                tur_sayısı +=1
            if bilgisayar_secimi == "su":
                bilgisayar_puanı +=1
                print("bilgisayar skoru :"  + str(bilgisayar_puanı) + "\n" + "kullanıcı skoru :" + str(kullanıcı_puanı))
                print("Kazanan bilgisayar !Su ,ateşi söndürür.")
                tur_sayısı +=1
print("Kullanıcı  : " , kullanıcı_puanı ,"Bilgisayar  :" ,bilgisayar_puanı)


if bilgisayar_puanı == 3 :
    print("oyun bitti kazanan bilgisayar")
    bilgisayar_secimi =random.choice(devammı_tamammı)
    if bilgisayar_secimi == "evet":
         print("Oyun ,devam etsin ")
    else :
         print("Oyun ,devam etmesin")    

if kullanıcı_puanı == 3:
    tur_sayısı +=1
    print("Kazanan ,kullanıcı .Devam etmek ister misiniz ? Lütfen evet veya hayır giriniz.")
    kullanıcı_secimi = input("Seçiminizi giriniz : ")
    if kullanıcı_secimi == "hayır":
        
        print("Oyun bitti  Kazanan kullanıcı")
        
    if kullanıcı_secimi == "evet":
             print("Oyun, devam etsin")     
             
else:
    print("Berabere")
   
