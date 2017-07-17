
import sys
import collections

import itertools

import random

import encoding4NN
import mix_false_true_to_one


# inputfilename1=./splice_site_dataset/splice.train-false.A outputbase= flag=1 phase=0 csize=1 specialbreak=yes






#############The below parameters are for the data set of benchmark.

allparameters=[
	[
		['./splice_site_dataset/splice.train-false.D','','entropy','all',2,'no','yes'],
		['./splice_site_dataset/splice.test-false.D','','entropy','all',2,'no','yes'],
		['./splice_site_dataset/splice.train-real.D','','entropy','all',2,'no','yes'],	
		['./splice_site_dataset/splice.test-real.D','','entropy','all',2,'no','yes']
	],

	[
	['./splice_site_dataset/splice.train-false.D','','enthalpy','all',2,'no','yes'],
	['./splice_site_dataset/splice.test-false.D','','enthalpy','all',2,'no','yes'],
	['./splice_site_dataset/splice.train-real.D','','enthalpy','all',2,'no','yes'],	
	['./splice_site_dataset/splice.test-real.D','','enthalpy','all',2,'no','yes']
	],		
	
	[
	['./splice_site_dataset/splice.train-false.D','','EIIP','0',1,'no','yes'],
	['./splice_site_dataset/splice.test-false.D','','EIIP','0',1,'no','yes'],
	['./splice_site_dataset/splice.train-real.D','','EIIP','0',1,'no','yes'],	
	['./splice_site_dataset/splice.test-real.D','','EIIP','0',1,'no','yes']	
	],
	
	[
	['./splice_site_dataset/splice.train-false.D','','1','0',1,'no','yes'],
	['./splice_site_dataset/splice.test-false.D','','1','0',1,'no','yes'],
	['./splice_site_dataset/splice.train-real.D','','1','0',1,'no','yes'],	
	['./splice_site_dataset/splice.test-real.D','','1','0',1,'no','yes']	
	],

	[
	['./splice_site_dataset/splice.train-false.D','','complementary','0',1,'no','yes'],
	['./splice_site_dataset/splice.test-false.D','','complementary','0',1,'no','yes'],
	['./splice_site_dataset/splice.train-real.D','','complementary','0',1,'no','yes'],	
	['./splice_site_dataset/splice.test-real.D','','complementary','0',1,'no','yes']	
	],	

	[
	['./splice_site_dataset/splice.train-false.D','','arbitary','0',1,'no','yes'],
	['./splice_site_dataset/splice.test-false.D','','arbitary','0',1,'no','yes'],
	['./splice_site_dataset/splice.train-real.D','','arbitary','0',1,'no','yes'],	
	['./splice_site_dataset/splice.test-real.D','','arbitary','0',1,'no','yes']	
	],
	
	[
	['./splice_site_dataset/splice.train-false.D','','stati2','all',2,'no','yes'],
	['./splice_site_dataset/splice.test-false.D','','stati2','all',2,'no','yes'],
	['./splice_site_dataset/splice.train-real.D','','stati2','all',2,'no','yes'],	
	['./splice_site_dataset/splice.test-real.D','','stati2','all',2,'no','yes']	
	],	

	[
	['./splice_site_dataset/splice.train-false.D','','neural','0',1,'no','yes'],
	['./splice_site_dataset/splice.test-false.D','','neural','0',1,'no','yes'],
	['./splice_site_dataset/splice.train-real.D','','neural','0',1,'no','yes'],	
	['./splice_site_dataset/splice.test-real.D','','neural','0',1,'no','yes']	
	],	

	[
	['./splice_site_dataset/splice.train-false.D','','galois2','all',2,'no','yes'],
	['./splice_site_dataset/splice.test-false.D','','galois2','all',2,'no','yes'],
	['./splice_site_dataset/splice.train-real.D','','galois2','all',2,'no','yes'],	
	['./splice_site_dataset/splice.test-real.D','','galois2','all',2,'no','yes']	
	],	

	
	[
		['./splice_site_dataset/splice.train-false.A','','entropy','all',2,'no','yes'],
		['./splice_site_dataset/splice.test-false.A','','entropy','all',2,'no','yes'],
		['./splice_site_dataset/splice.train-real.A','','entropy','all',2,'no','yes'],	
		['./splice_site_dataset/splice.test-real.A','','entropy','all',2,'no','yes']
	],

	[
	['./splice_site_dataset/splice.train-false.A','','enthalpy','all',2,'no','yes'],
	['./splice_site_dataset/splice.test-false.A','','enthalpy','all',2,'no','yes'],
	['./splice_site_dataset/splice.train-real.A','','enthalpy','all',2,'no','yes'],	
	['./splice_site_dataset/splice.test-real.A','','enthalpy','all',2,'no','yes']
	],		
	
	[
	['./splice_site_dataset/splice.train-false.A','','EIIP','0',1,'no','yes'],
	['./splice_site_dataset/splice.test-false.A','','EIIP','0',1,'no','yes'],
	['./splice_site_dataset/splice.train-real.A','','EIIP','0',1,'no','yes'],	
	['./splice_site_dataset/splice.test-real.A','','EIIP','0',1,'no','yes']	
	],
	
	[
	['./splice_site_dataset/splice.train-false.A','','1','0',1,'no','yes'],
	['./splice_site_dataset/splice.test-false.A','','1','0',1,'no','yes'],
	['./splice_site_dataset/splice.train-real.A','','1','0',1,'no','yes'],	
	['./splice_site_dataset/splice.test-real.A','','1','0',1,'no','yes']	
	],

	[
	['./splice_site_dataset/splice.train-false.A','','complementary','0',1,'no','yes'],
	['./splice_site_dataset/splice.test-false.A','','complementary','0',1,'no','yes'],
	['./splice_site_dataset/splice.train-real.A','','complementary','0',1,'no','yes'],	
	['./splice_site_dataset/splice.test-real.A','','complementary','0',1,'no','yes']	
	],

	[
	['./splice_site_dataset/splice.train-false.A','','arbitary','0',1,'no','yes'],
	['./splice_site_dataset/splice.test-false.A','','arbitary','0',1,'no','yes'],
	['./splice_site_dataset/splice.train-real.A','','arbitary','0',1,'no','yes'],	
	['./splice_site_dataset/splice.test-real.A','','arbitary','0',1,'no','yes']	
	],
	
	[
	['./splice_site_dataset/splice.train-false.A','','stati2','all',2,'no','yes'],
	['./splice_site_dataset/splice.test-false.A','','stati2','all',2,'no','yes'],
	['./splice_site_dataset/splice.train-real.A','','stati2','all',2,'no','yes'],	
	['./splice_site_dataset/splice.test-real.A','','stati2','all',2,'no','yes']	
	],
	
	[
	['./splice_site_dataset/splice.train-false.A','','neural','0',1,'no','yes'],
	['./splice_site_dataset/splice.test-false.A','','neural','0',1,'no','yes'],
	['./splice_site_dataset/splice.train-real.A','','neural','0',1,'no','yes'],	
	['./splice_site_dataset/splice.test-real.A','','neural','0',1,'no','yes']	
	],

	[
	['./splice_site_dataset/splice.train-false.A','','galois2','all',2,'no','yes'],
	['./splice_site_dataset/splice.test-false.A','','galois2','all',2,'no','yes'],
	['./splice_site_dataset/splice.train-real.A','','galois2','all',2,'no','yes'],	
	['./splice_site_dataset/splice.test-real.A','','galois2','all',2,'no','yes']	
	]	
		
]



