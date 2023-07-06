#!/usr/bin/env python3

# import additional code to complete the task
import shutil
import os

# move into the working directory
os.chdir("/home/student/mycode/")

# copy the fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# cope the entire directoryA to direcotryB
shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__'':
    main()
