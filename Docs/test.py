# required imports
import sys
import os

os.chdir("..")
# find absolute paths
_CloudAPIs =  os.path.join(os.getcwd(), os.path.dirname("CloudAPIs"))
_libs =  os.path.join(os.getcwd(), os.path.dirname("libs"))

# insert into path variables
sys.path.insert(0,_CloudAPIs)
sys.path.insert(0,_libs)

# import from path variables
<<<<<<< HEAD
import CloudAPIs.sqlInterface as l

print(os.getcwd())
os.chdir("CSC405")
print(os.getcwd())

m = l.query.account_email(1)
=======
from CloudAPIs.sqlInterface import *

m = query.account_email(1)
>>>>>>> 8387eb1308925c1ecfd7788264dae94fd9b9dabc

for i in m:
    print(i)
