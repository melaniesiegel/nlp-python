import nlp_basics
from nlp_basics import *
import re
import ner
from ner import *
 
testsaetze = open('prognosen_sentences.txt','r', encoding='utf-8')
prognosen_out = open('prognosen_out.xml','w', encoding='utf-8')


##Patterns

erwartung_pattern = re.compile(r'(voraussichtlich|erwartet|rechnen|erwarten) .* Umsatz.* .+ €')
erwartung_pattern2 = re.compile(r'(.*gewinn .* von) (\d+ Mio\. €)')

stagnation_pattern = re.compile(r'Umsatz.* .+ bleibt .+ €')
anpassung_pattern = re.compile(r'(wurde \w* Prognose .* auf) (\d\,\d Mrd\. €) (angepasst)')
anpassung_pattern2 = re.compile(r'(Anpassung .* Prognose) .* (niedrigeren Umsatzziel)')

steigerung_pattern = re.compile(r'(voraussichtlich|erwartet|rechnen|erwarten|prognostizieren|gehen).* .* (Umsatz|Bruttomarge) .* (steigen|ansteigen)')
steigerung_pattern2 = re.compile(r'(voraussichtlich|erwartet|rechnen|erwarten|prognostizieren|gehen).* .* (Wachstum|Umsatzanstieg|wachsen)')
steigerung_pattern3 = re.compile(r'(voraussichtlich|erwartet|rechnen|erwarten|prognostizieren|gehen).* .* (positiv|Anstieg) .* Umsatz.*')
steigerung_pattern4 = re.compile(r'(Verbesserung.*|Wachstum|Impulse) .* (gerechnet|erwartet)')
steigerung_pattern5 = re.compile(r"(werden|wird) .* (Entwicklung|Effekten|Verbesserungen|Wachstum|Umsatzentwicklung|Umsatzwachstum) .* (unterst.tzen|beg.nstigen|profitieren|f.rdern|beitragen|ausgegangen|erwartet)")
steigerung_pattern6 = re.compile(r"(werden|wird) .* (Entwicklung|Effekten|Verbesserungen) (beg.nstigen|profitieren|f.rdern|beitragen)")
steigerung_pattern7 = re.compile(r"(erwarteten|bedeutende) (Umsatzanstieg|Wachstumschancen)")
steigerung_pattern8 = re.compile(r"(Umsatz .* voraussichtlich befl.geln)")
                                 
steigerung_auf_pattern = re.compile(r'(Gesch.ft .* steigern[a-zA-Z0-9, ]* auf) (\d+ Mio\. €)')
aktien_steigerung_auf_pattern = re.compile(r'(Aktie steigt voraussichtlich auf) (.+ €)')
aktien_steigerung_auf_pattern2 = re.compile(r'(Aktie .* auf) (.+ €) .* steigen')
aktien_steigerung_auf_pattern3 = re.compile(r'Steigerung .* (Aktie auf) (.+ €)')


steigerung_um_pattern2 = re.compile(r'(Umsatz.*|Konzernumsatz) im ((niedrigen|hohen|mittleren) .+stelligen Bereich) .*(steigen|höhen|wachsen)')
steigerung_um_pattern3 = re.compile(r'Anstieg .* im ((niedrigen|hohen|mittleren) .+stelligen Bereich)')
steigerung_um_pattern = re.compile(r'Umsatz(anstieg|zuwachs|plus)\s*(.*)?im ((niedrigen|hohen|mittleren) .+stelligen\s*(?:bis (niedrigen|hohen|mittleren) .+stelligen(.*))?Bereich)')
steigerung_um_pattern4 = re.compile(r'Umsatz .* (moderat positive Entwicklung)')
beeintraechtigung = re.compile(r'((Ums.tz.*|Wachstum) .* (beeintr.chtigen|bremsen|gef.hrden))')
beeintraechtigung2 = re.compile(r'((Ums.tz.*|Entwicklung) negativ (beeintr.chtigen|beeinflussen))')
beeintraechtigung3 = re.compile(r'((Ums.tz.*|Entwicklung|k.nnten) .* negativ (beeintr.chtigen|beeinflussen|auswirken))')
beeintraechtigung4 = re.compile(r'(voraussichtlich negativ .* (Umsatzentwicklung))')

beeintraechtigung5 = re.compile(r'((kann|Risiko) .* (Umsatzeinbu.en|Umsatzverlusts))')

