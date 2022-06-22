#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:07:05 2022

@author: Lucas Cortes 
"""

# This script will process a vcf to calculate variant allele frequency 


#!/usr/bin/env python

import sys
import os
import gzip
import csv
import pandas as pd


def myOpen(infile, mode="rt"):
    if infile.endswith(".gz"):
        return gzip.open(infile, mode=mode)
    else:
        return open(infile, mode=mode)
    
    
def OpenAndWrite():
    try:
        fn = sys.argv[1]
    except IndexError as ie:
        raise SystemError("Error: Specify file name\n")
    
    if not os.path.exists(fn):
        raise SystemError("Error: File does not exist\n")
        
    #This file becomes the final file, it is the file without the header
    with myOpen(fn) as fh:
        found = False
        f = open("test.txt", "w")
        for line in fh:
            if '#CHROM'  in line:
                found = True
            if found and "AD" in line:
                f.write(line)
                #print(line.split(":")[2])
        f.close()
      
        
def grabCol():
    with open("test.txt", "r+") as df:
        f = open("test1.txt", "w")
        for line in df:
            f.write(line.split()[9])
            f.write("\n")
    f.close()
    df.close()
    
def grabColon():
    with open("test1.txt", "r+") as df:
        f = open("test2.txt", "w")
        for line in df:
            f.write(str(line.split(":")[1:3]))
            f.write("\n")
            #print(line)
    f.close()
    df.close()

def divide():
    with open("test2.txt", "r+") as df:
        f = open("test3.txt", "w")
        ad = int()
        dp = int()
        for line in df:
            
            ad = (line.split(",")[1])
            dp = (line.split("'")[3])
            ad = int(ad)
            dp = int(dp)
            calc = ad/dp
            f.write(ad/dp)
            f.write("\n")
    f.close()
    df.close()
    
def paste():
    fn = sys.argv[1]
    os.system("paste -d '   ' test.txt test3.txt > "+fn+"vaf.txt")

            
def main():
    OpenAndWrite()
    grabCol()
    grabColon()
    divide()
    paste()
    os.remove("test.txt")
    for i in range(1,4):
        os.remove("test"+i+".txt")
    
            
if __name__ == "__main__":
    main()
