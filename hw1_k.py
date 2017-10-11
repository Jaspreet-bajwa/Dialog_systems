from nltk.book import *
from nltk import bigrams;
from collections import Counter
import numpy as np
import pandas as pd

lamda=0.9

def enc_dec(unigram):
	length=0;
	encode={};
	decoder={};
	for key,_ in unigram:
	    encode[key]=length
	    decoder[length]=key
	    length+=1
	return encode,decoder,length

def create_2d(Bigram,Unigram,encode,decoder,length):
	mat=np.zeros((len(Unigram),len(Unigram)))
	for key in Bigram:
	    mat[encode[key[0]]][encode[key[1]]]=Bigram[key]/Unigram[key[0]]
	for i in range(0,len(Unigram)):
	    for j in range(0,len(Unigram)):
		mat[i][j]=lamda*mat[i][j]+((1-lamda)*Unigram[decoder[j]]/length);
	return mat

def excel_data(decoder,mat,size):
	row=[];
	for i in range(0,size):
	    row.append(decoder[i]);
	df=pd.DataFrame(mat,index=row,columns=row)
	writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
	df.to_excel(writer, sheet_name='Sheet1')
	writer.save()

if _name=="main_":
	text1_upper=[text.upper() for text in text1]
	Bigrams=Counter(bigrams(text1_upper))
	Unigram=Counter(text1_upper)
	encode,decode,length=enc_dec(Unigram.most_common())
	mat=create_2d(Bigrams,Unigram,encode,decode,len(text1))
	excel_data(decode,mat[:25,:25],25)
