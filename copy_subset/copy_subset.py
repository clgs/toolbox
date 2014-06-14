# copy_subset.py
# Script to select a subset of text files from a larger text collection.
# v0.3, 2014-06-14, by #cf.


#######################
# Overview 
#######################

# 1. Reads metadata from CSV file.
# 2. Defines subset of files via filters based on metadata.
# 3. Copies subset of files to new folder

#######################
# Import statements
#######################

import glob
import pandas as pd
import numpy as np
import os
import shutil


#######################
# Functions
#######################

def copy_subset(fullset,metadata):
    metadata = pd.read_csv(metadata, delimiter=',', index_col=0)
    #print(metadata)
    by_date = metadata[metadata.date > 1720]
    by_date_sgenre = by_date[by_date.sgenre == "Comedie"]
    by_date_sgenre_form = by_date_sgenre[by_date_sgenre.form == "vers"]
    print(by_date_sgenre_form)
    subset = []
    for item in by_date_sgenre_form.index:
        item = item + ".txt"
        subset.append(item)
    print(subset)
    for file in glob.glob(fullset):
        if os.path.basename(file) in subset:
            shutil.copy(file, "./subset")


#######################
# Main
#######################

def main(fullset,metadata):
    copy_subset(fullset,metadata)

main("./fullset/*.txt","metadata.csv")
