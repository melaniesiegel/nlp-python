import nlp_basics
from nlp_basics import *
from keyword_cluster import *


#textin = open('adidas_JA_2012_Text_lemmatized.txt', 'r',encoding='utf-8')

out = open('out.txt','w',encoding='utf-8')

inputfile = input('Welche Datei soll analysiert werden? ')

textin = open(inputfile, 'r',encoding='utf-8')

lines = textin.readlines()

'''Sätze im Text zählen.
Eigentlich: Zeilen zählen, weil mit der Textvorbereitung schon ein Satz
pro Zeile steht.
'''

def count_sents(lines):
    number_of_sentences = 0    
    for line in lines:
        number_of_sentences = number_of_sentences + 1
    return(number_of_sentences)

#Wörter im Text zählen

def count_words(lines):
    number_of_words = 0
    for line in lines:
        blob  = TextBlobDE(line)
        words = blob.words
        for word in words:
            number_of_words = number_of_words + 1
    return(number_of_words)


#Wörter aus dem Themenbereich PV zählen. Auskommentiert: PV-Wörter im Text listen.

def count_pv_words(lines):
    number_of_pv_words = 0
    pv_words = []
    for line in lines:
        blob  = TextBlobDE(line)
        words = blob.words
        for word in words:
            if word in public_value:
                number_of_pv_words = number_of_pv_words + 1
                pv_words.append(word)
#    return(pv_words, number_of_pv_words)
    pv_words = sorted(set(pv_words))
    print('PV-Wörter: ' + str(pv_words))
    return(number_of_pv_words)


#Zahl der Sätze mit Wörtern aus dem Themenbereich PV (allgemein)

def count_pv_sents(lines):
    pv_sents = 0
    sent_pv_status = 0
    for line in lines:
        blob  = TextBlobDE(line)
        words = blob.words
        if(len(set(words).intersection(public_value)) > 0):
            sent_pv_status = 1
        else:
            sent_pv_status = 0
        pv_sents = pv_sents + sent_pv_status
    return(pv_sents)

#Wörter aus dem Themenbereich Gesellschaft zählen.

def count_gesellschaft_words(lines):
    number_of_gesellschaft_words = 0
    for line in lines:
        blob  = TextBlobDE(line)
        words = blob.words
        for word in words:
            if word in gesellschaft:
                number_of_gesellschaft_words = number_of_gesellschaft_words + 1
                out.write('WORT_GESELLSCHAFT: ' + word + '\t' + line)
    return(number_of_gesellschaft_words)




#Zahl der Sätze mit Wörtern aus dem Themenbereich Gesellschaft

def count_gesellschaft_sents(lines):
    gesellschaft_sents = 0
    sent_gesellschaft_status = 0
    for line in lines:
        blob  = TextBlobDE(line)
        words = blob.words
        if(len(set(words).intersection(gesellschaft)) > 0):
            sent_gesellschaft_status = 1
        else:
            sent_gesellschaft_status = 0
        gesellschaft_sents = gesellschaft_sents + sent_gesellschaft_status
    return(gesellschaft_sents)

#Wörter aus dem Themenbereich Wirtschaft zählen.

def count_wirtschaft_words(lines):
    number_of_wirtschaft_words = 0
    for line in lines:
        blob  = TextBlobDE(line)
        words = blob.words
        for word in words:
            if word in wirtschaft:
                number_of_wirtschaft_words = number_of_wirtschaft_words + 1
                out.write('WORT_WIRTSCHAFT: ' + word + '\t' + line)
    return(number_of_wirtschaft_words)


#Zahl der Sätze mit Wörtern aus dem Themenbereich Wirtschaft

def count_wirtschaft_sents(lines):
    wirtschaft_sents = 0
    sent_wirtschaft_status = 0
    for line in lines:
        blob  = TextBlobDE(line)
        words = blob.words
        if(len(set(words).intersection(wirtschaft)) > 0):
            sent_wirtschaft_status = 1
        else:
            sent_wirtschaft_status = 0
        wirtschaft_sents = wirtschaft_sents + sent_wirtschaft_status
    return(wirtschaft_sents)

#Wörter aus dem Themenbereich Ökologie zählen.

def count_oekologie_words(lines):
    number_of_oekologie_words = 0
    for line in lines:
        blob  = TextBlobDE(line)
        words = blob.words
        for word in words:
            if word in oekologie:
                number_of_oekologie_words = number_of_oekologie_words + 1
                out.write('WORT_ÖKOLOGIE: ' + word + '\t' + line)
    return(number_of_oekologie_words)

