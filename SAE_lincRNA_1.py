from keras.layers.core import Dense, AutoEncoder, Dropout, Activation                                                                                                                                                                  
#from keras.layers import containers                                                                                                                                                                                 
from keras.models import Sequential                                                                                                                                                                                                                                                                                                                                                                     
from keras.utils import np_utils  
import numpy as np
np.random.seed(1337)  
#np.random.seed(2355)                                                                                                                                                                                
from keras.optimizers import SGD
from load_gene_data import load_data

##########################
##"c:\users\Ning Yu\Documents\splicing-site-test\SAE_GENE_1.py"
#
##########################




#05/18/2017 for normalization:
#################################Notice:#############
########The below is for normalized standard benchmark dataset using z-score.

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/results-normal/splice.train.A_complementary.z.txt'
#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/results-normal/splice.train.A_arbitary.z.txt'
#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/results-normal/splice.train.A_EIIP.z.txt'
#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/results-normal/splice.train.A_neural.z.txt'
#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/results-normal/splice.train.A_1.z.txt'
#par=[0,5877,5877,6877,0,90];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/results-normal/splice.train.A_enthalpy.z.txt'
#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/results-normal/splice.train.A_entropy.z.txt'
#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/results-normal/splice.train.A_stati2.z.txt'
#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/results-normal/splice.train.A_galois2.z.txt'

#par=[0,5877,5877,6877,0,89];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/results-normal/splice.train.D_complementary.z.txt'
#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/results-normal/splice.train.D_arbitary.z.txt'
#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/results-normal/splice.train.D_EIIP.z.txt'
#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/results-normal/splice.train.D_neural.z.txt'
#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/results-normal/splice.train.D_1.z.txt'

#par=[0,5246,5246,6246,0,15];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/results-normal/splice.train.D_enthalpy.z.txt'
#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/results-normal/splice.train.D_entropy.z.txt'
#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/results-normal/splice.train.D_stati2.z.txt'
dataset='c:/Users/Ning Yu/Documents/splicing-site-test/results-normal/splice.train.D_galois2.z.txt'

par=[0,5246,5246,6246,0,14];







#################################Notice:#############
########The below is for lincRNA prediction.

###dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/concat_chr20_A_complementary-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
###par=[0,46982,46983,56571,0,90];

																									  
#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr1_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,101424,0,90];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr2_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,121990,0,90];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr3_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,97792,0,90];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr4_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,109564,0,90];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr5_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,103123,0,90];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr6_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,88107,0,90];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr7_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,88207,0,90];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr8_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,68337,0,90];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr9_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,80157,0,90];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr10_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,76278,0,90];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr11_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,62067,0,90];


##something in epoch 6-7, 5/23/2016.
#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr12_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,79450,0,90];


#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr13_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,69528,0,90];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr14_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,65850,0,90];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr15_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,74672,0,90];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr16_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,71645,0,90];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr17_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,65181,0,90];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr18_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,60826,0,90];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr19_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,61920,0,90];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/ncrna_notran_splicing_site/chr20_A.fasta_ph0.complementary.txt-ncRNA_trans_chr1-10_chr11-22_ncRNA_nctr_chr21_chr22_A.txt'
#par=[0,46982,46983,56571,0,90];




#par=[0,5787,5787,6877,0,89];

#dataset='c:\Users\Ning Yu\Documents\splicing-site-test\splice_site_dataset\standard_separate_traintest\concat_train_test_D.complementary.txt'
#par=[0,5255,5256,6246,0,15];







######Notice:
###The below is for synthisized data set.
#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/06.23.2015.c.AD/syn_gene_notr_06.23.2015.c/gene_notr_06.23.2015.c_A.txt'
#par=[0,40926,40926,54000,0,90];

#dataset='c:/Users/Ning Yu/Documents/splicing-site-test/splice_site_dataset/06.23.2015.c.AD/syn_gene_notr_06.23.2015.c/gene_notr_06.23.2015.c_D.txt'
#par=[0,90784,90784,99115,0,15];




#par = [start_train, stop_train, start_test, stop_test, start_col, stop_col]
##par=[0,5664,5664,6664,0,90];


#splice.train-false.A_splice.test-false.A_n_splice.train-real.A_splice.test-real.A.txt
(X_train, y_train), (X_test, y_test)= load_data(dataset, par) 


#pre_train_batch_size = 10		# 10 samples for a update.
#Pre_train_nb_epoch = 20			# train 20 iterations. 20 is better than 50.
#nb_classes = 2					# label 0 or 1.
#Fine_tune_batch_size = 25		# fine tune for update. 25 samples for a update
#Fine_tune_nb_epoch = 100		# fine tune iterations. 100 was.


pre_train_batch_size = 20		# 10 samples for a update.
Pre_train_nb_epoch = 20			# train 20 iterations. 20 is better than 50.
nb_classes = 2				# label 0 or 1.
Fine_tune_batch_size = 50		# fine tune for update. 25 samples for a update
Fine_tune_nb_epoch = 7	        # fine tune iterations. 100 was.


#print (X_train.shape)
#print (type(X_train))
#X_train = X_train.reshape(X_train.shape[0], 26)                                                                                                                                                                                  
#X_test = X_test.reshape(X_test.shape[0], 26) 
#print ('Train:',X_train.shape[0], 'test:',X_test.shape[0])                                                                                                                                                                                                                                                                                                                                                      

