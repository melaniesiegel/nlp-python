import nlp_basics
from nlp_basics import *
from collections import Counter

#Ziel: für eine Liste von Wörtern alle Komposita finden, die mit diesen Wörtern im Korpus gebildet wurden.

testtext = open('all.txt','r', encoding='utf-8')

#testtext = "Nachhaltigkeitsbericht und Compliance-Prozesse und Gesellschaftssystemen"

keywordlist = ['Überstunden', 'ökologisch', 'Abfälle', 'Abfall', 'Abwasser', 'Alter', 'Altersgruppe', 'Altersstruktur', 'Altersvorsorgeverpflichtungen', 'Antikorruption', 'Arbeitnehmerausschuss', 'Arbeitnehmervertreter', 'Arbeitsbedingungen', 'Arbeitspraktiken', 'Artenschutz', 'Aufbereitung', 'Auftreten', 'Ausbildung', 'Ausfalltage', 'Auswirkungen', 'Auszeichnung', 'Auszubildende', 'Award', 'Baseler Übereinkommen', 'Basler Übereinkommen', 'Beruf und Privatleben', 'Berufskrankheit', 'Beschäftigung', 'Beschaffung', 'Beschwerde', 'Beschwerden', 'Bewertung', 'Bezahlung', 'Bonus', 'Bußgeld', 'Bußgelder', 'CO2', 'Compliance', 'Dialog', 'Diskriminierung', 'Effekte', 'Einstiegsgehälter', 'Eintrittsgehälter', 'Emission', 'Emissionen', 'Energie', 'Energieeffizienz', 'Energieverbrauch', 'Engagement', 'Entlohnung', 'Entsorgung', 'Erderwärmung', 'Erfolgsbeteiligung', 'Externe Effekte', 'Förderung', 'Fluktuation', 'Fluktuationsrate', 'Forschung', 'Forschungsausgabe', 'Frauen', 'FuE-Ausgabe', 'Gefahrgut', 'Gefahrstoffe', 'Gehälter', 'Gehalt', 'Geschlecht', 'Gesundheit', 'Gewerkschaft', 'Gewicht', 'Gleichbehandlung', 'Gleichberechtigung', 'Greenhouse Gas Protocol', 'Habität', 'Hilfe', 'Index', 'Indikator', 'Indirekte  Auswirkungen', 'Infrastruktur', 'Innovation', 'Kennzahl', 'Kennzeichnung', 'Kinderarbeit', 'Klimaschutz', 'Klimawandel', 'Kodex', 'Kommunikation', 'Korruption', 'Korruptionsfälle', 'Kunden', 'Kundengesundheit', 'Kundensicherheit', 'Kundenzufriedenheit', 'Lebensraum', 'Leistung', 'Leitlinien', 'Lieferanten', 'Lieferkette', 'Logistik', 'Lokale Gemeinschaften', 'Marketing', 'Marktpräsenz', 'Material', 'Materialität', 'Menge', 'Menschenrecht', 'Menschenrechte', 'Menschenrechtspolitik', 'Meschlichkeitsklausel', 'Meschlichkeitsklauseln', 'Minderheit', 'Mindestlohn', 'Mitarbeiter', 'Mitarbeiterausschuss', 'Mitarbeiterzufriedenheit', 'Mobilität', 'NOX', 'Nachhaltigkeit', 'Nachhaltigkeitsindex', 'Nationalpark', 'Neueinstellung', 'Neueinstellungen', 'Nichteinhaltung', 'Pensionen', 'Performance', 'Pflichtarbeit', 'Politsche Spenden', 'Privatsphäre', 'Produkt', 'Produkte', 'Produktentwicklung', 'Produktionsfaktor', 'Rückgewinnung', 'Rückkehrer', 'Rückkehrrate', 'Rückstellung', 'Rating', 'Reduktion', 'Schulung', 'Schutzgebiet', 'Schwermetall', 'Schwermetalle', 'Sicherheit', 'Spenden', 'Staatliche Leistungen', 'Staatliche Unterstützung', 'Stakeholder', 'Stakeholdereinbezug', 'Stickstoff', 'Stiftung', 'Strategie', 'Training', 'Transport', 'Treibhauseffekt', 'Trinkwasser', 'Umfrage', 'Umwelt', 'Umweltgesetz', 'Umweltgesetze', 'Umweltschutz', 'Unfälle', 'Unterstützung', 'Ureinwohner', 'Verantwortung', 'Verbotene Produkte', 'Verbrauch', 'Vereinigungsfreiheit', 'Verhaltenskodex', 'Verletzungen', 'Verpackung', 'Verpackungen', 'Verringerung', 'Versammlungfreiheit', 'Verteilter Wert', 'Vielfalt', 'Wasser', 'Wasserentnahme', 'Wasserverbrauch', 'Weiterbildung', 'Werbung', 'Wertschöpfung', 'Wesentlichkeit', 'Wiederverwendung', 'Wissenschaft', 'Work-Life', 'Zufriedenheit', 'Zulieferer', 'Zwangsarbeit', 'diversity', 'einleiten', 'energieeffizient', 'engagiert', 'fördern', 'gesellschaftlich', 'indigen', 'kartell', 'langfristig', 'lokal', 'nachhaltig', 'nicht-finanziell', 'non-financial', 'regional', 'responsibility', 'sozial', 'spenden', 'umstrittene Produkte', 'wettbewerbswidrig']


lines = testtext.readlines()

#blob = TextBlobDE(str(lines))
words = TextBlobDE(str(lines)).words
#sentences = blob.sentences

#compound_pattern = re.compile(r'($KEYWORD.+)')

#keyword = "Compliance"

##Alle Komposita mit einem Keyword heraussuchen

def find_compounds_in_sentence(keyword,words):
    compounds = []
    for word in words:
        if re.search(r'(%s.+)' %keyword, word):
            compounds = compounds + [word]
    return compounds

for keyword in keywordlist:
    print(keyword + ':')
    print(find_compounds_in_sentence(keyword,words))
    
testtext.close()
