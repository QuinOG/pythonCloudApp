from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    frenchText = MyMemoryTranslator(source='english', target='french').translate(englishText)
    print(frenchText)
    return(frenchText)

def frenchToEnglish(frenchText):
    englishText = MyMemoryTranslator(source='french', target='english').translate(frenchText)
    print(englishText)
    return(englishText)