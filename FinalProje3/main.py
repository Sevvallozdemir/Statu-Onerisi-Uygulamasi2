from insan import insan
from issiz import İssiz
from calisan import calisan
from mavi_yaka import maviYaka
from beyaz_yaka import beyazYaka
import pandas as pd





def main():
        #insan nesneleri

        insan1=insan("123456963","Şevval","Özdemir",20,"Kadın","Türk")
        insan2=insan("147852369","Elif","Özdemir",30,"Kadın","Türk")
        print("İnsan Nesneleri")
        print(insan1)
        print(insan2)


        #issiz nesneleri
        statu_dict1={"Mavi yaka":3,"Beyaz yaka":5,"Yönetici":2}
        statu_dict2={"Mavi yaka":20,"Beyaz yaka":5,"Yönetici":2}
        statu_dict3={"Mavi yaka":1,"Beyaz yaka":2,"Yönetici":3}
        issiz1=İssiz("123456963","Şevval","Özdemir",20,"Kadın","Türk",statu_dict1)
        issiz2=İssiz("147852369","Elif","Özdemir",30,"Kadın","Türk",statu_dict2)
        issiz3=İssiz("123654789","Ahmet","Özdemir",35,"Erkek","Türk",statu_dict3)

        print("İşsiz nesneleri")
        print(issiz1)
        print(issiz2)
        print(issiz3)

        #CALİSAN NESNELERİ
        calisan1=calisan("123654789","Ahmet","Özdemir",35,"Erkek","Türk","Yazılım",5,1600)
        calisan2=calisan("123456963","Şevval","Özdemir",20,"Kadın","Türk","Donanım",3,1400)
        calisan3=calisan("147852369","Elif","Özdemir",30,"Kadın","Türk","Muhasebe",8,2600)
        print("Çalışan Nesneleri")
        print(calisan1)
        print(calisan2)
        print(calisan3)

        #MAVİ YAKA NESNELERİ
        maviyaka1=maviYaka("147852369", "Elif", "Özdemir",30,"Kadın","Türk","Muhasebe",5,26000, 0.5)
        print("Mavi Yaka Nesneleri")
        print(maviyaka1)
        maviyaka2=maviYaka("123456963","Şevval","Özdemir",20,"Kadın","Türk","Donanım",3,1400,0.2)
        print(maviyaka2)
        maviyaka3=maviYaka("123654789","Ahmet","Özdemir",35,"Erkek","Türk","Yazılım",4,20000,0.7)
        print(maviyaka3)

        #BEYAZ YAKA NESNELERİ
        beyazyaka1=beyazYaka("123654789","Ahmet","Özdemir",35,"Erkek","Türk","Yazılım",5,20000,200)
        print("Beyaz Yaka Nesneleri")
        print(beyazyaka1)
        beyazyaka2=beyazYaka("147852369","Elif","Özdemir",30,"Kadın","Türk","Muhasebe",3,10000,500)
        print(beyazyaka2)
        beyazyaka3=beyazYaka("123456963","Şevval","Özdemir",20,"Kadın","Türk","Donanım",6,26000,400)
        print(beyazyaka3)



        # DataFrame oluşturma
        data = pd.DataFrame({
                "Nesne Değeri": ["Çalışan", "Çalışan", "Çalışan"],
                "T.C. Kimlik No": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no()],
                "Ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad()],
                "Soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad()],
                "Yaş": [calisan1.get_yaş(), calisan2.get_yaş(), calisan3.get_yaş()],
                "Cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet()],
                "Uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk()],
                "Sektör": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor()],
                "Tecrübe": [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube()],
                "Maaş": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas()],
                "Yeni Maaş": [calisan1.zam_hakki(), calisan2.zam_hakki(), calisan3.zam_hakki()]
        })

        print(data)

        data.fillna(0, inplace=True)
        grouped = data.groupby("Nesne Değeri").agg({"Tecrübe": "mean", "Maaş": "mean"})


        print(grouped)
        maas_ustunde = data[data["Maaş"] > 15000]
        sayi = len(maas_ustunde)
        print("Maaşı 15000 TL üzerinde olanların toplam sayısı:", sayi)
        sorted_data = data.sort_values("Maaş")
        print(sorted_data)
        tecrube_ustunde = data[(data["Nesne Değeri"] == "Beyaz Yaka") & (data["Tecrübe"] > 3)]

        print(tecrube_ustunde)
        yuksek_maas = data[data["Maaş"] > 10000].iloc[2:5, [1, 10]]

        print(yuksek_maas)
        yeni_dataframe = data[["Ad", "Soyad", "Sektör", "Yeni Maaş"]]

        print(yeni_dataframe)



if __name__ == "__main__":
        main()










