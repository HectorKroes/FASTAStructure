from results import *
print('Program sync completed!')

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
print('Modules imported!')

record = SeqIO.read(fstf + "2WFU_A.fasta", format="fasta")
print('Sequence read!')

result_handle = NCBIWWW.qblast("blastp", "pdb", record.seq)
print('BLAST done!')

with open(tmpf + "blastp.xml", "w") as out_handle:
	out_handle.write(result_handle.read())
out_handle.close()
print('XML file created!')

readxml("blastp.xml")
