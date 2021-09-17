import re


class search(object):
    testStr = ''

    def getStr(self, el):
        self.testStr = str(el)

    def seek_something(self):
        match = re.findall(r'[a]{2}|[0]{2}', self.testStr)
        if match:
            answer = "Yes"
        else:
            answer = "No"
        return answer
