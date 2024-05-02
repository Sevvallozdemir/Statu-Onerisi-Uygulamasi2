from insan import insan

class calisan(insan):
    def __init__(self,tc_no,ad,soyad,yaş,cinsiyet,uyruk,sektor,tecrube,maas):
        super().__init__(tc_no, ad, soyad, yaş, cinsiyet, uyruk)
        self.__tecrube=int(tecrube)
        self.__sektor=sektor
        self.__maas=maas

    def set_sektor(self, sektor):
        self.__sektor = sektor
    def get_sektor(self):
        return self.__sektor
    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube
    def get_tecrube(self):
        return self.__tecrube
    def set_maas(self, maas):
        self.__maas = maas
    def get_maas(self):
        return self.__maas

    try:

        def zam_hakki(self):
            if self.__tecrube<=2:
                return 0
            elif 2<self.__tecrube<=4 and self.__maas<15000:
                return self.__maas+(self.__maas*self.__tecrube)/100
            elif self.__tecrube>4 and self.__maas<25000:
                return self.__maas+(self.__maas*self.__tecrube)/200
            else:
                return self.__maas
    except Exception as e:
        print("Hata:",e)

    def __str__(self):
        return """
        Ad:{}
        Soyad:{}
        Tecrübe:{}
        Yeni maaş:{}
        """.format(self.get_ad(),self.get_soyad(),self.__tecrube,self.zam_hakki())