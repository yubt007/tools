#!/usr/bin/env python3
#time: 2018/04/20 16:03
#version:1.0
#_author_:Benty_Yu

file1 = input('which flie you want to open it\n')
file2 = input('which flie you want to complete with sequence1\n')

f1 = open(file1,'rt')
f2 = open(file2,'rt')

seq1=f1.readlines()
seq2=f2.readlines()

a =seq1[0].strip()
b =seq2[0].strip()

Distance = 0

for i in range(len(b)):
	if a[i]!=b[i]:
		Distance = Distance+1

	
print (Distance)
