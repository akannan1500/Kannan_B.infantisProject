#!/usr/bin/env python
import re 
from collections import Counter

# ----------------USAGE-----------------------
# This script parses a BLAST alignment file created using output format 7 and returns 
# a tab-delimited text file with the number of total hits, multiply aligned hits, and 
# good quality hits (above a certain identity and length threshold) for every contig/gene 
# in the reference sequence database. 

def blast_scraper(infilename, identitythresh, lengththresh, countfilename, outfilename):
    # Opens an infile specified by the user. Should be a BLAST file 
    IN = open(infilename, 'r')
    text = open(infilename, 'r')

    identity=float(identitythresh) 
    length=float(lengththresh)

    # Opens an output text file specified by user 
    COUNT = open(countfilename, 'w')
    OUT = open(outfilename, 'w')

    # Find all BLAST hits in infile
    hit_list = re.findall('found(.*?)# BLAST', text.read(), re.S)
   
    hits_dict = {} # store hits to queries
    out_dict = {} # store hits to queries
    num_query = 0 # use to iterate through hit_list

    # Starts a for loop to read through the infile line by line
    for line in IN:
        if re.search("^# Query:", line): # if line with the BLAST query
            query = ':'.join([line.split(":")[1],line.split(":")[2].split()[0].strip()])
            hits_dict[query] = [0, 0, 0] # initialize all queries with 0 hits
            out_dict[query] = []

        if re.search("hits found$", line): # if line with the number of hits
            total_hits = line.split()[1].strip()
            hits_dict[query][0] = int(total_hits) # set total number of hits for a query

            hits = hit_list[num_query].split('\n')

            genomes = []
            quality_hits = 0
            for hit in hits:
                if hit.strip():
                    q, genome, iden, leng, mismatches, gaps, \
                    q_start, q_end, s_start, s_end, evalue, bit_score = hit.split()
                    
                    genomes.append(genome)

                    # Count number of quality hits for a query
                    if float(iden) >= identity and float(leng) >= length:
                        quality_hits += 1
            
            # Count number of multiple hits for a query
            multiples = [k for (k,v) in Counter(genomes).items() if v > 1]
            hits_dict[query][1] = len(multiples)
            
            hits_dict[query][2] = quality_hits

            # Store names of hits for a query
            out_dict[query] = genomes

            num_query += 1

             

    # Format dictionary data into a tab-delimited text file
    COUNT.write('Query'+'\t'+'Total Hits'+'\t'+'Multiple Hits'+'\t'+'Quality Hits')

    printed = []
    for key,value in hits_dict.items():
        printed.append((key,value))

    for item in printed:
        COUNT.write('\n%s\t%d\t%d\t%d' % (item[0], item[1][0], item[1][1], item[1][2]))
    
    # Format dictionary data into a tab-delimited text file
    OUT.write('Query'+'\t'+'Genome')
    printed = []

    for key,value in out_dict.items():
        printed.append((key,value))

    for item in printed:
        for genome in item[1]:
            OUT.write('\n%s\t%s' % (item[0], genome))

    COUNT.close()
    OUT.close()

if __name__=="__main__":
    import sys
    # Usage blast_scraper(infilename, identitythresh, lengththreshold, countfilename, outfilename)
    blast_scraper(sys.argv[3], sys.argv[1], sys.argv[2], sys.argv[3]+'_counts.txt', sys.argv[3]+'_names.txt')
