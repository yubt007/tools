#!/usr/bin/env python3
#time: 2017/11/10 10:03
#version:1.0
#_author_:Benty_Yu

import re

file=input('which flie do you want to open it\n')
raw_file = open(file,'rb')

seq = ''
for line in raw_file:
    line = line.strip()
    line = line.decode('GBK')
    seq += line.upper()
    
    RNAseq = re.sub(r'T','U',seq)


def complement_seq(seq):
    change = {'A':'T','G':'C','T':'A','C':'G'}
    reverse = list(reversed(seq))
    reverse_change_seq = [change[k] for k in reverse]

    revcomseq = ''.join(reverse_change_seq)
    return revcomseq
		
print("RNAseq:%s"%(RNAseq))
print("DNA2seq:%s"%(complement_seq(seq)))
