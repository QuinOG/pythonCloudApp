from deep_translator import MyMemoryTranslator
from typing import Union, List

def englishToFrench(englishText) -> Union[str, List[str]]:
    frenchText = MyMemoryTranslator(source='english', target='french').translate(englishText)
    print(frenchText)
    return(frenchText)

def frenchToEnglish(frenchText):
    englishText = MyMemoryTranslator(source='french', target='english').translate(frenchText)
    print(englishText)
    return(englishText)