####ncrna transcript and gene
'''
allparameters=[
	[
		['./splice_site_dataset/gene_ncrna_splicing_site/chr1-10_false_nc_A.fasta','','entropy','all',2,'no','yes'],
		['./splice_site_dataset/gene_ncrna_splicing_site/chr11-22_false_nc_A.fasta','','entropy','all',2,'no','yes'],
		['./splice_site_dataset/gene_ncrna_splicing_site/chr21_real_gene_A.fasta','','entropy','all',2,'no','yes'],	
		['./splice_site_dataset/gene_ncrna_splicing_site/chr22_real_gene_A.fasta','','entropy','all',2,'no','yes']
	],

	[
	['./splice_site_dataset/gene_ncrna_splicing_site/chr1-10_false_nc_A.fasta','','enthalpy','all',2,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr11-22_false_nc_A.fasta','','enthalpy','all',2,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr21_real_gene_A.fasta','','enthalpy','all',2,'no','yes'],	
	['./splice_site_dataset/gene_ncrna_splicing_site/chr22_real_gene_A.fasta','','enthalpy','all',2,'no','yes']
	],		
	
	[
	['./splice_site_dataset/gene_ncrna_splicing_site/chr1-10_false_nc_A.fasta','','EIIP','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr11-22_false_nc_A.fasta','','EIIP','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr21_real_gene_A.fasta','','EIIP','0',1,'no','yes'],	
	['./splice_site_dataset/gene_ncrna_splicing_site/chr22_real_gene_A.fasta','','EIIP','0',1,'no','yes']	
	],
	
	[
	['./splice_site_dataset/gene_ncrna_splicing_site/chr1-10_false_nc_A.fasta','','1','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr11-22_false_nc_A.fasta','','1','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr21_real_gene_A.fasta','','1','0',1,'no','yes'],	
	['./splice_site_dataset/gene_ncrna_splicing_site/chr22_real_gene_A.fasta','','1','0',1,'no','yes']	
	],

	[
	['./splice_site_dataset/gene_ncrna_splicing_site/chr1-10_false_nc_A.fasta','','complementary','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr11-22_false_nc_A.fasta','','complementary','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr21_real_gene_A.fasta','','complementary','0',1,'no','yes'],	
	['./splice_site_dataset/gene_ncrna_splicing_site/chr22_real_gene_A.fasta','','complementary','0',1,'no','yes']	
	],	

	[
	['./splice_site_dataset/gene_ncrna_splicing_site/chr1-10_false_nc_A.fasta','','arbitary','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr11-22_false_nc_A.fasta','','arbitary','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr21_real_gene_A.fasta','','arbitary','0',1,'no','yes'],	
	['./splice_site_dataset/gene_ncrna_splicing_site/chr22_real_gene_A.fasta','','arbitary','0',1,'no','yes']	
	],
	
	[
	['./splice_site_dataset/gene_ncrna_splicing_site/chr1-10_false_nc_A.fasta','','stati2','all',2,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr11-22_false_nc_A.fasta','','stati2','all',2,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr21_real_gene_A.fasta','','stati2','all',2,'no','yes'],	
	['./splice_site_dataset/gene_ncrna_splicing_site/chr22_real_gene_A.fasta','','stati2','all',2,'no','yes']	
	],	

	[
	['./splice_site_dataset/gene_ncrna_splicing_site/chr1-10_false_nc_A.fasta','','neural','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr11-22_false_nc_A.fasta','','neural','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr21_real_gene_A.fasta','','neural','0',1,'no','yes'],	
	['./splice_site_dataset/gene_ncrna_splicing_site/chr22_real_gene_A.fasta','','neural','0',1,'no','yes']	
	],	

	[
	['./splice_site_dataset/gene_ncrna_splicing_site/chr1-10_false_nc_A.fasta','','galois2','all',2,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr11-22_false_nc_A.fasta','','galois2','all',2,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr21_real_gene_A.fasta','','galois2','all',2,'no','yes'],	
	['./splice_site_dataset/gene_ncrna_splicing_site/chr22_real_gene_A.fasta','','galois2','all',2,'no','yes']	
	],	

	
	[
		['./splice_site_dataset/gene_ncrna_splicing_site/chr1-10_false_nc_D.fasta','','entropy','all',2,'no','yes'],
		['./splice_site_dataset/gene_ncrna_splicing_site/chr11-22_false_nc_D.fasta','','entropy','all',2,'no','yes'],
		['./splice_site_dataset/gene_ncrna_splicing_site/chr21_real_gene_D.fasta','','entropy','all',2,'no','yes'],	
		['./splice_site_dataset/gene_ncrna_splicing_site/chr22_real_gene_D.fasta','','entropy','all',2,'no','yes']
	],

	[
	['./splice_site_dataset/gene_ncrna_splicing_site/chr1-10_false_nc_D.fasta','','enthalpy','all',2,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr11-22_false_nc_D.fasta','','enthalpy','all',2,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr21_real_gene_D.fasta','','enthalpy','all',2,'no','yes'],	
	['./splice_site_dataset/gene_ncrna_splicing_site/chr22_real_gene_D.fasta','','enthalpy','all',2,'no','yes']
	],		
	
	[
	['./splice_site_dataset/gene_ncrna_splicing_site/chr1-10_false_nc_D.fasta','','EIIP','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr11-22_false_nc_D.fasta','','EIIP','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr21_real_gene_D.fasta','','EIIP','0',1,'no','yes'],	
	['./splice_site_dataset/gene_ncrna_splicing_site/chr22_real_gene_D.fasta','','EIIP','0',1,'no','yes']	
	],
	
	[
	['./splice_site_dataset/gene_ncrna_splicing_site/chr1-10_false_nc_D.fasta','','1','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr11-22_false_nc_D.fasta','','1','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr21_real_gene_D.fasta','','1','0',1,'no','yes'],	
	['./splice_site_dataset/gene_ncrna_splicing_site/chr22_real_gene_D.fasta','','1','0',1,'no','yes']	
	],

	[
	['./splice_site_dataset/gene_ncrna_splicing_site/chr1-10_false_nc_D.fasta','','complementary','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr11-22_false_nc_D.fasta','','complementary','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr21_real_gene_D.fasta','','complementary','0',1,'no','yes'],	
	['./splice_site_dataset/gene_ncrna_splicing_site/chr22_real_gene_D.fasta','','complementary','0',1,'no','yes']	
	],

	[
	['./splice_site_dataset/gene_ncrna_splicing_site/chr1-10_false_nc_D.fasta','','arbitary','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr11-22_false_nc_D.fasta','','arbitary','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr21_real_gene_D.fasta','','arbitary','0',1,'no','yes'],	
	['./splice_site_dataset/gene_ncrna_splicing_site/chr22_real_gene_D.fasta','','arbitary','0',1,'no','yes']	
	],
	
	[
	['./splice_site_dataset/gene_ncrna_splicing_site/chr1-10_false_nc_D.fasta','','stati2','all',2,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr11-22_false_nc_D.fasta','','stati2','all',2,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr21_real_gene_D.fasta','','stati2','all',2,'no','yes'],	
	['./splice_site_dataset/gene_ncrna_splicing_site/chr22_real_gene_D.fasta','','stati2','all',2,'no','yes']	
	],
	
	[
	['./splice_site_dataset/gene_ncrna_splicing_site/chr1-10_false_nc_D.fasta','','neural','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr11-22_false_nc_D.fasta','','neural','0',1,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr21_real_gene_D.fasta','','neural','0',1,'no','yes'],	
	['./splice_site_dataset/gene_ncrna_splicing_site/chr22_real_gene_D.fasta','','neural','0',1,'no','yes']	
	],

	[
	['./splice_site_dataset/gene_ncrna_splicing_site/chr1-10_false_nc_D.fasta','','galois2','all',2,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr11-22_false_nc_D.fasta','','galois2','all',2,'no','yes'],
	['./splice_site_dataset/gene_ncrna_splicing_site/chr21_real_gene_D.fasta','','galois2','all',2,'no','yes'],	
	['./splice_site_dataset/gene_ncrna_splicing_site/chr22_real_gene_D.fasta','','galois2','all',2,'no','yes']	
	]	
		
]	
'''	



