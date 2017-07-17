# -*- coding: utf-8 -*-
#import gzip

#from six.moves import cPickle
import sys
import numpy

def load_data(dataset, par):
	print "...Load the dataset"
	#e = numpy.loadtxt('c:\Users\Ning Yu\Documents\splicing-site-test\splice_site_dataset\splice.false.A.EIIP.txt_n_splice.real.A.EIIP.txt',dtype=numpy.float32)
	e = numpy.loadtxt(dataset,dtype=numpy.float32)
	#e = numpy.loadtxt(dataset,dtype=numpy.float64)
	#print  e.shape
	'''
	X_train = e[0:5664,0:90]
	y_train = e[0:5664,90]
	
	
	#print  y_train
	#print X_train.shape
	X_test = e[5664:6664,0:90]
	y_test = e[5664:6664,90]
	'''
	
	
	#par = [start_train, stop_train, start_test, stop_test, start_col, stop_col]
	#par=[0,5664,5664,6664,0,89];	
	X_train = e[par[0]:par[1],par[4]:par[5]]
	y_train = e[par[0]:par[1],par[5]-par[4]]
	
	
	#print  y_train
	#print X_train.shape
	X_test = e[par[2]:par[3],par[4]:par[5]]
	y_test = e[par[2]:par[3],par[5]-par[4]]
	
		
	
	#print  y_test
	return [(X_train, y_train), (X_test, y_test)]
if __name__ == '__main__':
	dataset='Yeast_data'
	load_data(dataset)
	