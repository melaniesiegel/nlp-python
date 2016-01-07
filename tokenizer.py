import nlp_basics
from nlp_basics import *


text = '''Sehr geehrte Damen und Herren, das Familienunternehmen Haniel
hat im vergangenen Jahr wichtige Veränderungen angestoßen. Dabei hat der
Aufsichtsrat den Vorstand in vier ordentlichen und sechs außerordentlichen
Sitzungen beraten. Im Einzelnen ging es zum Beispiel um den Verkauf von Movianto
, Pharmexx und der Versandapotheke DocMorris durch Celesio oder die Uebernahme
von Ratioform, einem Anbieter fuer Verpackungslösungen, durch TAKKT. Darüber
hinaus hat der Aufsichtsrat in einer außerordentlichen Sitzung am 26. November
2012 ein umfangreiches Maßnahmenpaket zur Schuldenreduktion der Holding
genehmigt, das unter anderem die Verringerung der Celesio-Beteiligung auf
50,01 Prozent beinhaltet und zudem vorsieht, die Beteiligung an der Metro AG
um 4,23 Prozentpunkte zu reduzieren, ohne damit die strategische Bedeutung
beider Beteiligungen zu mindern.'''

#### Tokenizer ####

#erst mit Textblob

##print("SENTENCE TOKENIZER (TextBlobDE)")

sentences = blob.sentences
##print (sentences)

##print("WORD TOKENIZER (TextBlobDE)")

tokens = blob.tokens
##print(tokens)

#dann mit NLTK

##print ("SENTENCE TOKENIZER (NLTK)")
sent_detector = nltk.data.load('tokenizers/punkt/german.pickle')
##print ('\n--\n'.join(sent_detector.tokenize(text.strip())))

##print("WORD TOKENIZER (NLTK)")
tokens = word_tokenize (text)
##print (tokens)
