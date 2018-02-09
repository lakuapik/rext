#!/usr/bin/env python3
##  Rext - Remove extension
##  Remove file extension on file system
##  @author: David Adi Nugroho <davidadi216@gmail.com>

import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dir", help="directory of file(s)")
parser.add_argument("-e", "--ext", help="extension to be removed")
parser.add_argument("-v", "--verbose", help="show all renamed files", action='store_true')
args = parser.parse_args()

if args.dir and args.ext:
    directory = os.path.abspath(args.dir)
    if not os.path.isdir(directory):
        print("No such directory: '"+directory+"'")
        sys.exit()
    os.chdir(directory)
    if args.verbose:
        print("===============")
        print("Starting Rext")
        print("===============")
        print("Directory:", directory)
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            if filename.find(args.ext) > 0:  
                subdirectoryPath = os.path.relpath(subdir, directory)
                filePath = os.path.join(subdirectoryPath, filename)
                newFilePath = filePath.replace(args.ext, "")
                os.rename(filePath, newFilePath)
                if args.verbose:
                    print("Renamed " +filePath+ " -> " +newFilePath)
    print("All clear.")