from calisan import calisan

class beyazYaka(calisan):
    def __init__(self,tc_no,ad,soyad,yaş,cinsiyet,uyruk,sektor,tecrube,maas,tesvik_primi):
        super().__init__(tc_no, ad, soyad, yaş, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi=tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi
    def set_tesvik_primi(self,tesvik_primi):
        self.__tesvik_primi=tesvik_primi,

    try:
        def zam_hakki(self):
            if self.get_tecrube()<=2:
                return self.get_tesvik_primi()
            elif 2<self.get_tecrube()<=4 and self.get_maas()<15000:
                return (self.get_maas()%self.get_tecrube())*5 + self.get_tesvik_primi()
            elif self.get_tecrube()>4 and self.get_maas()<25000:
                return (self.get_maas()%self.get_tecrube())*4 + self.get_tesvik_primi()
            else:
                return self.get_maas()
    except Exception as e:
        print("Hata:",e)

    try:
        def __str__(self):
            return """
            Ad:{}
            Soyad:{}
            Tecrübe:{}
            Yeni maaş:{}
            """.format(self.get_ad(),self.get_soyad(),self.get_tecrube(),self.get_maas()+self.zam_hakki())
    except Exception as e:
        print("Hata",e)
