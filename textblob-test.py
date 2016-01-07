

import nltk
from textblob_de import TextBlobDE
from textblob_de.lemmatizers import PatternParserLemmatizer
from textblob_de.packages import pattern_de as pd
from textblob_de import PatternParser
from nltk.tokenize import word_tokenize
import nltk.data
import re
import html.parser
from html.parser import HTMLParser


#####Ein paar Texte zum Probieren####

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
##text = "Auch für 2013 und 2014 z.B. gehen wir wieder von einem hohen Free Cash Flow aus. Die Mehrheit der Mittelabflüsse im Zuge des Effizienzsteigerungsprogramms werden 2013 zahlbar und dürften gegenüber 2012 zusätzliche Zahlungsmittelabflüsse von ca. 300 Mio EUR mit sich bringen."
##text = "In Schottland fiel das Ergebnis deutlicher aus."
##text = "Frau Anna Meier spielt Tennis."
##text = "Den Mann biss der Hund."
##text = "Ich liebe dieses Handy, aber der Akku ist einfach Mist."
##text = "Das Buch ist nicht spannend"
##text = "Die Frau sah den Mann mit dem Fernrohr"
##text = "Die Frau sah den Mann auf dem Buch"
##text = "Der Mann biss den Hund"
##text = "Den Mann biss der Hund"
##text = "Ich liebe dieses Handy aber der Akku ist Mist"
##text = "auf dem Buch"
###text = "Die ABC AG hat einen Preis ausgeschrieben"

##Jetzt lesen wir mal den ersten Geschäftsbericht ein.
adidas_file = open('adidas_JA_2012.htm','r')

adidas_data = adidas_file.read()

adidas_text = open('adidas_JA_2012_Text.txt','r')

##Jetzt versuchen wir, das HTML zu parsen

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        adidas_text.write(data)
        

parser = MyHTMLParser()

##Das musste ich nur einmal machen:
##parser.feed(adidas_data)

text_long = adidas_text.read()


#### Regular Expressions ####

#alle Wörter, die mit "heit" enden
heitwords = re.findall(r"\w+heit",text_long)

##print ("HEIT:", heitwords)
    
#### Tokenizer ####

#erst mit Textblob

blob = TextBlobDE(text)

print("SENTENCE TOKENIZER (TextBlobDE)")

sentences = blob.sentences
print (sentences)

print("WORD TOKENIZER (TextBlobDE)")

tokens = blob.tokens
print(tokens)

#dann mit NLTK

print ("SENTENCE TOKENIZER (NLTK)")
sent_detector = nltk.data.load('tokenizers/punkt/german.pickle')
print ('\n--\n'.join(sent_detector.tokenize(text.strip())))

print("WORD TOKENIZER (NLTK)")
tokens = word_tokenize (text)
print (tokens)

#### POS Tagging ####

print("POS TAGS")

postags = blob.tags
print(postags)

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

'''
print("LONG WORDS IN ADIDAS TEXT")
adidas_tokens = word_tokenize (text_long)
longwordslist = []
longwordslist.append([w for w in adidas_tokens if len(w) > 15])
longwords_adidas = open('longwords_adidas','w')
for item in longwordslist:
  longwords_adidas.write("%s\n" % item)


longwords_adidas.close()

'''    

#### Nominalphrasen ####

# mit Textblob

##print(blob.noun_phrases)

# mit eigener Chunk-Grammatikt

print("CHUNKING")
chunk_grammar = r"""
NP: {<DT>?<CD>?<JJ>*<NN>+<NNP>*}
    {<PRP>}
    {<CD><CC><CD>}
PP: {<IN><NP>+}
"""
chunk_parse = nltk.RegexpParser(chunk_grammar)
chunk_result = chunk_parse.parse(postags)
print(chunk_result)

#### Named-Entity Recognition ####

#sehr einfache Lösung

print("NER")

ne_grammar = r"""
PERSON: { <NNP><NNP>}
PLACE: {<IN><NNP>}
ORGANIZATION: {<NN><NNP>}
"""

ne_parse = nltk.RegexpParser(ne_grammar)
ne_result = ne_parse.parse(postags)
print(ne_result)

## Lösung für NER von Andreas Schieberle

print("NER - Schieberle")

