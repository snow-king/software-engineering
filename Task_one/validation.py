import hashlib
import uuid


class validation(object):
    input_password = ""

    def __init__(self, base):
        self.base_password = self.hash_password(base)

    @staticmethod
    def hash_password(password):
        # uuid используется для генерации случайного числа
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    def check_password(self):
        password, salt = self.base_password.split(':')
        return password == hashlib.sha256(salt.encode() + self.input_password.encode()).hexdigest()

    # compare password
    def compare(self):
        if self.check_password():
            print("Yup, you are right (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
            return False
        else:
            print("Sorry, it's not your password (｡╯︵╰｡)")
            return True

    def setBase(self):
        print("please input new base password:")
        self.base_password = input()

    # this method launches magic
    def setInput(self, el):
        # print("Please, input your password \n *type \"exit\" if you want to exit \n")
        # self.input_password = input()
        self.input_password = el
        if self.input_password == "exit":
            print("Goodbye , Samurai (っ˘̩╭╮˘̩)っ")
        else:
            return self.compare()

