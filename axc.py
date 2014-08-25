#!/usr/bin/env python3

"""
Program in Python3 to create ZIP files
"""

from sys import argv
from zipfile import ZipFile
import os.path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--force", help="force action", action="store_true")
parser.add_argument("Zipfile", help="path of the output zip file")
parser.add_argument("Source", help="path(s) of the input files")
args = parser.parse_args()


def zipping():
    with ZipFile(args.Zipfile, 'w') as myzip:
        myzip.write(args.Source)
        print("done")

if args.force:
    zipping()
elif os.path.isfile(args.Zipfile):
    print("The file already exists. Do you want to overwrite? y/n")
    ans = input("=>")
    if ans == 'y':
        zipping()
    else:
        print("Try another name")
else:
    zipping()
