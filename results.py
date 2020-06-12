from Bio import SearchIO
import urllib.request
import os

cwd = os.getcwd()
tmpf = cwd + os.sep + 'tmp'+ os.sep
pdbf = cwd + os.sep + 'PDB-files' + os.sep
fstf = cwd + os.sep + 'FASTA-files' + os.sep
pdbd = 'http://files.rcsb.org/download/'

def results(results):
	with open(tmpf + "blastp.xml", "w") as out_handle:
		out_handle.write(results.read())
	out_handle.close()
	print('XML file created!')

	blast_qresult = SearchIO.read(tmpf + "blastp.xml", "blast-xml")
	res_lines = str(blast_qresult).split('\n')
	first_hit = res_lines[7]
	PDBid = first_hit[26:30]
	file = PDBid + '.pdb'
	print('Protein PDB id acquired!')

	url = pdbd + file
	urllib.request.urlretrieve(url, pdbf + file)
	print('PDB file downloaded!')

	os.startfile(pdbf + file)
	print('Protein 3D structure opened in PyMol!')