''' 
#The below is the ncRNA non transcript and gene
allparameters=[
	[
		['./splice_site_dataset/gene_nctr_splicing_site/chr21_false_nctr_A.fasta','','entropy','all',2,'no','yes'],
		['./splice_site_dataset/gene_nctr_splicing_site/chr22_false_nctr_A.fasta','','entropy','all',2,'no','yes'],
		['./splice_site_dataset/gene_nctr_splicing_site/chr21_real_gene_A.fasta','','entropy','all',2,'no','yes'],	
		['./splice_site_dataset/gene_nctr_splicing_site/chr22_real_gene_A.fasta','','entropy','all',2,'no','yes']
	],

	[
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_false_nctr_A.fasta','','enthalpy','all',2,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_false_nctr_A.fasta','','enthalpy','all',2,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_real_gene_A.fasta','','enthalpy','all',2,'no','yes'],	
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_real_gene_A.fasta','','enthalpy','all',2,'no','yes']
	],		
	
	[
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_false_nctr_A.fasta','','EIIP','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_false_nctr_A.fasta','','EIIP','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_real_gene_A.fasta','','EIIP','0',1,'no','yes'],	
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_real_gene_A.fasta','','EIIP','0',1,'no','yes']	
	],
	
	[
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_false_nctr_A.fasta','','1','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_false_nctr_A.fasta','','1','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_real_gene_A.fasta','','1','0',1,'no','yes'],	
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_real_gene_A.fasta','','1','0',1,'no','yes']	
	],

	[
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_false_nctr_A.fasta','','complementary','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_false_nctr_A.fasta','','complementary','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_real_gene_A.fasta','','complementary','0',1,'no','yes'],	
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_real_gene_A.fasta','','complementary','0',1,'no','yes']	
	],	

	[
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_false_nctr_A.fasta','','arbitary','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_false_nctr_A.fasta','','arbitary','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_real_gene_A.fasta','','arbitary','0',1,'no','yes'],	
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_real_gene_A.fasta','','arbitary','0',1,'no','yes']	
	],
	
	[
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_false_nctr_A.fasta','','stati2','all',2,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_false_nctr_A.fasta','','stati2','all',2,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_real_gene_A.fasta','','stati2','all',2,'no','yes'],	
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_real_gene_A.fasta','','stati2','all',2,'no','yes']	
	],	

	[
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_false_nctr_A.fasta','','neural','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_false_nctr_A.fasta','','neural','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_real_gene_A.fasta','','neural','0',1,'no','yes'],	
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_real_gene_A.fasta','','neural','0',1,'no','yes']	
	],	

	[
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_false_nctr_A.fasta','','galois2','all',2,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_false_nctr_A.fasta','','galois2','all',2,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_real_gene_A.fasta','','galois2','all',2,'no','yes'],	
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_real_gene_A.fasta','','galois2','all',2,'no','yes']	
	],	

	
	[
		['./splice_site_dataset/gene_nctr_splicing_site/chr21_false_nctr_D.fasta','','entropy','all',2,'no','yes'],
		['./splice_site_dataset/gene_nctr_splicing_site/chr22_false_nctr_D.fasta','','entropy','all',2,'no','yes'],
		['./splice_site_dataset/gene_nctr_splicing_site/chr21_real_gene_D.fasta','','entropy','all',2,'no','yes'],	
		['./splice_site_dataset/gene_nctr_splicing_site/chr22_real_gene_D.fasta','','entropy','all',2,'no','yes']
	],

	[
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_false_nctr_D.fasta','','enthalpy','all',2,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_false_nctr_D.fasta','','enthalpy','all',2,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_real_gene_D.fasta','','enthalpy','all',2,'no','yes'],	
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_real_gene_D.fasta','','enthalpy','all',2,'no','yes']
	],		
	
	[
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_false_nctr_D.fasta','','EIIP','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_false_nctr_D.fasta','','EIIP','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_real_gene_D.fasta','','EIIP','0',1,'no','yes'],	
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_real_gene_D.fasta','','EIIP','0',1,'no','yes']	
	],
	
	[
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_false_nctr_D.fasta','','1','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_false_nctr_D.fasta','','1','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_real_gene_D.fasta','','1','0',1,'no','yes'],	
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_real_gene_D.fasta','','1','0',1,'no','yes']	
	],

	[
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_false_nctr_D.fasta','','complementary','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_false_nctr_D.fasta','','complementary','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_real_gene_D.fasta','','complementary','0',1,'no','yes'],	
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_real_gene_D.fasta','','complementary','0',1,'no','yes']	
	],

	[
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_false_nctr_D.fasta','','arbitary','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_false_nctr_D.fasta','','arbitary','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_real_gene_D.fasta','','arbitary','0',1,'no','yes'],	
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_real_gene_D.fasta','','arbitary','0',1,'no','yes']	
	],
	
	[
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_false_nctr_D.fasta','','stati2','all',2,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_false_nctr_D.fasta','','stati2','all',2,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_real_gene_D.fasta','','stati2','all',2,'no','yes'],	
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_real_gene_D.fasta','','stati2','all',2,'no','yes']	
	],
	
	[
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_false_nctr_D.fasta','','neural','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_false_nctr_D.fasta','','neural','0',1,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_real_gene_D.fasta','','neural','0',1,'no','yes'],	
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_real_gene_D.fasta','','neural','0',1,'no','yes']	
	],

	[
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_false_nctr_D.fasta','','galois2','all',2,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_false_nctr_D.fasta','','galois2','all',2,'no','yes'],
	['./splice_site_dataset/gene_nctr_splicing_site/chr21_real_gene_D.fasta','','galois2','all',2,'no','yes'],	
	['./splice_site_dataset/gene_nctr_splicing_site/chr22_real_gene_D.fasta','','galois2','all',2,'no','yes']	
	]	
		
]
'''


