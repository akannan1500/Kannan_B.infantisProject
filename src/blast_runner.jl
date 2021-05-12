using BioSequences
using BioServices.EUtils
using DataFrames
using CSV

res = efetch(db="sra", id="SRR4408194", retmax=10)

res.data

1+1

`echo $PATH`