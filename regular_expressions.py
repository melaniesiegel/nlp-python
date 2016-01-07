import nlp_basics
from nlp_basics import *

##### Einen Geschäftsbericht öffnen ####

adidas_text = open('adidas_JA_2012_Text.txt','r')
text_long = adidas_text.read()

#### Regular Expressions ####

#alle Wörter, die mit "heit" enden
heitwords = re.findall(r"\w+heit",text_long)

print ("HEIT:", heitwords)
