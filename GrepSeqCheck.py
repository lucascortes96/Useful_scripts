#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 10:39:23 2022

@author: nlt112
"""

#!/usr/bin/env python

import sys
import os
import gzip
import glob, os
import csv

def getBars():
    barfile = input("enter name of barcode file: ")
    bars = []
    with open(barfile, 'r') as bf:
        reader = csv.reader(bf, delimiter=',')
        for row in reader:
            bars.append(row[1])
    return(bars)

def processBars():
    bars = getBars()
    newbars = []
    for i in bars:
        newbars.append(''.join([c for c in i if c.isupper()])) 
    return(newbars)
     

def myOpen(infile, mode="rt"):
    if infile.endswith(".gz"):
        return gzip.open(infile, mode=mode)
    else:
        return open(infile, mode=mode)

def openAndProcess():
    usr_dir = input("enter your directory: ")
    os.chdir(usr_dir)
    bars = processBars()
    for file in glob.glob("*.fastq.gz"):
        for i in bars:
            cmd = "grep " + " '" + i + " '" + " " + file + ">" + file +".result.txt"
            

def main():
    openAndProcess()
    
            
if __name__ == "__main__":
    main()