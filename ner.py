import nlp_basics
from nlp_basics import *
#import pos_tagging
#from pos_tagging import *

import re

#### Named-Entity Recognition ####

#sehr einfache Lösung
'''
print("NER")

ne_grammar = r"""
PERSON: { <NNP><NNP>}
PLACE: {<IN><NNP>}
ORGANIZATION: {<NN><NNP>}
"""

ne_parse = nltk.RegexpParser(ne_grammar)
ne_result = ne_parse.parse(postags)
print(ne_result)
'''



organizations = []
money_expressions = 'y'
products = []
org_divisions = []
markets = []


org_abbrevs = ["AG", "GmbH", "Konzern",["AG", "&", "Co", "KG"], 'OHG', 'Aktiengesellschaft', 'Corp', 'Corporation', "e.G.", 'eG', "e.G",'Holding', 'GbR', 'gGmbH', ["GmbH", "&", "Co", "KG"]]

money_abbrevs = ['€', 'EUR']

money_multipliers = ["Mrd.", "Mio.", "Tsd"]

product_prefixes = ["Marke", "Marken"]

gaz_organisations = ["adidas", "Adidas", "Reebok", "Reebok-CCM", "TaylorMade-adidas", "Rockport", "Konzerns"]

gaz_subdivisions = ["Golf", "Hockey"]

gaz_divisions = ["Segmenten", "eCommerce-Geschäft", "Einzelhandelssegment", "Großhandelssegment", "Sportartikelsektors", "Sporteinzelhandels"] 

division_prefixes = ["Segment"]

markets = ["China", "Schwellenländer", "Deutschland", "asiatischen", "Lateinamerikas", "Lateinamerika"]

def named_entities_org(blob):
    tags = blob.tags
    org_string = ''
    for word in tags:
        if word[0] in gaz_organisations:
            next_word = tags[tags.index(word) +1]
            if next_word[0] in ["EOS"]:
                org_string = word[0]
            else:
                nextnext_word = tags[tags.index(word) +2]
                if next_word[1] in ["NN", "NNP"] and nextnext_word[1] in ["NN", "NNP"]:
                    org_string = word[0] + ' ' + next_word[0] + ' ' + nextnext_word[0]
                else: org_string = word[0]
        elif word[0] in org_abbrevs:
            prev_word = tags[tags.index(word) -1]
            if prev_word[1] in ["NN", "NNP", "JJ"]:
                org_string = prev_word[0] + ' ' + word[0]
    return org_string


def named_entities_org_xml(txt,blob):
    tags = blob.tags
    for word in tags:
        if word[0] in gaz_organisations:
            print(word[0])
            txt.replace(word,'<ORG>word<\ORG>')
    print(txt)


    
## adidas Sport Performance
## eCommerce-Geschäft
                
def named_entities_org_division(blob):
    tags = blob.tags
    org_string = ''
    for word in tags:
        if word[0] in gaz_organisations:
            next_word = tags[tags.index(word) +1]
            nextnext_word = tags[tags.index(word) +2]
            if next_word[0] in gaz_subdivisions:
                org_string = word[0] + ' ' + next_word[0]
            elif next_word[1] in ["NN", "NNP"] and nextnext_word[1] in ["NN", "NNP"]:
                org_string = word[0] + ' ' + next_word[0] + ' ' + nextnext_word[0]
        elif word[0] in ["Segmenten"]:
            prev_word = tags[tags.index(word) -1]
            if prev_word[0] in ["allen"]:
                org_string = prev_word[0] + ' ' + word[0]
        elif word[0] in gaz_divisions:
                org_string = word[0]
        elif word[0] in division_prefixes:
            next_word = tags[tags.index(word) +1]
            if next_word[1] in ["NN", "NNP", "JJ"]:
                org_string = word[0] + ' ' + next_word[0]
    return org_string
        
                
def named_entities_product(blob):
    tags = blob.tags
    product_string = ''
    for word in tags:
        if word[0] in product_prefixes:
            next_word = tags[tags.index(word) +1]
            nextnext_word = tags[tags.index(word) +2]
            if nextnext_word[1] in ["CC"]:
                nextnextnext_word = tags[tags.index(word) +3]
                if nextnextnext_word[1] in ["NN", "NNP", "JJ"]:
                    products.append(nextnext_word[0] + next_word[0] + ' ' + word[0])
                    product_string = word[0] + ' ' + next_word[0] + ' ' + nextnext_word[0] + ' ' + nextnextnext_word[0]
