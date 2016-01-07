######## BASICS #######

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


text = "Auch für 2013 und 2014 z.B. gehen wir wieder von einem hohen Free Cash Flow aus. Die Mehrheit der Mittelabflüsse im Zuge des Effizienzsteigerungsprogramms werden 2013 zahlbar und dürften gegenüber 2012 zusätzliche Zahlungsmittelabflüsse von ca. 300 Mio EUR mit sich bringen."
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
#adidas_file = open('adidas_JA_2012.htm','r', encoding='utf-8')

#allianz_file = open('allianz_JA_2012.htm','r', encoding='utf-8')

#allianz_data = allianz_file.read()

#allianz_text = open('allianz_JA_2012_Text.txt','w', encoding='utf-8')
#Axel_Springer_JA_2012
#todo_file = open('Vulcanic_Triatherm_JA_2012.htm','r', encoding='utf-8')

#todo_data = todo_file.read()

#todo_text = open('Vulcanic_Triatherm_JA_2012_Text.txt','w', encoding='utf-8')

#### HTML-Parser ####

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        todo_text.write(data)
        

parser = MyHTMLParser()

##Das musste ich nur einmal machen:
#parser.feed(todo_data)

#text_long = adidas_text.read()

#### Textblob initialisieren ####
blob = TextBlobDE(text)

### was man aufmacht, muss man auch wieder zumachen ####
    
#todo_file.close()
#todo_text.close()
