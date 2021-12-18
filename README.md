
# Files


grabs each file in data/*.txt and stores as a collection
runs collection of files through run_n_grams() from %n_grams.py
collects n_grams.py informtion and runs through cacls() from %containment.py 
% main.py 

grabs each file from a collection of file paths from %main.py 
processes each file in read_n_proc() from %data_utils
prints out n-gram inforation to output.txt 
returns a datastructure to %main.py that stores all file n-gram information
%n_grams.py

computes the containment value for every pair of files using n-grams with n=1..10
creates a col header for csv file 
sends containment values and col header to output_csv() in %data_utils
% python containment.py 


function to process files 
function to output information in a csc called output.txt 
% data_utils/__init__.py 
