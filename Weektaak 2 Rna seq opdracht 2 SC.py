#!/usr/bin/env python

Seq = "" 
Bestand = open("/home/sasnee/Documents/School Bio-informatica/Bio-informatica/Blok 1/Week 2/Opdracht 2/SCrna seq.txt", "r")
for line in Bestand:
    if not line.startswith(">"):
        Seq = Seq + line
print(Seq)

print("Hieronder staat de volle sequentielengte")
print(len(Seq))
print("Hieronder staan alle basen in de volgorde ATGC")
print(Seq.count("A"))
print(Seq.count("T"))
print(Seq.count("G"))
print(Seq.count("C"))

print("Hieronder staat het aantal G + C bij elkaar opgeteld")

print(Seq.count("G") + (Seq.count("C")))
print("Hieronder staat het GC percentage")
GC_percentage = (((Seq.count("G") + (Seq.count("C"))) / len(Seq)) * 100)
print(GC_percentage,"%")

print("Saccharomyces Cerevisiae GC_percentage = 50.95%")
