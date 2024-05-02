from calisan import calisan

class maviYaka(calisan):
    def __init__(self,tc_no, ad, soyad, yaş, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no,ad,soyad,yaş,cinsiyet,uyruk,sektor,tecrube,maas)
        self.__yipranma_payi=int(yipranma_payi)


    def get_yipranma_payi(self):
        return self.__yipranma_payi
    def set_yipranma_payi(self,yipranma_payi):
        self.__yipranma_payi=yipranma_payi

    try:
        def zam_hakki(self):
            if self.get_tecrube()<=2:
                return self.__yipranma_payi*10
            elif 2<self.get_tecrube()<=4 and self.get_maas()<15000:
                return (self.get_maas()%self.get_tecrube())/2 + (self.__yipranma_payi*10)
            elif self.get_tecrube()>4 and self.get_maas()<25000:
                return (self.get_maas()%self.get_tecrube())/3+ (self.__yipranma_payi*10)
            else:
                return self.get_maas()
    except Exception as e:
        print("Hata:",e)

    def __str__(self):
        return """
        Ad:{}
        Soyad:{}
        Tecrübe:{}
        Yeni maaş:{}
        """.format(self.get_ad(),self.get_soyad(),self.get_tecrube(),self.zam_hakki())