result = []
for i, word in enumerate(blob.tags):
    position = i
    if word[0].find("AG") > -1 or word[0].find("GmbH") > -1:
        named_entity = word[0]
        prev_words = blob.tags[:position]
        prev_words.reverse()
        for k in prev_words:
            if k[1] in ["NN", "NNP", "JJ"]:
                named_entity = k[0] + " " + named_entity
            else:
                result.append(named_entity)
                break
print("ORGANIZATION")
print (result)


##sent = nltk.corpus.treebank.tagged_sents()[22]
##print nltk.ne_chunk(sent)

##print blob.sentiment

##sent = text.split()




#### Sentiment Analysis ####

# mit Textblob
print("Sentiment")

print(blob.sentiment)

#### Parsing ####

# mit Textblob
print("Textblob Parser")

print(blob.parse())

# Lösung aus dem NLTK-Buch 
print ("CONTEXT-FREE GRAMMAR")
'''
## Hier muss man das Lexikon selbst schreiben.
Andreas Schieberle hat eine Lösung entwickelt, bei der die POS aus dem Treetagger benutzt werden.

cfg_grammar = nltk.CFG.fromstring("""
  S -> NP VP
  NP -> DT N | DT N PP | PRP | N
  VP -> V NP | V NP PP | V ADJP
  ADJP -> RB JJ | JJ
  PP -> P NP
  N -> "Frau" | "Mann" | "Fernrohr" | "Buch" | "Hund" | "Akku" |"Handy" | "Mist"
  P -> "mit" | "auf"
  V -> "sah" | "biss" | "liebe" | "ist"
  DT -> "Die" | "den" | "Den" | "dem" | "Der" | "der" | "dieses" | "Das" | "das"
  PRP -> "Ich"
  CC -> "aber"
  RB -> "nicht"
  JJ -> "spannend"
  PUNCT -> '.' | '!'
  """)

rd_parser = nltk.RecursiveDescentParser(cfg_grammar)
sr_parser = nltk.ShiftReduceParser(cfg_grammar)
ch_parser = nltk.ChartParser(cfg_grammar)

for tree in rd_parser.parse(tokens):
    print (tree)
    tree.draw() 
'''

# von Andreas Schieberle: Verwendung der POS-Tags

def nltk_parser(txt):
    myblob = TextBlobDE(txt)
    sent = [x[1] for x in myblob.tags]
    sent_text = [x[0] for x in myblob.tags]
    cfg_grammar = nltk.CFG.fromstring("""
    S -> NP VP | S CC S
    NP -> 'DT' N | 'DT' N PP | 'PRP' | N | 'PRP$'
    VP -> V NP | V NP PP | V ADJP
    ADJP -> 'RB' 'JJ' | 'JJ'
    PP -> P NP
    N -> 'NN' | 'NNP' | 'NNS' | 'FW'
    V -> 'VBN' | 'VB' | 'MD'
    P -> 'IN' | 'TO'
    CC -> 'CC'
    O -> 'RP' | 'WDT' | 'TRUNC' | 'CD'
    """)
    
    parser = nltk.parse.ChartParser(cfg_grammar)
    for tree in parser.parse(sent):
        print(tree)
        tree.draw()

nltk_parser(text)



#### Dependenzgrammatik ####

# sehr einfache Lösung mit dem NLTK-Buch

dep_grammar = nltk.DependencyGrammar.fromstring("""
   'sah' -> 'Frau' | 'Mann' | 'mit' |'auf'
   'Frau' -> 'Die'
   'Mann' -> 'den'
   'mit' -> 'Fernrohr'
   'Fernrohr' -> 'dem'
   'auf' -> 'Buch'
   'Buch' -> 'dem'
   """)

dep_parser = nltk.ProjectiveDependencyParser(dep_grammar)
trees = dep_parser.parse(tokens)
##for tree in trees:
##    print (tree)
##    tree.draw()


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

#jetzt eine Stoppwortliste

stoppwortliste = ('03erfolgte','1a','%','$/€','%-igen',"'","'",'*','+')

# Terme in der Stoppwortliste werden rausgeworfen

for term in sorted_terms:
    if term[0] in stoppwortliste:
        sorted_terms.remove(term)

#jetzt schreibe ich das Ganze in eine Datei

terms_adidas = open('terms_adidas','w')
for term in sorted_terms:
    terms_adidas.write(term[0])
    terms_adidas.write(':\tPOS: ')
    terms_adidas.write(term[1])
    terms_adidas.write('\n')
    

### was man aufmacht, muss man auch wieder zumachen ####
    
terms_adidas.close()
adidas_file.close()
adidas_text.close()

