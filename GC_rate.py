#!/usr/bin/env python3
#time: 2017/11/07 21:33
#version: 1.0
#_author_:Benty_Yu

NA=0
NT=0
NC=0
NG=0
sum=0
other=0

file=input('which fsa flie do you want to open it\n')
raw_file = open(file,'rb')
raw_data = raw_file.readlines()
data=str(raw_data)

for Nuc in data:
    if Nuc =='A':
        NA=NA+1
        sum=sum+1
    if Nuc =='T':
        NT=NT+1
        sum=sum+1
    if Nuc =='G':
        NG=NG+1
        sum=sum+1
    if Nuc =='C':
        NC=NC+1
        sum=sum+1
    else:
        other=other+1


GC_rate=((NG+NC)/sum)

print("SUM:%s A:%s T:%s G:%s C:%s"%(sum,NA,NT,NG,NC))
print("GC_rate:%0.3f"%(GC_rate))


raw_file.close




