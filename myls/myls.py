#!/usr/bin/env python3

import os
import sys
from argparse import ArgumentParser

def myls(path):
    for files in os.walk(path):
        name = files[-1]
        direc = files[-2]
        for filen in name:
            print(filen, end=" ")
        for dire in direc:
            print(dire, end=" ")
        print("")
        return
            

if __name__ == '__main__': 
#    path = os.getcwd() 
    try:
        if sys.argv[1] != 0:
            path = sys.argv[1]
        myls(path)
    except IndexError:
        path = os.getcwd()
        myls(path)