'''
#The below is for ncRNA's transcription and non-transcript

allparameters=[
	[
		['./splice_site_dataset/ncrna_notran_splicing_site/chr21_false_nc_A.fasta','','entropy','all',2,'no','yes'],
		['./splice_site_dataset/ncrna_notran_splicing_site/chr22_false_nc_A.fasta','','entropy','all',2,'no','yes'],
		['./splice_site_dataset/ncrna_notran_splicing_site/chr1-10_real_nctr_A.fasta','','entropy','all',2,'no','yes'],	
		['./splice_site_dataset/ncrna_notran_splicing_site/chr11-22_real_nctr_A.fasta','','entropy','all',2,'no','yes']
	],

	[
	['./splice_site_dataset/ncrna_notran_splicing_site/chr21_false_nc_A.fasta','','enthalpy','all',2,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr22_false_nc_A.fasta','','enthalpy','all',2,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr1-10_real_nctr_A.fasta','','enthalpy','all',2,'no','yes'],	
	['./splice_site_dataset/ncrna_notran_splicing_site/chr11-22_real_nctr_A.fasta','','enthalpy','all',2,'no','yes']
	],		
	
	[
	['./splice_site_dataset/ncrna_notran_splicing_site/chr21_false_nc_A.fasta','','EIIP','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr22_false_nc_A.fasta','','EIIP','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr1-10_real_nctr_A.fasta','','EIIP','0',1,'no','yes'],	
	['./splice_site_dataset/ncrna_notran_splicing_site/chr11-22_real_nctr_A.fasta','','EIIP','0',1,'no','yes']	
	],
	
	[
	['./splice_site_dataset/ncrna_notran_splicing_site/chr21_false_nc_A.fasta','','1','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr22_false_nc_A.fasta','','1','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr1-10_real_nctr_A.fasta','','1','0',1,'no','yes'],	
	['./splice_site_dataset/ncrna_notran_splicing_site/chr11-22_real_nctr_A.fasta','','1','0',1,'no','yes']	
	],

	[
	['./splice_site_dataset/ncrna_notran_splicing_site/chr21_false_nc_A.fasta','','complementary','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr22_false_nc_A.fasta','','complementary','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr1-10_real_nctr_A.fasta','','complementary','0',1,'no','yes'],	
	['./splice_site_dataset/ncrna_notran_splicing_site/chr11-22_real_nctr_A.fasta','','complementary','0',1,'no','yes']	
	],	

	[
	['./splice_site_dataset/ncrna_notran_splicing_site/chr21_false_nc_A.fasta','','arbitary','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr22_false_nc_A.fasta','','arbitary','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr1-10_real_nctr_A.fasta','','arbitary','0',1,'no','yes'],	
	['./splice_site_dataset/ncrna_notran_splicing_site/chr11-22_real_nctr_A.fasta','','arbitary','0',1,'no','yes']	
	],
	
	[
	['./splice_site_dataset/ncrna_notran_splicing_site/chr21_false_nc_A.fasta','','stati2','all',2,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr22_false_nc_A.fasta','','stati2','all',2,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr1-10_real_nctr_A.fasta','','stati2','all',2,'no','yes'],	
	['./splice_site_dataset/ncrna_notran_splicing_site/chr11-22_real_nctr_A.fasta','','stati2','all',2,'no','yes']	
	],	

	[
	['./splice_site_dataset/ncrna_notran_splicing_site/chr21_false_nc_A.fasta','','neural','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr22_false_nc_A.fasta','','neural','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr1-10_real_nctr_A.fasta','','neural','0',1,'no','yes'],	
	['./splice_site_dataset/ncrna_notran_splicing_site/chr11-22_real_nctr_A.fasta','','neural','0',1,'no','yes']	
	],	

	[
	['./splice_site_dataset/ncrna_notran_splicing_site/chr21_false_nc_A.fasta','','galois2','all',2,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr22_false_nc_A.fasta','','galois2','all',2,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr1-10_real_nctr_A.fasta','','galois2','all',2,'no','yes'],	
	['./splice_site_dataset/ncrna_notran_splicing_site/chr11-22_real_nctr_A.fasta','','galois2','all',2,'no','yes']	
	],	

	
	[
		['./splice_site_dataset/ncrna_notran_splicing_site/chr21_false_nc_D.fasta','','entropy','all',2,'no','yes'],
		['./splice_site_dataset/ncrna_notran_splicing_site/chr22_false_nc_D.fasta','','entropy','all',2,'no','yes'],
		['./splice_site_dataset/ncrna_notran_splicing_site/chr1-10_real_nctr_D.fasta','','entropy','all',2,'no','yes'],	
		['./splice_site_dataset/ncrna_notran_splicing_site/chr11-22_real_nctr_D.fasta','','entropy','all',2,'no','yes']
	],

	[
	['./splice_site_dataset/ncrna_notran_splicing_site/chr21_false_nc_D.fasta','','enthalpy','all',2,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr22_false_nc_D.fasta','','enthalpy','all',2,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr1-10_real_nctr_D.fasta','','enthalpy','all',2,'no','yes'],	
	['./splice_site_dataset/ncrna_notran_splicing_site/chr11-22_real_nctr_D.fasta','','enthalpy','all',2,'no','yes']
	],		
	
	[
	['./splice_site_dataset/ncrna_notran_splicing_site/chr21_false_nc_D.fasta','','EIIP','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr22_false_nc_D.fasta','','EIIP','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr1-10_real_nctr_D.fasta','','EIIP','0',1,'no','yes'],	
	['./splice_site_dataset/ncrna_notran_splicing_site/chr11-22_real_nctr_D.fasta','','EIIP','0',1,'no','yes']	
	],
	
	[
	['./splice_site_dataset/ncrna_notran_splicing_site/chr21_false_nc_D.fasta','','1','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr22_false_nc_D.fasta','','1','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr1-10_real_nctr_D.fasta','','1','0',1,'no','yes'],	
	['./splice_site_dataset/ncrna_notran_splicing_site/chr11-22_real_nctr_D.fasta','','1','0',1,'no','yes']	
	],

	[
	['./splice_site_dataset/ncrna_notran_splicing_site/chr21_false_nc_D.fasta','','complementary','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr22_false_nc_D.fasta','','complementary','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr1-10_real_nctr_D.fasta','','complementary','0',1,'no','yes'],	
	['./splice_site_dataset/ncrna_notran_splicing_site/chr11-22_real_nctr_D.fasta','','complementary','0',1,'no','yes']	
	],

	[
	['./splice_site_dataset/ncrna_notran_splicing_site/chr21_false_nc_D.fasta','','arbitary','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr22_false_nc_D.fasta','','arbitary','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr1-10_real_nctr_D.fasta','','arbitary','0',1,'no','yes'],	
	['./splice_site_dataset/ncrna_notran_splicing_site/chr11-22_real_nctr_D.fasta','','arbitary','0',1,'no','yes']	
	],
	
	[
	['./splice_site_dataset/ncrna_notran_splicing_site/chr21_false_nc_D.fasta','','stati2','all',2,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr22_false_nc_D.fasta','','stati2','all',2,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr1-10_real_nctr_D.fasta','','stati2','all',2,'no','yes'],	
	['./splice_site_dataset/ncrna_notran_splicing_site/chr11-22_real_nctr_D.fasta','','stati2','all',2,'no','yes']	
	],
	
	[
	['./splice_site_dataset/ncrna_notran_splicing_site/chr21_false_nc_D.fasta','','neural','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr22_false_nc_D.fasta','','neural','0',1,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr1-10_real_nctr_D.fasta','','neural','0',1,'no','yes'],	
	['./splice_site_dataset/ncrna_notran_splicing_site/chr11-22_real_nctr_D.fasta','','neural','0',1,'no','yes']	
	],

	[
	['./splice_site_dataset/ncrna_notran_splicing_site/chr21_false_nc_D.fasta','','galois2','all',2,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr22_false_nc_D.fasta','','galois2','all',2,'no','yes'],
	['./splice_site_dataset/ncrna_notran_splicing_site/chr1-10_real_nctr_D.fasta','','galois2','all',2,'no','yes'],	
	['./splice_site_dataset/ncrna_notran_splicing_site/chr11-22_real_nctr_D.fasta','','galois2','all',2,'no','yes']	
	]	
		
]

'''













