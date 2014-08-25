#!/usr/bin/env python3
import requests
import os
import sys
from argparse import ArgumentParser

def pinger(file):
    try:
        i = 0
        with open(file, 'r') as links:
            link = links.read()
            link = link.split("\n")
            while link[i]:
               # if 'http' not in link[i]:

                req = requests.get(link[i])
                status = req.status_code
                if status != 200:
                    print("Error,", link[i])
                else:
                    print("Working")
                i += 1;
    except requests.exceptions.ConnectionError:
            print("Error", link[i])


if __name__ == '__main__':
    parse  = ArgumentParser()
    parse.add_argument("-f", dest="filename", help="Filename containing links", metavar="FILE")
    args=parse.parse_args()
    pinger(args.filename)
#    pinger(sys.argv[1])
