import nltk
import pandas as pd
from nltk.collocations import *
from nltk.book import text1
from collections import Counter
from nltk.probability import SimpleGoodTuringProbDist
from openpyxl import Workbook

#Create your bigrams
bgs = nltk.bigrams(text1)

#compute frequency distribution for bigrams
fdistB = nltk.FreqDist(bgs)

#compute frequency distribution for unigrams
fdistU = nltk.FreqDist(text1)

#apply simple good turing smoothing method
sgt = SimpleGoodTuringProbDist(fdistB)

#most common 25 unigrams
mostCommon = fdistU.most_common(25)

#initialize dataframe for the excel sheet
column = []
for k, v in mostCommon:
    column.append(k)

#data frame

df = pd.DataFrame(index = column, columns = column)

#fill data frame with probability data
for k , v in mostCommon:
    for k1, v1 in mostCommon:
        df.loc[k][k1] = sgt.prob((k,k1))

#write dataframe in excel sheet
writer = pd.ExcelWriter("output.xlsx")
df.to_excel(writer, "Sheet1")
writer.save()

