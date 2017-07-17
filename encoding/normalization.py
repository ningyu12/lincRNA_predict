import sys

import collections

import itertools

import random

import encoding4NN

import mix_false_true_to_one

import numpy as np


#originalfilename = "splice.train-false.A_splice.test-false.A_complementary_splice.train-real.A_splice.test-real.A_complementary.txt";
#originalfilename = "splice.train-false.A_splice.test-false.A_neural_splice.train-real.A_splice.test-real.A_neural.txt"
#originalfilename = "splice.train-false.A_splice.test-false.A_arbitary_splice.train-real.A_splice.test-real.A_arbitary.txt"
#originalfilename = "splice.train-false.A_splice.test-false.A_1_splice.train-real.A_splice.test-real.A_1.txt"
#originalfilename = "splice.train-false.A_splice.test-false.A_EIIP_splice.train-real.A_splice.test-real.A_EIIP.txt"

#originalfilename = "splice.train-false.A_splice.test-false.A_galois2_splice.train-real.A_splice.test-real.A_galois2.txt"
#originalfilename = "splice.train-false.A_splice.test-false.A_stati2_splice.train-real.A_splice.test-real.A_stati2.txt"
#originalfilename = "splice.train-false.A_splice.test-false.A_enthalpy_splice.train-real.A_splice.test-real.A_enthalpy.txt"
#originalfilename = "splice.train-false.A_splice.test-false.A_entropy_splice.train-real.A_splice.test-real.A_entropy.txt"


#originalfilename = "splice.train-false.D_splice.test-false.D_complementary_splice.train-real.D_splice.test-real.D_complementary.txt";
#originalfilename = "splice.train-false.D_splice.test-false.D_neural_splice.train-real.D_splice.test-real.D_neural.txt"
#originalfilename = "splice.train-false.D_splice.test-false.D_arbitary_splice.train-real.D_splice.test-real.D_arbitary.txt"
#originalfilename = "splice.train-false.D_splice.test-false.D_1_splice.train-real.D_splice.test-real.D_1.txt"
#originalfilename = "splice.train-false.D_splice.test-false.D_EIIP_splice.train-real.D_splice.test-real.D_EIIP.txt"

#originalfilename = "splice.train-false.D_splice.test-false.D_galois2_splice.train-real.D_splice.test-real.D_galois2.txt"
#originalfilename = "splice.train-false.D_splice.test-false.D_stati2_splice.train-real.D_splice.test-real.D_stati2.txt"
#originalfilename = "splice.train-false.D_splice.test-false.D_enthalpy_splice.train-real.D_splice.test-real.D_enthalpy.txt"
originalfilename = "splice.train-false.D_splice.test-false.D_entropy_splice.train-real.D_splice.test-real.D_entropy.txt"


originalfolder = 'splice_site_dataset/';
savedfolder = 'results-normal/';



originalfile = originalfolder + originalfilename;

colnum = 90;
if 'D' in originalfilename:
	colnum = 15;
	if '2' in originalfilename:
		colnum = 14;
	elif 'ent' in originalfilename:
		colnum = 14;	
elif 'A' in originalfilename:
	colnum = 90;
	if '2' in originalfilename:
		colnum = 89;
	elif 'ent' in originalfilename:
		colnum = 89;
else:
	print 'A, D is not here';
	exit(-1);

savedfilename = originalfilename.split("-")[0]+'.'+originalfilename.split(".")[-2]+'.z.txt';

savedfile = savedfolder+savedfilename;

print savedfilename, colnum;

#matMad = np.mean( np.abs( np.tile( np.mean( a, axis=1 ), ( 1, a.shape[1] ) ) - a ), axis=1 )

#print matMad;

#vertical mean

#a = np.matrix( [[2,4,8,10],[2,1,2,3],[2,3,5,7]]);
#a = np.matrix( [ [ 80, 76, 77, 78, 79, 81, 76, 77, 79, 84, 75, 79, 76, 78 ], [ 66, 69, 76, 72, 79, 77, 74, 77, 71, 79, 74, 66, 67, 73 ],[ 60, 60, 70, 70, 70, 70, 70, 70, 70, 70, 70, 60, 60, 70 ] ], dtype=float ) 


originalfile = originalfolder+originalfilename;
a = np.loadtxt(originalfile, usecols=range(0,colnum));
print 'matrix a=',a;

b = np.loadtxt(originalfile, usecols=(colnum,));
print 'matrx b=', b;


print 'mean(a, axis=0):',np.mean( a, axis=0 );

print 'a.shape[0]=',a.shape[0];


matMean = np.tile( np.mean( a, axis=0 ), ( a.shape[0], 1 ) );

matMad = np.tile(np.mean( np.abs( matMean - a ), axis=0 ),( a.shape[0], 1 ));

print 'matrix of mean absolute deviation',matMad;

np.savetxt("results-normal/splice.train.Mad_complementary.txt",matMad);


zscore = np.around(np.nan_to_num((a - matMean)/matMad), decimals=3);

print 'zscore',zscore;

#z_b = np.c_[zscore,b]

#print 'z_b', z_b;

np.savetxt(savedfile,np.c_[zscore,b], fmt='%.3f');


