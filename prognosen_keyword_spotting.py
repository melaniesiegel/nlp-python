import nlp_basics
from nlp_basics import *

testtext = open('adidas_JA_2012_Text.txt','r', encoding='utf-8')

prognosen_sentences = open('prognosen_sentences.txt','w', encoding='utf-8')

lines = testtext.readlines()

blob = TextBlobDE(str(lines))
sentences = blob.sentences

keywords = ("Umsatz", "Prognose", "erwarten","voraussichtlich","erwartet","rechnen","gerechnet")


for satz in sentences:
    if any(w in satz for w in keywords):
#        print(satz + '\n')
        prognosen_sentences.write(str(satz) + ' EOS\n')
        
testtext.close()
prognosen_sentences.close()
