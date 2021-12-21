# Overview
The purpose of this project was to implement a simple plagarism technique using a containment metric in order to perform analysis between two bodies of text. For every file, n-grams are calculated for n = 1, 2, 3,... 10 grams. Each n-gram for each file is placed in one file. The containment calcation is as follows: 

C(A,B) = |S(A) ∩ S(B)| / |S(B)| where S(A) is a set of n-grams for document A and S(B) is a set of n-grams for document B

For every pair of documents the containment calcuation is calculated. When n=1, create the set of unigrams in the text A and the set of unigrams in the text B (call this S_B). Then determine the size of the intersection of the two sets and the size of S_B to calculate C1(A,B). After that, repeat this for the remaining values of n.

These containment values can be used and interpret and find if one body of text is plagarised by another.



## Files

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
      



