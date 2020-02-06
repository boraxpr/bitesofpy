#!/usr/bin/python3
import sys
import subprocess

userinput = sys.argv[1]
bash_unzip = "unzip {userinput}.zip -d {userinput}".format(userinput=str(userinput))
bash_remove = "rm {userinput}.zip".format(userinput=str(userinput))
subprocess.call(bash_unzip.split())
subprocess.call(bash_remove.split())
