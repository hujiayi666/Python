#演示面向对象封装思想中私有成员的使用

#定义一个类，内含私有成员变量和私有成员方法
class Phone:
    __current_voltage=0.5

    def __keep_sigle_core(self):
        print("让CPU以单核运行")
    def call_by_5g(self):
        if self.__current_voltage>=1:
            print("5G通话已开启")
        else:
            self.__keep_sigle_core()
            print("电量不足，保持单核模式")

phone=Phone()
phone.call_by_5g()






































