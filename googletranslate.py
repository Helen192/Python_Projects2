#import googletrans
from googletrans import Translator
#print(googletrans.LANGUAGES) # print out the languages which are supported by google
t = Translator() # create an object of class Translator
translation = t.translate("trời hôm nay đẹp quá", src='vi', dest='de')
print(translation.text)

