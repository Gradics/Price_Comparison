# Running a Python Script using another Python Script
# https://medium.com/codex/running-a-python-script-using-another-python-script-2a9773464d1b

import os
os.chdir(r"c:/Users/gradi/Documents/PROG/Scraping/Price_Comparison_v02/")


#imports a package called runpy which is used to locate and execute python scripts
import runpy
#the below variables define the path for each script file
Script1 = "00_Connections.py"
Script2 = "01_Price_Auchan.py"
Script3 = "02_Price_Kifli.py"
Script4 = "03_Price_merge.py"
Script5 = "04_Email_sending.py"

runpy.run_path(path_name=Script1)
print("Script 1 complete")

runpy.run_path(path_name=Script2)
print("Script 2 complete")

runpy.run_path(path_name=Script3)
print("Script 3 complete")

runpy.run_path(path_name=Script4)
print("Script 4 complete")

runpy.run_path(path_name=Script5)
print("Script 5 complete")

