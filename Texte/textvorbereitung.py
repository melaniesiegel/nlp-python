
##dient zur weiteren Vorbereitung der Texte, Löschen unnötiger Tabs, Leerzeichen und Zeilenumbrüche

import nltk
from textblob_de import TextBlobDE


raw_text = open('all.txt', 'r',encoding='utf-8')
out = open('out.txt','w',encoding='utf-8')

lines = raw_text.readlines()

all_sentences = []

for line in lines:
    line = line.replace('\r','')
    line = line.replace('\n','')
    line = line.replace('\t',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    line = line.replace('  ',' ')
    blob = TextBlobDE(line)
    sentences = blob.sentences
    all_sentences = all_sentences + sentences
#    print(line)

for sentence in all_sentences:
    out.write(str(sentence) + '\n')

raw_text.close()
out.close()
