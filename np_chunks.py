import nlp_basics
from nlp_basics import *
import pos_tagging
from pos_tagging import *

#### Nominalphrasen ####

# mit Textblob
print ("Chunks mit Textblob")
print(blob.noun_phrases)

# mit eigener Chunk-Grammatik

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
