# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:02:42 2022

@author: lucas
"""

#!/usr/bin/env python

import sys
import os
import gzip

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
        
    try:
        n2 = int(input("Number of lines to print:"))
    except ValueError:
        n2 = 1000
    n = 4
    i = 0 
    
    with myOpen(fn) as fh:
        lines = []
        for line in fh:
            lines.append(line.rstrip())
            if len(lines) == n and i < n2:
                record = process(lines)
                sys.stderr.write("Record: %s\n" % (str(record)))
                lines = []
                i+=1
            


def main():
    OpenAndWrite()
    
            
if __name__ == "__main__":
    main()
