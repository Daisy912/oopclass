# @name: Daisy StudentId: 202110701580008
# @Date: 2022-10-30 22:57
class Computer:

    def __init__(self, company):
        self.__company = company

    def __private_say_company(self):
        print(f"The company is {self.__company}")

    def public_say_company(self):
        self.__private_say_company()


class Phone:

    def __init__(self, phone_number):
        self.__phone_number = phone_number

    def get_phone_number(self):
        return self.__phone_number


class Smartphone(Computer, Phone):
    def __init__(self, public_say_company, get_phone_number, name):
        Computer.__init__(self, public_say_company)
        Phone.__init__(self, get_phone_number)
        self.__name = name

    def get_name(self):
        return self.__name


sp1 = Smartphone("Apple", 1525791834, "iPhone X")
sp1.public_say_company()
print(sp1.get_phone_number())
print(sp1.get_name())
