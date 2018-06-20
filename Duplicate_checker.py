#Script checks a given fasta for Sequences with identical Name; need BioPython; can output duplicate free fasta(1), name of duplicates in standard out(2), or textfile with names of duplicates(3)
#use the script like: $: python Duplicate_checker.py any.fasta
from Bio import SeqIO
import sys 
inputFasta= sys.argv[1]
liste= set()

eingabe1=input("Do you want a dupicate free fasta ? --> enter 1" + "\n" + 
               "Do you want the names of duplicates on standard out? --> enter 2" + "\n" +
              "Do you want the name of duplicates in a text file list? --> enter 3" + "\n")
if eingabe1 == "1":
    with open(inputFasta, 'r') as t:
        with open(inputFasta+ "_noDuplicates", 'w')as r:
            for record in SeqIO.parse(t, 'fasta'):
                if record.id not in liste:
                    liste.add(record.id)
                    SeqIO.write(record, r, 'fasta')
                elif record.id in liste:
                    print(record.id)
                
elif eingabe1=="2":
    with open(inputFasta, 'r') as t:
        for record in SeqIO.parse(t, 'fasta'):
            if record.id not in liste:
                liste.add(record.id)
            elif record.id in liste:
                print(record.id)

elif eingabe1=="3":
    with open(inputFasta, 'r') as t:
        with open(inputFasta + "_list_of_Duplicates", 'w') as r:
            for record in SeqIO.parse(t, 'fasta'):
                if record.id not in liste:
                    liste.add(record.id)
                elif record.id in liste:
                    r.write(record.id + "\n")   