#### for gene & nc non-transcript
#outputbase = './splice_site_dataset/gene_nctr_splicing_site/';	#base of output file and path.

#### for gene & ncRNA transcript
#outputbase = './splice_site_dataset/gene_ncrna_splicing_site/';	#base of output file and path.

#outputbase = './splice_site_dataset/ncrna_notran_splicing_site/';	#base of output file and path.

def procedures(parameters, outputbase): 

	file_names = [];

	for par in parameters:
		str = par[0].split('/');
		file_names.append(str[-1]);
		
	print file_names;


	outputfiles = [];
	##########################################
	#step 1: encode each sequence file into a file.
	#
	#
	##########################################
	#generate/encode sequences and write intermediate files (encoded files) and return the written file names.
	for par in parameters:
		outputfiles.append(encoding4NN.encode_fasta2NN_input(par));
	print outputfiles;



	##########################################
	#step 2: merge the first two files into one file.
	#
	#
	##########################################

	outputfilename1 = '{}{}_{}_{}'.format(outputbase,file_names[0],file_names[1],parameters[0][2]);
	houtputfile1 = open(outputfilename1,'wb+');
	for filename in outputfiles[0:2]:
		with open(filename) as file:
			contents = file.read()
			houtputfile1.write(contents);
	houtputfile1.close();		


	#merge the rest two files into one file.
	outputfilename2 = '{}{}_{}_{}'.format(outputbase,file_names[2],file_names[3],parameters[0][2]);
	houtputfile2 = open(outputfilename2,'wb+');
	for filename in outputfiles[2:]:
		with open(filename) as file:
			contents = file.read()
			houtputfile2.write(contents);
	houtputfile2.close();


	##########################################
	#step 3: merge two files (false and real) into a mixed file.
	#
	# python mix_false_true_to_one.py inputfilename1=splice.train-real.A_splice.test-real.A  inputfilename2=splice.train-false.A_splice.test-false.A inputbase=./splice_site_dataset/ outputbase=splice_site_dataset/
	##########################################
	filename1 = '{}_{}_{}'.format(file_names[0],file_names[1],parameters[0][2]);
	filename2 = '{}_{}_{}'.format(file_names[2],file_names[3],parameters[0][2]);

	print filename1, filename2;

	mix_false_true_to_one.mergeNN_false_true([filename1,filename2,outputbase,outputbase,parameters[0][2]]);


################################commandline usage#################
#python encoding_allfasta.py specify=complementary outputbase=./splice_site_dataset/
#or 
#python encoding_allfasta.py
#################################################################	
	

if __name__ == '__main__':	
	#outputbase = './';	#base of output file and path.
	
	specify = '';
	for rawstr in sys.argv:
		names = rawstr.split("=");
		if 'outputbase' in rawstr:
			outputbase = names[1]; #input genome file1 fasta
		elif 'specify' in rawstr:
			specify = names[1];
	
	if specify == '':
		for parameters in allparameters:
			procedures(parameters,outputbase);
	else:
		for parameters in allparameters:
			#if specified one is the type listed, then do the specified one.
			if specify == parameters[0][2]:
				procedures(parameters,outputbase);
		