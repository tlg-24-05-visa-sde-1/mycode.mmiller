#!/usr/bin/env python3

"""MMiller | TLG Learning
   Pushing files using import util & import os"""

# import necessary code from standard libraries
import shutil
import os

def main():

    # move into the working directory
    os.chdir("/home/student/mycode/")

    # copy fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # copy the entire directoryA to directoryB
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()