#Zahl der Sätze mit Wörtern aus dem Themenbereich Ökologie

def count_oekologie_sents(lines):
    oekologie_sents = 0
    sent_oekologie_status = 0
    for line in lines:
        blob  = TextBlobDE(line)
        words = blob.words
        if(len(set(words).intersection(oekologie)) > 0):
            sent_oekologie_status = 1
        else:
            sent_oekologie_status = 0
        oekologie_sents = oekologie_sents + sent_oekologie_status
    return(oekologie_sents)

#Wörter aus dem Themenbereich Sonstiges zählen.

def count_sonstiges_words(lines):
    number_of_sonstiges_words = 0
    for line in lines:
        blob  = TextBlobDE(line)
        words = blob.words
        for word in words:
            if word in sonstiges:
                number_of_sonstiges_words = number_of_sonstiges_words + 1
                out.write('WORT_SONSTIGES: ' + word + '\t' + line)
    return(number_of_sonstiges_words)

#Zahl der Sätze mit Wörtern aus dem Themenbereich Sonstiges

def count_sonstiges_sents(lines):
    sonstiges_sents = 0
    sent_sonstiges_status = 0
    for line in lines:
        blob  = TextBlobDE(line)
        words = blob.words
        if(len(set(words).intersection(sonstiges)) > 0):
            sent_sonstiges_status = 1
        else:
            sent_sonstiges_status = 0
        sonstiges_sents = sonstiges_sents + sent_sonstiges_status
    return(sonstiges_sents)



def quote(zahl1,zahl2):
    qu = zahl1 * 100 / zahl2
    return(qu)



print('Zahl der Wörter im Text: ')
wt = count_words(lines)
print(wt)
print('Zahl der Sätze im Text: ')
st = count_sents(lines)
print(st)
print('Zahl der Public Value-Wörter im Text: ')
pvw = count_pv_words(lines)
print(pvw)
print('Prozentsatz der Public Value-Wörter an allen Wörtern: ')
print(quote(pvw,wt))
print('Zahl der Sätze mit Wörtern aus dem Themenbereich Public Value: ')
pvs = count_pv_sents(lines)
print(pvs)
print('Prozentsatz der Sätze mit Public Value-Inhalten an allen Sätzen: ')
print(quote(pvs,st))
print('Zahl der Gesellschaftswörter im Text: ')
gw = count_gesellschaft_words(lines)
print(gw)
print('Prozentsatz der Gesellschaftswörter an allen Wörtern: ')
print(quote(gw,wt))
print('Zahl der Sätze mit Wörtern aus dem Themenbereich Gesellschaft: ')
gs = count_gesellschaft_sents(lines)
print(gs)
print('Prozentsatz der Sätze mit Gesellschaftsinhalten an allen Sätzen: ')
print(quote(gs,st))
print('Zahl der Wirtschaftswörter im Text: ')
ww = count_wirtschaft_words(lines)
print(ww)
print('Prozentsatz der Wirtschaftswörter an allen Wörtern: ')
print(quote(ww,wt))
print('Zahl der Sätze mit Wörtern aus dem Themenbereich Wirtschaft: ')
ws = count_wirtschaft_sents(lines)
print(ws)
print('Prozentsatz der Sätze mit Wirtschaftsinhalten an allen Sätzen: ')
print(quote(ws,st))
print('Zahl der Ökologiewörter im Text: ')
ow = count_oekologie_words(lines)
print(ow)
print('Prozentsatz der Ökologiewörter an allen Wörtern: ')
print(quote(ow,wt))
print('Zahl der Sätze mit Wörtern aus dem Themenbereich Ökologie: ')
os = count_oekologie_sents(lines)
print(os)
print('Prozentsatz der Sätze mit Ökologie-Inhalten an allen Sätzen: ')
print(quote(os,st))
print('Zahl der sonstigen Wörter im Text: ')
sw = count_sonstiges_words(lines)
print(sw)
print('Prozentsatz der sonstigen Wörter an allen Wörtern: ')
print(quote(sw,wt))
print('Zahl der Sätze mit Wörtern aus dem Themenbereich Sonstiges: ')
ss = count_sonstiges_sents(lines)
print(ss)
print('Prozentsatz der Sätze mit Sonstiges-Inhalten an allen Sätzen: ')
print(quote(ss,st))




textin.close()
out.close()
