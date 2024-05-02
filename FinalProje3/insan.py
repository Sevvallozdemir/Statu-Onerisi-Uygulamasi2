class insan():
    def __init__(self,tc_no,ad,soyad,yaş,cinsiyet,uyruk):
        self.__tc_no=tc_no
        self.__ad=ad
        self.__soyad=soyad
        self.__yaş=yaş
        self.__cinsiyet=cinsiyet
        self.__uyruk=uyruk

    def get_tc_no(self):
        return self.__tc_no
    def set_tc_no(self, tc_no):
        self.__tc_no = tc_no
    def get_ad(self):
        return self.__ad
    def set_ad(self, ad):
        self.__ad = ad
    def get_soyad(self):
        return self.__soyad
    def set_soyad(self, soyad):
        self.__soyad = soyad
    def get_yaş(self):
        return self.__yaş
    def set_yaş(self, yaş):
        self.__yaş = yaş
    def get_cinsiyet(self):
        return self.__cinsiyet
    def set_cinsiyet(self, cinsiyet):
        self.__cinsiyet = cinsiyet
    def get_uyruk(self):
        return self.__uyruk
    def set_uyruk(self, uyruk):
        self.__uyruk = uyruk

    def __str__(self):
        return """
        Tc:{}
        Ad:{}
        Soyad:{}
        Yaş:{}
        Cinsiyet:{}
        Uyruk:{}
        """.format(self.__tc_no,self.__ad,self.__soyad,self.__yaş,self.__cinsiyet,self.__uyruk)