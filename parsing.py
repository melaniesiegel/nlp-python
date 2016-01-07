import nlp_basics
from nlp_basics import *
import pos_tagging
from pos_tagging import *
import tokenizer
from tokenizer import *



#### Parsing ####


# mit Textblob

def textblob_parser(txt):
    print("Textblob Parser")
    parse_blob = TextBlobDE(txt)
    print(parse_blob.parse())


##textblob_parser("Anna kauft ein gutes Buch über Hunde")

# Lösung aus dem NLTK-Buch 
'''
print ("CONTEXT-FREE GRAMMAR, NLTK-Book")

## Hier muss man das Lexikon selbst schreiben.
## Andreas Schieberle hat eine Lösung entwickelt, bei der die POS aus dem Treetagger benutzt werden.

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

print ("PARSING NACH ANDREAS SCHIEBERLE, UNTER VERWENDUNG DER POS-TAGS")

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
ch_parser = nltk.ChartParser(cfg_grammar)

def nltk_parser(txt):
    parse_blob = TextBlobDE(txt)
    print (parse_blob.tags)
    sent = [x[1] for x in parse_blob.tags]
    sent_text = [x[0] for x in parse_blob.tags]
    for tree in ch_parser.parse(sent):
        print(tree)
        tree.draw()

nltk_parser("Anna kauft ein Buch.")



#### Dependenzgrammatik ####
'''
# sehr einfache Lösung mit dem NLTK-Buch

print("DEPENDENZPARSER NACH NLTK-BUCH")

text_dep = "Die Frau sah den Mann mit dem Fernrohr"
blob_dep = TextBlobDE(text_dep)
tokens_dep = blob_dep.tokens

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
trees = dep_parser.parse(tokens_dep)
for tree in trees:
    print (tree)
    tree.draw()
'''
