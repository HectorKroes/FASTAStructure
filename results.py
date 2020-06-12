from Bio import SearchIO
import urllib.request
import os

cwd = os.getcwd()
tmpf = cwd + os.sep + 'tmp'+ os.sep
pdbf = cwd + os.sep + 'PDB-files' + os.sep
fstf = cwd + os.sep + 'FASTA-files' + os.sep
pdbd = 'http://files.rcsb.org/download/'

def readxml(xmlfile):
	blast_qresult = SearchIO.read(xmlfile, "blast-xml")
	res_lines = str(blast_qresult).split('\n')
	first_hit = res_lines[7]
	PDBid = first_hit[26:30]
	file = PDBid + '.pdb'
	url = pdbd + file
	urllib.request.urlretrieve(url, pdbf + file)
	os.startfile(pdbf + file)

