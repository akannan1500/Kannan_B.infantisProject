using BioSequences
using BioServices.EUtils
using DataFrames
using CSV

res = efetch(db="sra", id="SRR4408194", retmode="xml")
using EzXML
doc = parsexml(res.data)

res.data

1+1

`echo $PATH`