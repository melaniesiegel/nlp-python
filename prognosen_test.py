import prognosen
from prognosen import umsatz_prognose

test1 = '''Für adidas Sport Performance wird nun voraussichtlich ein Umsatz in Höhe von 8,9 Mrd. € erreicht werden (bisherige Prognose: 8,5 Mrd. €).'''
test2 = '''Bei der Marke Reebok erwartet das Management nun für 2015 Umsatzerlöse in Höhe von 2 Mrd. €; die bisherige Prognose lag bei 3 Mrd. €.'''
test3 = '''Anstatt der bisherigen 10,6 Mrd. € erwartet das Management nun einen Umsatz in Höhe von 10,2 Mrd. €.'''
test4 = '''Die Umsatzprognose für das Einzelhandelssegment bleibt mit 4,6 Mrd. € unverändert.'''
test5 = '''Zudem wollen wir unser eCommerce-Geschäft deutlich steigern, unseren Prognosen zufolge bis 2015 auf 500 Mio. €.'''
test6 = '''Im Segment Großhandel rechnen wir im Vergleich zum Vorjahr mit einem währungsbereinigten Umsatzanstieg im niedrigen einstelligen Bereich.'''
test7 = '''Bei adidas Sport Style wurde die Prognose von 3,7 Mrd. € auf 3,9 Mrd. € angepasst.'''
test8 = '''Der Umsatz von adidas Sport Style wird den Prognosen zufolge auf währungsbereinigter Basis im hohen einstelligen Bereich ansteigen.'''
test9 = '''Für Reebok erwarten wir einen Anstieg des währungsbereinigten Umsatzes im mittleren einstelligen Bereich.'''
test10 = '''Wir erwarten für das Einzelhandelssegment im Geschäftsjahr 2013 einen Umsatzzuwachs auf währungsbereinigter Basis im hohen einstelligen bis niedrigen zweistelligen Bereich.'''
test11 = '''Auf vergleichbarer Basis wird der Umsatz gegenüber dem Vorjahr voraussichtlich im niedrigen bis mittleren einstelligen Bereich steigen. '''
test12 = '''Für das Jahr 2013 erwarten wir, dass der Umsatz in den anderen Geschäftssegmenten auf währungsbereinigter Basis im mittleren bis hohen einstelligen Bereich ansteigen wird. '''
test13 = '''Bei TaylorMade-adidas Golf rechnen wir mit einem währungsbereinigten Anstieg gegenüber dem Vorjahr im mittleren einstelligen Bereich.'''
test14 = '''Für Rockport prognostizieren wir ein währungsbereinigtes Umsatzplus im mittleren bis hohen einstelligen Bereich. '''
test15 = '''Bei Reebok-CCM Hockey erwarten wir, dass sich der währungsbereinigte Umsatz im niedrigen zweistelligen Bereich erhöhen wird. '''
test16 = '''Wir erwarten, dass der währungsbereinigte Umsatz des Konzerns 2013 in all unseren Regionen, wenn auch in unterschiedlichem Ausmaß, steigen wird. '''
test17 = '''In Westeuropa wird der Umsatz im Jahr 2013, trotz nicht wiederkehrender positiver Effekte des Vorjahres im Zusammenhang mit der UEFA EURO 2012 und den Olympischen Spielen in London, voraussichtlich eine moderat positive Entwicklung verzeichnen.'''
test18 = '''In Nordamerika rechnen wir aufgrund der anhaltenden Dynamik der Marke adidas mit einem soliden Wachstum. '''
test19 = '''Wir erwarten, dass Reebok dank neuer Produkteinführungen wieder auf einen Wachstumspfad zurückkehren wird.'''
test20 = '''Für China prognostizieren wir, dass der Umsatz im Rahmen unserer Zielvorgaben von Route 2015 weiter steigen wird. '''
test21 = '''In Lateinamerika werden Handelseinschränkungen die Wachstumsaussichten und die zeitliche Verteilung von Umsätzen in bestimmten Märkten beeinträchtigen; dennoch gehen wir davon aus, dass sich die solide Dynamik der Sportartikelbranche dieser Region positiv auf die Umsatzentwicklung des Konzerns auswirken wird.'''
test22 = '''Zudem werden der FIFA Confederations Cup 2013 sowie die Vorbereitungen auf die FIFA Fußballweltmeisterschaft 2014 die Entwicklung in dieser Region begünstigen.'''
test23 = '''Es wird mit Verbesserungen in allen Segmenten gerechnet.'''
test24 = '''Die Bruttomarge wird von positiven Effekten aus der regionalen Umsatzverteilung und unserem Vertriebsmix profitieren, da die Wachstumsraten in den Schwellenländern und im Einzelhandelssegment, die jeweils hohe Margen erzielen, über den Wachstumsraten in den reiferen Märkten und im Großhandelssegment liegen dürften.'''
test25 = '''Des Weiteren werden Verbesserungen im Einzelhandelssegment sowie bei der Marke Reebok die Entwicklung der Bruttomarge fördern.'''
test26 = '''Diese positiven Effekte werden jedoch durch im Vergleich zum Vorjahr weniger günstige Hedging-Konditionen sowie durch steigende Lohnkosten, die unsere Umsatzkosten negativ beeinflussen dürften, zum Teil aufgehoben werden.'''
test27 = '''Ergebnis je Aktie steigt voraussichtlich auf 4,25 € bis 4,40 € '''
test28 = '''Das unverwässerte und verwässerte Ergebnis je Aktie wird unseren Prognosen zufolge um 12% bis 16% auf einen Wert zwischen 4,25 € und 4,40 € steigen (2012 ohne Wertminderung der Geschäfts- oder Firmenwerte: 3,78 €).'''
test29 = '''Dies entspricht einem auf Anteilseigner entfallenden Konzerngewinn in Höhe von 890 Mio. € bis 920 Mio. €. '''
test30 = '''Umsatzzuwächse und eine höhere operative Marge werden maßgeblich zu dieser positiven Entwicklung beitragen.'''
test31 = '''Für die Jahre 2014 und 2015 erwarten wir gemäß den Zielen des strategischen Geschäftsplans Route 2015 einen Anstieg von Umsatz und Gewinn sowie eine weitere Verbesserung der operativen Marge.'''
test32 = '''Für die Jahre 2014 und 2015 erwarten wir gemäß den Zielen des strategischen Geschäftsplans Route 2015 einen Anstieg von Umsatz und Gewinn sowie eine weitere Verbesserung der operativen Marge.'''


