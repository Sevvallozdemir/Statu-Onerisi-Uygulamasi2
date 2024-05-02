from insan import insan

class İssiz(insan):
    def __init__(self,tc_no,ad,soyad,yaş,cinsiyet,uyruk,statu_dict={}):
        super().__init__(tc_no, ad, soyad, yaş, cinsiyet, uyruk)
        self.__statu_dict=statu_dict


    def set_statu_dict(self,statu_dict):
        self.__statu_dict=statu_dict
    def get_statu_dict(self):
        return self.__statu_dict



    def statu_bul(self):
        max_puan=0
        max_statu=""
        for statu, yil in self.__statu_dict.items():
            puan=0
            if statu.lower() == "mavi yaka":
                puan=yil*0.2
            elif statu.lower() == "beyaz yaka":
                puan=yil*0.35
            elif statu.lower() == "yönetici":
                puan=yil*0.45
            if puan > max_puan:
                max_puan = puan
                max_statu = statu
        return max_statu

    def __str__(self):
        return """"
        Ad:{}
        Soyad:{}
        Statü:{}
        """.format(self.get_ad(),self.get_soyad(),self.statu_bul())

