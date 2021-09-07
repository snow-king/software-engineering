class validation(object):
    input_str = ""

    def __init__(self, base):
        self.base_str = base

    # compare password
    def compare(self):
        if self.input_str == self.base_str:
            print("Yup, you are right (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
            return False
        else:
            print("Sorry, it's not your password (｡╯︵╰｡)")
            return True

    def set_base(self):
        print("please input new base password:")
        self.base_str = input()

    # this method launches magic
    def run(self):
        print("Please, input your password \n *type \"exit\" if you want to exit \n")
        self.input_str = input()
        if self.input_str == "exit":
            print("Goodbye , Samurai (っ˘̩╭╮˘̩)っ")
        else:
            if self.compare():
                self.run()