Y_train = np_utils.to_categorical(y_train, nb_classes)                                                                                                                                                              
Y_test = np_utils.to_categorical(y_test, nb_classes)                                                                                                                                                                
print ('=='*20)
print ('Pre-training the AE')
print ('=='*20)
# Layer-wise pretraining

encoders = []
#nb_hidden_layers = [90,100,100]			#[number of features, number of 1st layer, number of 2nd layer, ....]
#nb_hidden_layers = [par[5],100,100]			#[number of features, number of 1st layer, number of 2nd layer, ....]
#nb_hidden_layers = [par[5],100]
nb_hidden_layers = [par[5],100,100]
#nb_hidden_layers = [par[5],100,100,100]
#nb_hidden_layers = [par[5],100,100,100,100]
#nb_hidden_layers = [par[5],100,100,100,100,100,100,100]
X_train_tmp = np.copy(X_train)

#Added by NYU4
Y_train_tmp = np.copy(y_train)

for i, (n_in, n_out) in enumerate(zip(nb_hidden_layers[:-1], nb_hidden_layers[1:]), start=1):
	print('Pre-training the layer {}: Input {} -> Output {}'.format(i, n_in, n_out))
	# Create AE and training
	ae = Sequential()
	encoder = Dense(output_dim=n_out, input_dim=n_in, activation='relu')
	#encoder = Dense(output_dim=n_out, input_dim=n_in, activation='sigmoid')
	#else:
		#encoder = containers.Sequential([Dense(output_dim=n_out, input_dim=n_in, activation='tanh')])
	decoder = Dense(output_dim=n_in, input_dim=n_out, activation='relu')
	ae.add(AutoEncoder(encoder=encoder, decoder=decoder, output_reconstruction=True))
 
	""" """ #alternative methods.
	''' 
	sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
	ae.compile(loss='categorical_crossentropy', optimizer=sgd)
	'''
	
	# method categorical_crossentropy for discrete samples.
	ae.compile(loss='categorical_crossentropy', optimizer='adadelta')
	#ae.compile(loss='categorical_crossentropy', optimizer=SGD(lr=0.01, momentum=0.9, nesterov=True));
	#ae.compile(loss='mse', optimizer='adam')
	
	#now iterate on training data in batches
	ae.fit(X_train_tmp, X_train_tmp, batch_size=pre_train_batch_size, nb_epoch=Pre_train_nb_epoch, verbose=2, shuffle=True)
	
	
	# Store trainined weight and update training data
	encoders.append(ae.layers[0].encoder)
	#decoders.append(ae.layers[0].decoder)
	
	
	encoder_temp = Sequential()
	encoder_temp.add(encoders[i-1])
	#encoder_temp.add(encoders[i])
	# This encoder_temp.compile just for .predict, not real using
	encoder_temp.compile(loss='mse', optimizer='adam')
	#encoder_temp.compile(loss='categorical_crossentropy', optimizer='adadelta')
	X_train_tmp = encoder_temp.predict(X_train_tmp, batch_size=X_train_tmp.shape[0])
	
print ('=='*20)
print ('Fine-tuning the AE after the each layer\'s separate training.')
print ('Fine-tune through the whole architecture.')
print ('=='*20)



model = Sequential()
for encoder in encoders:
	model.add(encoder)
	
model.add(Dense(nb_classes)) 
model.add(Activation('softmax'))
    
#model.add(Dense(nb_classes, input_dim=nb_hidden_layers[-1], activation='softmax')) 
model.compile(loss='categorical_crossentropy', optimizer='adadelta')

model.fit(X_train, Y_train, batch_size=Fine_tune_batch_size, nb_epoch=Fine_tune_nb_epoch,
          show_accuracy=True, verbose=2, validation_data=(X_test, Y_test))

		  
print("output the result of test data...")		  
X_pro = model.predict_proba(X_test, batch_size=X_test.shape[0])

#print (type(X_pro))
#print X_pro
#print (X_pro.shape)
file_object = open('c:\Users\Ning Yu\Documents\splicing-site-test\prob_gene.txt', 'w')

#number_it = int(X_pro.shape[0])
#temp_value = '0.0'
TP,TN,FP,FN=0,0,0,0;

file_object.write('estimated value \t label \t predict \n');
for i in range(0,X_pro.shape[0]):
	res = -1;
	if X_pro[i][1] < 0.5 and y_test[i] == 0:
		TN = TN + 1;
		res = 0;
	elif X_pro[i][1] >= 0.5 and y_test[i] == 0:
		FP = FP + 1;
		res = 1;
	elif X_pro[i][1] < 0.5 and y_test[i] == 1:
		FN = FN + 1;
		res = 0;
	elif X_pro[i][1] >= 0.5 and y_test[i] == 1:
		TP = TP + 1;
		res = 1;
		
	file_object.write(str(X_pro[i][1])+'\t'+str(y_test[i])+'\t'+str(res)+'\n')
	#file_object.write(str(X_pro[i][1])+'\n')
	


file_object.close( )

print 'TP\tFP\t FN\t TN';
print TP, '\t', FP, '\t', FN, '\t', TN, '\t';
#print len(y_test);
#print y_test[0];

score = model.evaluate(X_test, Y_test, show_accuracy=True, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])

