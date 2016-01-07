import nlp_basics
from nlp_basics import *
import pos_tagging
from pos_tagging import *
import tokenizer
from tokenizer import *

#### Termextraktion: Alle Nomen und Namen im Adidas-Bericht ####

#erst mache ich eine Terminologie-Liste auf

terms = []


#dann extrahiere ich alle Wörter mit einem POS-Tag, der mit "N" anfängt

def termex(txt):
    myblob = TextBlobDE(txt)
    pos = myblob.tags
    for item in pos:
        if item[1].startswith('N'):
            terms.append(item)
    
print("TERMEXTRACTION:")

termex(text_long)


#die Liste mit Tuples wird auch noch sortiert (unabhängig von Groß- und Kleinschreibung
#und dann Duplikate rausgeworfen

sorted_terms = sorted(set(terms), key=lambda terms:(terms[0].lower()))

##print(sorted_terms)

#jetzt eine Stoppwortliste

stoppwortliste = ('03erfolgte','1a','%','\$\/€',"%-igen","\'",'*','+',"\'%3E%3C\/script%3E","\'\/ebanzwww\/","\'\/ebanzwww\/contentloader", "\'\/ebanzwww\/wexsservlet", "\'Hair", "\'https", "\'ISIN", "\'s", "\'session\.sessionid=0c20b7b2f963372e84459686a04d3c05", "\'text\/javascript", "\+", "\/\/publikations-plattform.de\/sp\/wexsservlet", "\/\/www\.bundesanzeiger\.de\/", "\/css", "\images", "\=", "\[", "\]")

# Terme in der Stoppwortliste werden rausgeworfen

for term in sorted_terms:
    if term[0] in stoppwortliste:
        sorted_terms.remove(term)

##print(sorted_terms)

#jetzt schreibe ich das Ganze in eine Datei

terms_adidas = open('terms_adidas','w', encoding='utf-8')
for term in sorted_terms:
    terms_adidas.write(term[0])
    terms_adidas.write(':\tPOS: ')
    terms_adidas.write(term[1])
    terms_adidas.write('\n')
    

### was man aufmacht, muss man auch wieder zumachen ####
    
terms_adidas.close()
