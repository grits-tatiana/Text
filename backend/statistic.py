from text import *

def getStatistic(payload):
    text = Text(payload)
    lenWithTrim = text.getLenWithTrim(payload)
    lenWithoutTrim = text.getLenWithoutTrim(payload)
    countWord = text.getCountWord(payload)
    return {
        "lenWithTrim": lenWithTrim,
        "lenWithoutTrim": lenWithoutTrim,
        "countWord": countWord
    }
