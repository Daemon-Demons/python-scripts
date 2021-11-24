import os
import sys
# import pandas as pd
# import numpy as np

#help message
help_message = """python3 testtime_csv2xlsx.py -i <file.csv> -o <file.xlsx>
    -i  :   input csv file
    -o  :   output csv file/path
    -h  :   prints this message
 """
if (len(sys.argv) == 2):
    if(sys.argv[1] == "-h"):
        print('Test time crunching tool\n', help_message)
    else:
        print('Please input argument\n', help_message)