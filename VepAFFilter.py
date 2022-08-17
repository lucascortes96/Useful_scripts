#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:17:28 2022

@author: nlt112
"""
import sys
print("Provide two inputs, filename and AF filter level (0.01 or 0.05)")

file = str(sys.argv[1])
##If you get a vep output this will give you the AFs lower than 0.05
def vep5(file):
    with open(file) as f:
        lines = f.readlines()
        with open(file+'AFFilter0.05.txt', 'w') as fs:
            for i in lines:
                if ";AF=0.00" in i:
                    fs.write(i)
                elif ";AF=0.01" in i:
                    fs.write(i)
                elif ";AF=0.02" in i:
                    fs.write(i)
                elif ";AF=0.03" in i:
                    fs.write(i)
                elif ";AF=0.04" in i:
                    fs.write(i)
##If you get a vep output this will give you the AFs lower than 0.01
def vep1(file):
    with open(file) as f:
        lines = f.readlines()
        with open(file+'AFFilter0.01.txt', 'w') as fs:
            for i in lines:
                if ";AF=0.00" in i:
                    fs.write(i)
def main():
    choose = str(sys.argv[2])
    if choose == "0.01":
        vep1(file)
    if choose == "0.05":
        vep5(file)
    else:
        print("you need to make a valid choice AF filter choice!")
    
main()