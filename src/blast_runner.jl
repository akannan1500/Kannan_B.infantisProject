using BioSequences
using BioServices.EUtils
using DataFrames
using CSV
using EzXML

function get_metagenomes(acc_list_file) #a function that will make a file for each accession number with the metagenome
    for acc in acc_list_file
        res = efetch(db="sra", id=acc, retmode="xml")
        doc = parsexml(res.data)
        
function get_genomes(acc_list) #a function that will get the genomes of B. infantis HMO degrading genes in a file
    for 

doc = parsexml(res.data)

res.data

1+1

`echo $PATH`