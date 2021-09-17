class Calculate(object):

    @staticmethod
    def difference(a, b):
        try:
            a, b = int(a), int(b)
            return a - b
        except ValueError:
            print("input string contains letters or is empty ")