#                    products_annotation = '<PRODUCT>' + nextnextnext_word + nextnext_word[0]  + next_word[0] + word[0] + '<\PRODUCT>'
            elif next_word[1] in ["NN", "NNP", "JJ"]:
                products.append(next_word[0] + ' ' + word[0])
                product_string = word[0] + ' ' + next_word[0]
                products_annotation = '<PRODUCT>' + next_word[0] + word[0] + '<\PRODUCT>'
    return product_string


def named_entities_money(blob):
    tags = blob.tags
    for word in tags:
        if word[0] in money_abbrevs:
            prev_word = tags[tags.index(word) -1]
            if prev_word[0] in money_multipliers:                
                prevprev_word = tags[tags.index(word) -2]
                money_expressions = prevprev_word[0]+ ' ' + prev_word[0] + ' ' + word[0]
            else:
                money_expressions = prev_word[0] + ' ' + word[0]
        elif word[0] in ["Bereich"]:
            prev_word = tags[tags.index(word) -1]
            prevprev_word = tags[tags.index(word) -2]
            money_expressions = prevprev_word[0]+ ' ' + prev_word[0] + ' ' + word[0]
    return money_expressions



def named_entities_market(blob):
    tags = blob.tags
    for word in tags:
        if word[0] in markets:
            market_expression = word[0]
        else:
            market_expression = ''
    return market_expression
    
def named_entities_all(txt):
    blob = TextBlobDE(txt)
    tags = blob.tags
    print (tags)
    for word in tags[1:-2]:
        next_word = tags[tags.index(word) +1]
        nextnext_word = tags[tags.index(word) +2]
        prev_word = tags[tags.index(word) -1]
        prevprev_word = tags[tags.index(word) -2]
        if word[0] in product_prefixes:
            if next_word[1] in ["NN", "NNP", "JJ"]:
                products.append(next_word[0] + ' ' + word[0])
                products_string = next_word[0] + ' ' + word[0]
                products_annotation = '<PRODUCT>' + next_word[0] + word[0] + '<\PRODUCT>'
        elif word[0] in gaz_organisations:
            if next_word[1] in ["NN", "NNP", "JJ"] and nextnext_word[1] in ["NN", "NNP", "JJ"]:
                print (next_word[1] + nextnext_word[1])
                org_divisions.append(word[0] + ' ' + next_word[0] + ' ' + nextnext_word[0])
                org_string = word[0] + ' ' + next_word[0] + ' ' + nextnext_word[0]
                org_annotation = '<ORG_DIV>' + word[0]+ ' ' + next_word[0]+ ' ' + nextnext_word[0] +'<\ORG_DIV>'
            else:
                organizations.append(word[0])
                org_string = word[0]
                org_annotation = '<ORG>' + word[0] + '<\ORG>'
        elif word[0] in org_abbrevs:
            if prev_word[1] in ["NN", "NNP", "JJ"]:
                organizations.append(prev_word[0] + ' ' + word[0])
                org_string = prev_word[0] + ' ' + word[0]
                org_annotation = '<ORG_ABB>' + org_string + '<\ORG_ABB>'
        elif word[0] in money_abbrevs:
            if prev_word[0] in money_multipliers:                
                money_expressions.append(prevprev_word[0]+ ' ' + prev_word[0] + ' ' + word[0])
                money_string = prevprev_word[0]+ ' ' + prev_word[0] + ' ' + word[0]
                money_annotation = '<MONEY>' + money_string + '<\MONEY>'
            else:
                money_expressions.append(prev_word[0] + ' ' + word[0])
                money_annotation = '<MONEY>' + money_string + '<\MONEY>'
    print ("ORGANIZATION: ")
    print (organizations)
    print ("ORGANIZATION DIVISIONS")
    print (org_divisions)
    print ("PRODUCT_NAMES: ")
    print (products)
    print("MONEY: ")
    print(money_expressions)
    money_annotated_txt = txt.replace(money_string,money_annotation)
    org_annotated_txt = txt.replace(org_string,org_annotation)
    print ("ANNOTATED TEXT: ")
    annotated_text = txt.replace(money_string,money_annotation).replace(org_string,org_annotation).replace(products_string,products_annotation)
    print(annotated_text)    

text_nertest = '''Für die meisten anderen wichtigen asiatischen Schwellenländer wird für 2013 von einem rasanten Wachstum der Branche ausgegangen, da eine steigende Inlandsnachfrage sowie höhere Löhne den Umsatz mit nicht essenziellen Konsumartikeln weiter fördern werden. EOS'''
small_nertest = '''Des Weiteren werden Verbesserungen im Einzelhandelssegment sowie bei der Marke Reebok die Entwicklung der Bruttomarge fördern.'''

myblob = blob = TextBlobDE(text_nertest)
tags = blob.tags
#print (tags)
#print(named_entities_market(myblob))


