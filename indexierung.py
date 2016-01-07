import nlp_basics
from nlp_basics import *
#import pos_tagging
#from pos_tagging import *
#import tokenizer
#from tokenizer import *
from collections import Counter
import ner
from ner import *

#### Automatische Indexierung ####

terms = []
counted_terms = []
highfreqlist = []
terms_reduced = []
lemmatized_terms = []

#### zunächst Nomen extrahieren ####

def extract_nouns(txt,terms,blob):
    pos = blob.tags
    for item in pos:
        if item[1].startswith('N'):
            terms.append(item[0])

            
#### Stoppwörter rauswerfen ####

stoppwortliste = ('–',"%",'•','€',"Mio.",'SIEHE','Tsd','Jahr', "Mrd.")

def delete_stopwords(terms, terms_reduced):
    for term in terms:
        if term[0] not in stoppwortliste:
            terms_reduced.append(term)

#### Grundformen ####

## noch mal rausgenommen, weil der Lemmatizer zu schlecht ist

_lemmatizer = PatternParserLemmatizer()

def lemmata(terms):
    for word in terms:
        lemma = _lemmatizer.lemmatize(word)



    

#### Frequenzen ####

counted_terms = Counter(terms).most_common()

#### Nur die Nomen mit häufigem Auftreten ####

def high_freq(termlist,highfreqlist):
    for term in termlist:
##        if term[1] > 90:
        if term[1] > 1:
            highfreqlist.append(term)

#### Named Entities ####

def build_ner_list(txt,blob):
    named_entities_org(txt,blob)


#### Indexierung  ####

def index(txt):
    blob = TextBlobDE(txt)
    extract_nouns(txt,terms,blob)
    counted_terms = Counter(terms).most_common()
    high_freq(counted_terms,highfreqlist)
    delete_stopwords(highfreqlist,terms_reduced)
    print ("HIGH FREQUENT NOUNS: ")
    print(terms_reduced)
    build_ner_list(txt,blob)
    counted_names = Counter(organizations).most_common()
    print("ORGANIZATION NAMES: ")
    print(counted_names)


text_indextest = '''Im September 2012 bestätigte das Management seine Route 2015 Ziele
                              für den  adidas Konzern. Zudem gab das Management angesichts der erzielten
                              Ergebnisse in den ersten zwei Jahren des Plans aktualisierte Ziele
                              nach Segmenten und nach Marken bekannt. Für die Marke adidas wurde
                              das Ziel bis 2015 um 600 Mio. € auf 12,8 Mrd. € angehoben. Für adidas 
                              Sport Performance wird nun voraussichtlich ein Umsatz in Höhe von
                              8,9 Mrd. € erreicht werden (bisherige Prognose: 8,5 Mrd. €). Diese
                              höhere Erwartung gründet auf Rekordumsätzen in der Kategorie Fußball
                              und der Dynamik bei Running und Basketball.
                              er Aufsichtsrat der adidas AG hat sich verpflichtet,
                              den Anteil seiner Mitglieder ab der Neuwahl 2014 auf mindestens drei
                              Frauen, davon mindestens eine auf Seite der Anteilseigner, zu erhöhen / SIEHE CORPORATE
                              GOVERNANCE BERICHT MIT ERKLÄRUNG ZUR UNTERNEHMENSFÜHRUNG. Der adidas Konzern wurde
                              im Jahr 2012 zudem ein aktives Mitglied
                              der „Charta der Vielfalt“, um unser Wissen um Best Practices hinsichtlich
                              der Berücksichtigung von Diversity-Aspekten im Arbeitsumfeld mit anderen
                              Unternehmen zu teilen. 
                              '''
index(text_indextest)         

    
