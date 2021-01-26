from Bio import Entrez
import SRA Toolkit #import SRA toolkit.. unsure if this is the correct way to do so
import subprocess
import time
import os

def get_metagenomes(acc_list_file):
    '''
        Get metagenomes from NCBI given a list of accession numbers
    '''
    #for each accession number in an acc_list file, 
    for acc_list in acc_list_file:
        if os.path.isfile("fastas/{}.fasta".format(acc_list)):
            continue
        f = open("fastas/{}.fasta".format(acc_list), "w")
        sra = prefetch --option-file acc_list
        seq = fasterq-dump --split-files sra
        f.write(seq.read().decode().strip().replace('\n', ''))
        f.close()
        time.sleep(0.4)

def group_metagenomes(out):
    '''
        Group metagenomes in one large fasta file
    '''
    subprocess.call(['cat', 'fastas/*.fasta', '>', '{}.fasta'.format(out)])

def get_genomes_binfatis(acc_list):
    '''
        Get metagenomes from NCBI given a list of accession numbers
    '''
    #for each accession number in an acc_list file, 
    for acc in acc_list:
        if os.path.isfile("fastas/{}.fasta".format(acc)):
            continue
        f = open("fastas/{}.fasta".format(acc), "w")
        seq = Entrez.efetch(db="nucleotide", id=acc, rettype="fasta")
        f.write(seq.read().decode().strip().replace('\n', ''))
        f.close()
        time.sleep(0.4)


