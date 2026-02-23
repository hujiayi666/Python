class Phone:
    ID=None
    producer=None

    def call_by_5g(self):
        print("5g通话")

class NFCreader:
    nfc_type="第五代"
    producer="胡家毅"

    def read_card(self):
        print("读取NFC卡")

    def writ_card(self):
        print("写入NFC卡")

class remotecontrol:
    rc_type="红外遥控"
    def control(self):
        print("红外遥控开启")

class MyPhone(Phone,NFCreader,remotecontrol):
    pass
myphone=MyPhone()
myphone.control()















