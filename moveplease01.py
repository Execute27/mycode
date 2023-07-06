#!/usr/bin/env python3

import shutil #shell utilites will be used to move files
import os # provies access to the low level os operations (agnostic to favor of OS)

def main():
    """called at runtime"""
os.chdir('/home/student/mycode/') # move into this working directory
shutil.move('raynor.obj', 'ceph_storage/') # try moving the file raynor.obj

# program will pause while we accept input
xname = input('What is the new name of kerrigan.obj? ')
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main() #this calls our main fucntion
