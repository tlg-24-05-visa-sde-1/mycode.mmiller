#!/usr/bin/env python3

# necessary imports from standard libraries
import shutil
import os

def main():

    #force python to start in home directory
    os.chdir('/home/student/mycode/')

    #move the file at the path source to the path destination
    shutil.move('raynor.obj', 'ceph_storage/') # will return string of absolute path of new location

    # prompt user for new name for kerrigan.obj file
    xname = input('What is the new name for kerrigan.obj? ')

    # rename current kerrigan.obj file
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

if __name__ == "__main__":
    main()


