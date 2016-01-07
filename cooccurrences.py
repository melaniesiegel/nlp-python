import nlp_basics
from nlp_basics import *
from collections import Counter

##Ziel: für ein gegebenes Wort alle Nomen, Verben und Adjektive finden, die im selben Satz stehen.

##z.B.: Compliance

testtext = open('all.txt','r', encoding='utf-8')

cooc_out = open('cooc_out.xml','w', encoding='utf-8')

#zunächst nur für ein Keyword - zum Testen
#keyword = "Compliance"

#jetzt mit den Keyword aus dem Input:
#keyword = input("Keyword: ")

#jetzt mit einer Liste von Keywords:
keywordlist = ['Überstunden', 'ökologisch', 'Abfälle', 'Abfall', 'Abwasser', 'Alter', 'Altersgruppe', 'Altersstruktur', 'Altersvorsorgeverpflichtungen', 'Antikorruption', 'Arbeitnehmerausschuss', 'Arbeitnehmervertreter', 'Arbeitsbedingungen', 'Arbeitspraktiken', 'Artenschutz', 'Aufbereitung', 'Auftreten', 'Ausbildung', 'Ausfalltage', 'Auswirkungen', 'Auszeichnung', 'Auszubildende', 'Award', 'Baseler Übereinkommen', 'Basler Übereinkommen', 'Beruf und Privatleben', 'Berufskrankheit', 'Beschäftigung', 'Beschaffung', 'Beschwerde', 'Beschwerden', 'Bewertung', 'Bezahlung', 'Bonus', 'Bußgeld', 'Bußgelder', 'CO2', 'Compliance', 'Dialog', 'Diskriminierung', 'Effekte', 'Einstiegsgehälter', 'Eintrittsgehälter', 'Emission', 'Emissionen', 'Energie', 'Energieeffizienz', 'Energieverbrauch', 'Engagement', 'Entlohnung', 'Entsorgung', 'Erderwärmung', 'Erfolgsbeteiligung', 'Externe Effekte', 'Förderung', 'Fluktuation', 'Fluktuationsrate', 'Forschung', 'Forschungsausgabe', 'Frauen', 'FuE-Ausgabe', 'Gefahrgut', 'Gefahrstoffe', 'Gehälter', 'Gehalt', 'Geschlecht', 'Gesundheit', 'Gewerkschaft', 'Gewicht', 'Gleichbehandlung', 'Gleichberechtigung', 'Greenhouse Gas Protocol', 'Habität', 'Hilfe', 'Index', 'Indikator', 'Indirekte  Auswirkungen', 'Infrastruktur', 'Innovation', 'Kennzahl', 'Kennzeichnung', 'Kinderarbeit', 'Klimaschutz', 'Klimawandel', 'Kodex', 'Kommunikation', 'Korruption', 'Korruptionsfälle', 'Kunden', 'Kundengesundheit', 'Kundensicherheit', 'Kundenzufriedenheit', 'Lebensraum', 'Leistung', 'Leitlinien', 'Lieferanten', 'Lieferkette', 'Logistik', 'Lokale Gemeinschaften', 'Marketing', 'Marktpräsenz', 'Material', 'Materialität', 'Menge', 'Menschenrecht', 'Menschenrechte', 'Menschenrechtspolitik', 'Meschlichkeitsklausel', 'Meschlichkeitsklauseln', 'Minderheit', 'Mindestlohn', 'Mitarbeiter', 'Mitarbeiterausschuss', 'Mitarbeiterzufriedenheit', 'Mobilität', 'NOX', 'Nachhaltigkeit', 'Nachhaltigkeitsindex', 'Nationalpark', 'Neueinstellung', 'Neueinstellungen', 'Nichteinhaltung', 'Pensionen', 'Performance', 'Pflichtarbeit', 'Politsche Spenden', 'Privatsphäre', 'Produkt', 'Produkte', 'Produktentwicklung', 'Produktionsfaktor', 'Rückgewinnung', 'Rückkehrer', 'Rückkehrrate', 'Rückstellung', 'Rating', 'Reduktion', 'Schulung', 'Schutzgebiet', 'Schwermetall', 'Schwermetalle', 'Sicherheit', 'Spenden', 'Staatliche Leistungen', 'Staatliche Unterstützung', 'Stakeholder', 'Stakeholdereinbezug', 'Stickstoff', 'Stiftung', 'Strategie', 'Training', 'Transport', 'Treibhauseffekt', 'Trinkwasser', 'Umfrage', 'Umwelt', 'Umweltgesetz', 'Umweltgesetze', 'Umweltschutz', 'Unfälle', 'Unterstützung', 'Ureinwohner', 'Verantwortung', 'Verbotene Produkte', 'Verbrauch', 'Vereinigungsfreiheit', 'Verhaltenskodex', 'Verletzungen', 'Verpackung', 'Verpackungen', 'Verringerung', 'Versammlungfreiheit', 'Verteilter Wert', 'Vielfalt', 'Wasser', 'Wasserentnahme', 'Wasserverbrauch', 'Weiterbildung', 'Werbung', 'Wertschöpfung', 'Wesentlichkeit', 'Wiederverwendung', 'Wissenschaft', 'Work-Life', 'Zufriedenheit', 'Zulieferer', 'Zwangsarbeit', 'diversity', 'einleiten', 'energieeffizient', 'engagiert', 'fördern', 'gesellschaftlich', 'indigen', 'kartell', 'langfristig', 'lokal', 'nachhaltig', 'nicht-finanziell', 'non-financial', 'regional', 'responsibility', 'sozial', 'spenden', 'umstrittene Produkte', 'wettbewerbswidrig']



keyword_cluster = []
allcompounds = []

lines = testtext.readlines()

blob = TextBlobDE(str(lines))
sentences = blob.sentences

#compound_pattern = re.compile(r'(Compliance-.+)')
compound_pattern = re.compile(r'(Fluktuation.+)')

## Alle Nomen aus einem Satz herausgeben:

def nouns_verbs_adjs(blob):
    tags = blob.tags
    scluster = []
    for word in tags:
        if word[1] in ["NN", "NNP"]:
            scluster = scluster + [word[0]]
    return scluster



## Alle Nomen, die mit dem Keyword in einem Satz auftreten, in eine Liste packen:
'''
for satz in sentences:
    if (keyword in satz):
        sblob = TextBlobDE(str(satz))
        words = sblob.words
        scluster = nouns_verbs_adjs(sblob)
        compliance_cluster = compliance_cluster + scluster
        scompounds = find_compounds_in_sentence(words)
        allcompounds = allcompounds + scompounds

## Liste nach Häufigkeit sortieren, nur die häufigsten 10 ausgeben

print (Counter(compliance_cluster).most_common(50))
print (Counter(allcompounds))

'''

#Dasselbe für alle Keywords, die dann in eine Ausgabedatei kommen. Komposita lasse ich erst mal aus.

for keyword in keywordlist:
    print(keyword)
    keyword_cluster = []
    for satz in sentences:
        if (keyword in satz):
            sblob = TextBlobDE(str(satz))
            words = sblob.words
            scluster = nouns_verbs_adjs(sblob)
            keyword_cluster = keyword_cluster + scluster
    cooc_out.write('<KEYWORD>' + keyword + '</KEYWORD>' + '<CLUSTER>' )
    cooc_out.write(str(Counter(keyword_cluster).most_common(50)))
    cooc_out.write('</CLUSTER>\n')




testtext.close()
cooc_out.close()
