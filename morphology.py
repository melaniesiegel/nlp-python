import nlp_basics
from nlp_basics import *


#### Morphologie ####

#Grundformen

print("LEMMATIZATION AND POS TAGS - TEXTBLOB")

_lemmatizer = PatternParserLemmatizer()

lemmata = _lemmatizer.lemmatize(text)
print(lemmata)

#Generierung

print("MORPHOLOGY GENERATION - TEXTBLOB")

print(pd.attributive(u"gut", gender=pd.FEMALE, role=pd.INDIRECT, article="die"))

# Lange Wörter


print("LONG WORDS IN ADIDAS TEXT")
adidas_tokens = word_tokenize (text_long)
longwordslist = []
longwordslist.append([w for w in adidas_tokens if len(w) > 15])
longwords_adidas = open('longwords_adidas','w')
for item in longwordslist:
  longwords_adidas.write("%s\n" % item)


longwords_adidas.close()

    
