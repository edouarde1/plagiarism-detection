
# Files

### main.py
grabs each file in data/*.txt and stores as a collection
runs collection of files through run_n_grams() from %n_grams.py
collects n_grams.py informtion and runs through cacls() from %containment.py 

### n_grams.py
grabs each file from a collection of file paths from %main.py 
processes each file in read_n_proc() from %data_utils
prints out n-gram inforation to output.txt 
returns a datastructure to %main.py that stores all file n-gram information

### python containment.py 
computes the containment value for every pair of files using n-grams with n=1..10
creates a col header for csv file 
sends containment values and col header to output_csv() in %data_utils

### data_utils/__init__.py 
function to process files 
function to output information in a csc called output.txt 
