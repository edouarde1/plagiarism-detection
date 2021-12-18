
# Files

### main.py
- Grabs each file in data/*.txt and stores as a collection
- Runs collection of files through run_n_grams() from %n_grams.py
- Collects n_grams.py informtion and runs through calcs() from %containment.py 

### n_grams.py
- Takes each file path from %main.py 
- Processes each file in read_n_proc() from %data_utils
- Prints out n-gram inforation to output.txt 
- Returns a datastructure to %main.py that stores all file n-gram information

### containment.py 
- Computes the containment value for every pair of files using n-grams with n=1..10
- Creates a col header for csv file 
- Sends containment values and col header to output_csv() in %data_utils

### data_utils/__init__.py 
- Function to preprocess files 
- Function to output information in a csv called output.txt 
