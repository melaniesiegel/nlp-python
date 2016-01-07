import nlp_basics
from nlp_basics import *
from keyword_cluster_dict import cluster

textin = open('adidas_JA_2012_Text.txt', 'r',encoding='utf-8')

out = open('out.txt','w',encoding='utf-8')

testcluster = ['arbeitnehmer_arbeitgeber_verhaeltnis','forschung', 'leistung']

#inputfile = input('Welche Datei soll analysiert werden? ')

#textin = open(inputfile, 'r',encoding='utf-8')

lines = textin.readlines()

# Zugriff auf das Dictionary, das jedem Wort sein Cluster zuordnet.

def categorize_word(word):
    if word in cluster.keys():
        return(cluster[word])
    else:
        return('None')
                
            
# Eine Zeile (Satz) verarbeiten, dabei alle Cluster in dieser Zeile listen

def clusters_in_line(line):
    words = TextBlobDE(line).words
    lclusters = []
    for word in words:
        wcluster = categorize_word(word)
        if wcluster == 'None':
            lclusters = lclusters
        else:
           lclusters.append(wcluster)
    return(lclusters)

# Cluster-Listen abstrahieren. Idee: Wenn es mehrere Cluster in einer Zeile gibt, sucht man einen gemeinsamen Nenner.
# Also z.B. investment + gleichbehandlung --> menschenrechte

leitlinie = ['leitlinie','standard','standards']
menschenrechte = ['investment','gleichbehandlung','menschenrechte_allgemein', 'vereinigungsfreiheit', 'kinderarbeit', 'zwangs_oder_pflichtarbeit', 'sicherheitspraktiken', 'rechte_der_indigenen_bevoelkerung', 'menschenrechte_pruefung', 'bewertung_der_lieferanten_hinsichtlich_menschenrechten', 'beschwerde']
arbeitspraktien_und_menschenwuerdige_beschaeftigung = ['arbeitspraktiken_allgemein', 'beschaeftigung','arbeitnehmer_arbeitgeber_verhaeltnis','arbeitssicherheit_und_gesundheitsschutz','aus_und_weiterbildung','vielfalt_und_chancengleichheit','bezahlung','bewertung_der_lieferanten_hinsichtlich_arbeitspraktiken','beschwerde']
gesellschaft_gesellschaft = ['lokale_gemeinschaften','korruptionsbekaempfung','politik','wettbewerbswidriges_verhalten','gesellschaft_compliance','auswirkung','beschwerde','gesellschaft_gesellschaft_allgemein']
produktverantwortung = ['kundengesundheit_und_sicherheit','kennzeichnung_von_produkten_und_dienstleistungen','marketing','schutz_der_privatsphaere_des_kunden','produktverantwortung_compliance','forschung']




def abstract_cluster_lists(clist):
    sorted_clusters = sorted(set(clist))    #erst mal sortieren und doppelte rauswerfen
    if len(sorted_clusters) == 1:            #wenn es dann nur ein Cluster ist, dann bleibt es dabei
        return(sorted_clusters)
    elif len(sorted_clusters) == 2:          #bei zwei Clustern muss man versuchen zu abstrahieren
        if sorted_clusters[0] in menschenrechte and sorted_clusters[0] in menschenrechte:
            return(['_menschenrechte_'])
        elif sorted_clusters[0] in arbeitspraktien_und_menschenwuerdige_beschaeftigung and sorted_clusters[0] in arbeitspraktien_und_menschenwuerdige_beschaeftigung:
            return(['_arbeitspraktien_und_menschenwuerdige_beschaeftigung_'])
        elif sorted_clusters[0] in gesellschaft_gesellschaft and sorted_clusters[0] in gesellschaft_gesellschaft:
            return(['_gesellschaft_gesellschaft_'])
        elif sorted_clusters[0] in produktverantwortung and sorted_clusters[0] in produktverantwortung:
            return(['_produktverantwortung_'])
        elif sorted_clusters[0] in leitlinie and sorted_clusters[0] in leitlinie:
            return(['_leitlinie_'])
        else:
            return(sorted_clusters)
    else:
        return(sorted_clusters)


# Den ganzen Text verarbeiten und Cluster-Listen herausgeben

for line in lines:
    lclusters = clusters_in_line(line)
    lclusters = abstract_cluster_lists(lclusters)
    if len(lclusters) > 0:
        out.write(str(lclusters) + '\t' + line)
#    out.write(str(clusters_in_line(line)) + '\t' + line)

    






textin.close()
out.close()
