#activate otherenv in conda
conda activate otherenv

from Bio import Entrez
import subprocess
import time
import os

def get_metagenomes(acc_list_file):
    '''
        Get metagenomes from NCBI given a list of accession numbers
    '''
    #for each accession number in an acc_list file, 
    for acc_list in acc_list_file:
        if os.path.isfile("fastqs/{}.fastq".format(acc_list)):
            continue
        f = open("fastqs/{}.fastq".format(acc_list), "w")
        sra = prefetch --option-file acc_list
        seq = fasterq-dump --split-files sra
        f.write(seq.read().decode().strip().replace('\n', ''))
        f.close()
        time.sleep(0.4)

def group_metagenomes(out):
    '''
        Group metagenomes in one large fasta file
    '''
    subprocess.call(['cat', 'fastqs/*.fastq', '>', 'Metagenome_1.fastq'.format(out)])

def get_genomes_binfatis(acc_list):
    '''
        Get metagenomes from NCBI given a list of accession numbers
    '''
    #for each accession number in an acc_list file, 
    for acc in acc_list:
        if os.path.isfile("fastas/{}.fasta".format(acc)):
            continue
        f = open("fastas/{}.fasta".format(acc), "w")
        seq = Entrez.efetch(db="nuccore", id=acc, rettype="fasta")
        f.write(seq.read().decode().strip().replace('\n', ''))
        f.close()
        time.sleep(0.4)

#Merge all B. infantis reference genomes into one genomes.fna file
    cp HQ*.fasta HQ*.fna
    cat ref_genomes/binfantis/*.fna > binfantisgenomes.fna

#Create a bowtie2 index database
    bowtie2-build binfantisgenomes.fna binfantis

#Define BOWTIE2_INDEXES directory and move the database files into it
    export BOWTIE2_INDEXES=/augusta/students/aditi/binfantisgenomes
    cp *.bt2 $BOWTIE2_INDEXES

#code for running bowtie2
    bowtie2 -x binfantis -U acc_list_file.fastq --no-unal -p 12 -S Metagenome1_bowtie2.sam

#Need to write a run_bowtie2(query, db, out) function
def run_bowtie2(query, db, out):
    for acc_list in query:
        metagenome = get_metagenomes(acc_list=)
        metagenomefile = group_metagenomes(metagenome)



if __name__=="__main__":
    import sys
    with open(sys.argv[1]) as io:
        acc_list_file = io.read().splitlines()

    get_metagenomes(acc_list_file=)
    group_metagenomes(sys.argv[2])
    run_blast(sys.argv[3], sys.argv[2], sys.argv[4])
