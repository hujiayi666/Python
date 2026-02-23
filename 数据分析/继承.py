class Phone:
    ID=200538
    producer="胡家毅"
    def call_by_4g(self):
        print("4g通话")
class Phone2022(Phone):
    face_ID=1111
    def call_by_5g(self):
        print("2022最新5g通话")
phone=Phone2022()
phone.call_by_5g()
phone.call_by_4g()
















