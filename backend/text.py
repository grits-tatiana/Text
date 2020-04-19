class Text:

    def __init__(self, text):
    	self.text = text

    def getLenWithTrim(self, text):
        return len(self.text)

    def getLenWithoutTrim(self, text):
        return len(self.text.replace(' ', ''))

    def getCountWord(self, text):
        return (self.text.count(' ') + 1)