from Bio import Entrez
import subprocess

# ----------------------------------USAGE----------------------------------
# Hey Aditi! This python script should contain functions for setting up the 
# BLAST we were talking about. I wasn't able to test these functions without
# the metagenome accession numbers, but it should be close if not. Run the 
# file like this: 
# python blast_runner.py [list_of_accession_nums] [name_of_merged_mgx_file] [name_of_query_file] [name_of_blast_output_file]  
Entrez.email = "akannan2@wellesley.edu"
def get_metagenomes(acc_list):
    '''
        Get metagenomes from NCBI given a list of accession numbers
    '''
    for acc in acc_list:
        f = open("fastas/{}.fasta".format(acc), "a")
        seq = Entrez.efetch(db="SRA", id=acc, rettype="fasta")
        f.write(seq.read().strip().replace('\n', ''))
        f.close()

def group_metagenomes(out):
    '''
        Group metagenomes in one large fasta file
    '''
    subprocess.call(['cat', 'fastas/*.fasta', '>', '{}.fasta'.format(out)])

def run_blast(query, db, out):
    '''
        Run blastn of conserved genes against metagenomes
    '''
    subprocess.call(['makeblastdb', '-in', '{}'.format(db),
                     '-dbtype', "'nucl'", '-out', 'blast_{}'.format(db),
                     '-parse_seqids'])
    subprocess.call(['blastn', '-db', 'blast_{}'.format(db), 'query',
                     '{}'.format(query), '-out', '{}'.format(out), '-outfmt', '7'])

if __name__=="__main__":
    import sys
    with open(sys.argv[1]) as io:
        acc_list = io.read().splitlines()

    get_metagenomes(acc_list)
    group_metagenomes(sys.argv[2])
    run_blast(sys.argv[3], sys.argv[2], sys.argv[4])