#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 13:31:57 2022

@author: nlt112
"""

#!/usr/bin/env python3

import os
import subprocess
import glob
from pathlib import Path
import os

def check_star():
    rc = subprocess.call(['which', 'STAR'])
    if rc == 0:
        print('bwa installed!')
    else:
        print('bwa missing in path!')

def check_featureCounts():
    rc = subprocess.call(['which', 'featureCounts'])
    if rc == 0:
        print('samtools installed!')
    else:
        print('samtools missing in path!')


def get_genome():
    genome = input("give me the location of your STAR genome ")
    return(genome)
def getGtf():
    gtf = input("give me location of the gtf: ")
    return(gtf)

def get_prefix():
    prefix = input("write the prefix of your file ( everything before the L001)")
    L001R1 = prefix+"L001_R1_001.fastq.gz" #These may neeed to be changed
    L001R2 = prefix+"L001_R2_001.fastq.gz"
    L002R1 = prefix+"L002_R1_001.fastq.gz"
    L002R2 = prefix+"L002_R2_001.fastq.gz"
    L003R1 = prefix+"L003_R1_001.fastq.gz"
    L003R2 = prefix+"L003_R2_001.fastq.gz"
    L004R1 = prefix+"L004_R1_001.fastq.gz"
    L004R2 = prefix+"L004_R2_001.fastq.gz"
    
    return(prefix, L001R1, L001R2, L002R1, L002R2, L003R1, L003R2, L004R1, L004R2)

def makeDirectory():
    global all_stuff
    all_stuff = get_prefix()
    prefix = all_stuff[0]
    
    path = False
    if os.path.exists(prefix):
        path=True
        if path == True:
            os.makedirs(prefix)
        else:
            print("path exists please delete")
def star():
    genome = get_genome()
    cmd = "STAR --genomeLoad LoadAndKeep --genomeDir " + genome + " " +"--runThreadN 30 --readFilesIn " +all_stuff[1]+","+all_stuff[2]+","+all_stuff[3]+","+all_stuff[4]+","+all_stuff[5]+","+all_stuff[6]+","+all_stuff[7]+","+all_stuff[8] + " " + "--outFileNamePrefix " + all_stuff[0] + " " + "--readFilesCommand zcat" 
    os.system(cmd)  

def featureCounts():
    directory = all_stuff[0]
    gtf = getGtf()
    cmd = "featureCounts -g gene_name -p --primary -T 4 -a " + gtf + " " + "-o " + directory + "/"+ directory + "out.txt" + " " + directory + "Aligned.out.sam"
    os.system(cmd)


def main():
    ## Call all functions
    print("this script will automate your analysis, please put only the files you want to run in this directory, cheers, Lucas ")
    print("you will need to have bwa, samtools, and gatk4 installed prior to running this script ")
    check_star()
    check_featureCounts()
    get_prefix()
    makeDirectory()
    star()
    featureCounts()
main()