#!/usr/bin/env python3

import sys
import os
import zipfile
from argparse import ArgumentParser

def zipper(name, path, mode, flag):
    
    """arg name is the name of the file with its absolute path"""

    if os.path.exists(path):
        loc = name.rsplit(name.split("/")[-1])[0]
        name = name.split("/")[-1]
        k = os.listdir(loc)
        os.chdir(loc)
        
        for i in k:
            if name==i and flag==0:
                return "ERROR"

        with zipfile.ZipFile(name, mode) as comp:
            newpath = (path.rsplit(path.split("/")[-1]))[0]
            os.chdir(newpath)
            path = path.split("/")[-1]
            comp.write(path)
        return name

if __name__ == "__main__":
    flag = 0
    parser = ArgumentParser(description="Zip file creater")
    parser.add_argument("-n", "--name", dest="filename", help="file name", metavar="FILE")
    parser.add_argument("-p", "--path", dest="location", help="path of file to compress")
    #parser.add_argument("-p2", "--path2", dest="location2", default=None, help="path of file to compress")
    parser.add_argument("-f", "--force", action="store_true", default=False, help="force overwrite if file already exists")
    parser.add_argument("-q", "--quit", action="store_false", default=True, help="quit the program")
    
    args=parser.parse_args()
    if args.filename:
        i = zipper(args.filename, args.location, "w", flag)
        if i != "ERROR":
            print("%s created" %i)
        else:
            if args.force:
                print("args is ", args)
                flag = 1
                zipper(args.filename, args.location, "w", flag)
            else:
                print("\nFile already exists... Do you want to overwrite it use '-f or --force' in input or type ./filename -h for help\n")

