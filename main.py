#!/usr/bin/env python3

import os  # this modules are used to run this program
import time


def file():
    os.system('clear')
    print('       ----------------------------------------------------------------------')
    print('                                         Files Searcher')
    print('       ----------------------------------------------------------------------')
    a = input('       Enter a file (with extension) to be search in this pc:')
    b = '/home/iresh'
    print('Processing.....')
    time.sleep(2)
    for path, folders, files in os.walk(b):
        if a in files:
            b = path
    print('The File is located in this path: ', b)
def folder():
    os.system('clear')
    print('       ----------------------------------------------------------------------')
    print('                                      Folder Searcher')
    print('       ----------------------------------------------------------------------')
    a = input('       Enter a folder to be search in this pc:')
    b = '/home/iresh'
    print('Processing.....')
    time.sleep(2)
    for path,folders,files in os.walk(b):
        if a in folders:
            b = path
    print('The Folder is located in this path: ',os.path.join(b,a))

os.system('clear')
print('       ----------------------------------------------------------------------')
print('                          Files and Folder Searcher')
print('       ----------------------------------------------------------------------')
c = input('       What do you want to search file or folder:')
if c.lower() == 'file':
    file()
elif c.lower() == 'folder':
    folder()
else:
    print('Please check you input!!')