print(test1 + ":")
umsatz_prognose(test1)

print(test2 + ":")
umsatz_prognose(test2)

print(test3 + ":")
umsatz_prognose(test3)

print(test4 + ":")
umsatz_prognose(test4)

print(test5 + ":")
umsatz_prognose(test5)

print(test6 + ":")
umsatz_prognose(test6)

print(test7 + ":")
umsatz_prognose(test7)

print(test8 + ":")
umsatz_prognose(test8)

print(test9 + ":")
umsatz_prognose(test9)

print(test10 + ":")
umsatz_prognose(test10)

print(test11 + ":")
umsatz_prognose(test11)

print(test13 + ":")
umsatz_prognose(test13)

print(test14 + ":")
umsatz_prognose(test14)

print(test15 + ":")
umsatz_prognose(test15)

print(test15 + ":")
umsatz_prognose(test15)

print(test15 + ":")
umsatz_prognose(test15)

print(test16 + ":")
umsatz_prognose(test16)

print(test17 + ":")
umsatz_prognose(test17)

print(test18 + ":")
umsatz_prognose(test18)

print(test19 + ":")
umsatz_prognose(test19)

print(test20 + ":")
umsatz_prognose(test20)

print(test21 + ":")
umsatz_prognose(test21)

print(test22 + ":")
umsatz_prognose(test22)

print(test23 + ":")
umsatz_prognose(test23)

print(test24 + ":")
umsatz_prognose(test24)


print(test25 + ":")
umsatz_prognose(test25)

print(test26 + ":")
umsatz_prognose(test26)

print(test27 + ":")
umsatz_prognose(test27)

print(test28 + ":")
umsatz_prognose(test28)

print(test29 + ":")
umsatz_prognose(test29)

print(test30 + ":")
umsatz_prognose(test30)

print(test31 + ":")
umsatz_prognose(test31)