def umsatz_prognose(txt):
    blob = TextBlobDE(txt)
    org_string = named_entities_org(blob)
    org_div_string = named_entities_org_division(blob)
    prod_string = named_entities_product(blob)
    market_string = named_entities_market(blob)
    if erwartung_pattern.search(txt):
        m = erwartung_pattern.search(txt)
        mstr = m.group(0)
        mblob = TextBlobDE(mstr)
        money_expressions = named_entities_money(mblob)
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzprognose</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT>' + prod_string + '</PRODUCT><VALUE>' + money_expressions + '</VALUE></PROGNOSE></ANALYSIS>')
    elif erwartung_pattern2.search(txt):
        m = erwartung_pattern2.search(txt)
        mstr = m.group(0)
        mblob = TextBlobDE(mstr)
        money_expressions = named_entities_money(mblob)
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Gewinnprognose</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT>' + prod_string + '</PRODUCT><VALUE>' + money_expressions + '</VALUE></PROGNOSE></ANALYSIS>')
    elif stagnation_pattern.search(txt):
        m = stagnation_pattern.search(txt)
        mstr = m.group(0)
        mblob = TextBlobDE(mstr)
        money_expressions = named_entities_money(mblob)
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzprognose</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT>' + prod_string + '</PRODUCT><VALUE>' + money_expressions + '</VALUE></PROGNOSE></ANALYSIS>')
    elif anpassung_pattern.search(txt):
        m = anpassung_pattern.search(txt)
        mstr = m.group(2)
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Prognose_Anpassung_auf</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE>' + mstr + '</VALUE></PROGNOSE></ANALYSIS>')
    elif anpassung_pattern2.search(txt):
        m = anpassung_pattern2.search(txt)
        mstr = m.group(2)
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Prognose_Anpassung_auf</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE>' + mstr + '</VALUE></PROGNOSE></ANALYSIS>')
    elif steigerung_auf_pattern.search(txt):
        m = steigerung_auf_pattern.search(txt)
        mstr = m.group(2)
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzsteigerung_auf</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE>' + mstr + '</VALUE></PROGNOSE></ANALYSIS>')
    elif aktien_steigerung_auf_pattern.search(txt):
        m = aktien_steigerung_auf_pattern.search(txt)
        mstr = m.group(2)
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Aktiensteigerung_auf</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE>' + mstr + '</VALUE></PROGNOSE></ANALYSIS>')
    elif aktien_steigerung_auf_pattern2.search(txt):
        m = aktien_steigerung_auf_pattern2.search(txt)
        mstr = m.group(2)
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Aktiensteigerung_auf</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE>' + mstr + '</VALUE></PROGNOSE></ANALYSIS>')
    elif aktien_steigerung_auf_pattern3.search(txt):
        m = aktien_steigerung_auf_pattern3.search(txt)
        mstr = m.group(2)
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Aktiensteigerung_auf</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE>' + mstr + '</VALUE></PROGNOSE></ANALYSIS>')
    elif steigerung_um_pattern.search(txt):
        m = steigerung_um_pattern.search(txt)
        mstr = m.group(3)
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzsteigerung_um</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE>' + mstr + '</VALUE></PROGNOSE></ANALYSIS>')
    elif steigerung_um_pattern2.search(txt):
        m = steigerung_um_pattern2.search(txt)
        mstr = m.group(1)
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzsteigerung_um</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE>' + mstr + '</VALUE></PROGNOSE></ANALYSIS>')
    elif steigerung_um_pattern3.search(txt):
        m = steigerung_um_pattern3.search(txt)
        mstr = m.group(1)
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzsteigerung_um</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE>' + mstr + '</VALUE></PROGNOSE></ANALYSIS>')
    elif steigerung_um_pattern4.search(txt):
        m = steigerung_um_pattern4.search(txt)
        mstr = m.group(1)
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzsteigerung_um</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE>' + mstr + '</VALUE></PROGNOSE></ANALYSIS>')
    elif steigerung_pattern.search(txt):
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzsteigerung</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE></VALUE></PROGNOSE></ANALYSIS>')
    elif steigerung_pattern2.search(txt):
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzsteigerung</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE></VALUE></PROGNOSE></ANALYSIS>')
    elif steigerung_pattern3.search(txt):
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzsteigerung</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE></VALUE></PROGNOSE></ANALYSIS>')
    elif steigerung_pattern4.search(txt):
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzsteigerung</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE></VALUE></PROGNOSE></ANALYSIS>')
    elif steigerung_pattern5.search(txt):
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzsteigerung</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE></VALUE></PROGNOSE></ANALYSIS>')
    elif steigerung_pattern6.search(txt):
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzsteigerung</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE></VALUE></PROGNOSE></ANALYSIS>')
    elif steigerung_pattern7.search(txt):
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzsteigerung</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE></VALUE></PROGNOSE></ANALYSIS>')
    elif steigerung_pattern8.search(txt):
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzsteigerung</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE></VALUE></PROGNOSE></ANALYSIS>')
    elif beeintraechtigung.search(txt):
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzbeeinträchtigung</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE></VALUE></PROGNOSE></ANALYSIS>')
    elif beeintraechtigung2.search(txt):
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzbeeinträchtigung</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE></VALUE></PROGNOSE></ANALYSIS>')
    elif beeintraechtigung3.search(txt):
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzbeeinträchtigung</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE></VALUE></PROGNOSE></ANALYSIS>')
    elif beeintraechtigung4.search(txt):
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzbeeinträchtigung</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE></VALUE></PROGNOSE></ANALYSIS>')
    elif beeintraechtigung5.search(txt):
        prognosen_out.write ('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE><ABOUT>Umsatzbeeinträchtigung</ABOUT><ORGANIZATION>' + org_string + '</ORGANIZATION><MARKET>' + market_string + '</MARKET><DIVISON>' + org_div_string + '</DIVISON><PRODUCT></PRODUCT><VALUE></VALUE></PROGNOSE></ANALYSIS>')
    else:
        prognosen_out.write('<ANALYSIS><TEXT>' + txt + '</TEXT><PROGNOSE>NO ANALYSIS</PROGNOSE></ANALYSIS>')


lines = testsaetze.readlines()


#for satz in lines:
#        print(satz + '\n')
#        umsatz_prognose(str(satz))
#        prognosen_out.write(' \n')

satz = '''Hohe Fluktuationsraten sowie unzureichende Fähigkeiten und Qualifikation der Mitarbeiter unseres eigenen Einzelhandels könnten sich negativ auf Umsatz und Profitabilität auswirken. EOS'''
umsatz_prognose(satz)
prognosen_out.write(' \n')
    
testsaetze.close()
prognosen_out.close()

