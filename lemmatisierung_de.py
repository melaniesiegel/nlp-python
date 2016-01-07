from textblob_de import TextBlobDE
from morphy_mapping import lemma

'''Lemmatisierung auf Basis des Dictionaries morphy_mapping.
Für jedes Wort wird nachgesehen, ob es im Dictionary mit einem Lemma verzeichnet ist.
Wenn ja, dann wird es durch das Lemma ersetzt. Wenn nicht, dann bleibt es stehen.
Für den langen Text habe ich versucht, das als Pre-Processing durchzuführen - also nur einmal zu machen.
Das ist allerdings so langsam, dass es auch nach Stunden noch nicht zu einem Ende führt.
'''


testtext = open('all.txt','r', encoding='utf-8').read()

all_lemmatized = open('all_lemmatized.txt','w', encoding='utf-8')


def lemmatize_word(word):
    if word in lemma.keys():
        return(lemma[word])
    else:
        return(word)
    print('.')

def lemmatize_sentence(sentence):
    sblob = TextBlobDE(str(sentence))
    for w in sblob.words:
        w_new = lemmatize_word(w)
        sentence = sentence.replace(w,w_new)
    return(sentence)

all_lemmatized.write(lemmatize_sentence(testtext))

testtext.close()
all_lemmatized.close()
