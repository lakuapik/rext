#!/usr/bin/env python3
##  Rext - Remove extension
##	Remove all extension on file system
##  @author: David Adi Nugroho <davidadi216@gmail.com>

import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dir", help="directory of file(s)")
parser.add_argument("-e", "--ext", help="extension to be removed")
args = parser.parse_args()

if args.dir and args.ext:
    directory = os.path.abspath(args.dir)
    os.chdir(directory)
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            if filename.find(args.ext) > 0:  
                subdirectoryPath = os.path.relpath(subdir, directory)
                filePath = os.path.join(subdirectoryPath, filename)
                newFilePath = filePath.replace(args.ext, "")
                os.rename(filePath, newFilePath)