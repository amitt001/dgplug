#!/usr/bin/env python3

import os
import sys
from argparse import ArgumentParser
import hashlib

def duplicate(path):
    unique = []
    dup = []
    for files in os.walk(path):
        for a_file in files[-1]:

            file_loc = path + "/" + a_file
            with open(file_loc, "rb") as fobj:
                filehash = hashlib.md5(fobj.read()).hexdigest()
            if filehash not in unique:
                unique.append(filehash)
            else:
                dup.append(file_loc)

        return dup

if __name__ == '__main__':
    
    parser = ArgumentParser()
    parser.add_argument("-d", help="Directoy")
    args = parser.parse_args()

    path = os.getcwd()

    if args.d:
        path = args.d

    a = duplicate(path)
    print(a)
    if a:
        for name in a:
            print("Duplicate file found: ", name.split("/")[-1])
    else:
        print("No duplicate file found")
