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
    
    
def process(lines=None):
    ks = ['name', 'sequence', 'optional', 'quality']
    return {k: v for k, v in zip(ks, lines)}

def OpenAndWrite():
    
    try:
        fn = sys.argv[1]
    except IndexError as ie:
        raise SystemError("Error: Specify file name\n")
    
    if not os.path.exists(fn):
        raise SystemError("Error: File does not exist\n")
        
    
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
            f.write(line.split()[10])
            f.write("\n")
    f.close()
def grabColon():
    with open("test1.txt", "r+") as df:
        f = open("test2.txt", "w")
        for line in df:
            f.write(str(line.split(":")[1:2]))
            f.write(str(line.split(":")[3:4]))
            f.write("\n")
            #print(line)
    f.close()

def divide():
    with open("test2.txt", "r+") as df:
        f = open("test3.txt", "w")
        ad = int()
        dp = int()
        for line in df:
            
            ad = (line.split("[")[1])
            ad = (ad.split(",")[1])
            
            dp = (line.split("[")[2])
            dp = ''.join(i for i in dp if i.isdigit())
            ad = ''.join(i for i in ad if i.isdigit())
            ad = int(ad)
            dp = int(dp)
            if ad and dp !=0:
                calc = ad/dp
                print(calc)
                f.write(str(calc))
                f.write("\n")
            else:
                f.write("0")
                f.write("\n")
            
def paste():
    fn = sys.argv[1]
    os.system("paste -d '  ' test.txt test3.txt > "+fn+"vaf.txt")
            
def main():
    OpenAndWrite()
    grabCol()
    grabColon()
    divide()
    paste()
    os.remove("test.txt")
    for i in range(1,4):
        os.remove("test"+str(i)+".txt")
            
if __name__ == "__main__":
    main()
