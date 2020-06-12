import shutil
shutil.rmtree(cwd + os.sep + '__pycache__')

from results import *
print('Program sync completed!')

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
print('Modules imported!')

record = SeqIO.read(fstf + "2WFU_A.fasta", format="fasta")
print('Sequence read!')

print('Starting BLAST!')
result_handle = NCBIWWW.qblast("blastp", "pdb", record.seq)
print('BLAST done!')

results(result_handle)
