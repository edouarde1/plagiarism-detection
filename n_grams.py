from data_utils import read_n_proc



def run_n_grams(collection, n):

    """
    This function finds and runs (1-n) grams on a collection of files 
    and outputs n-grams on each file in output.txt
    
    Parameters:
    ----------
    collection= a list of file paths 

    Returns:
    ---------
    res = a list of tuples (filename, fileGrams) that stores all (1-n) grams for each file
    """
    proc_files = []  
    res = []
    with open('ngrams-per-file.txt', 'w') as output:
        res = [] # res [filename, fileGrams]

        # Iterate through files
        for file in collection:
            filename_short = file.split('/')[-1] 
            output.write("Processing File: {filename} \n".format(filename = filename_short))
            
            #process files
            proc_file_text = (read_n_proc(file))
        
            # file = a.txt
            # fileGrams { 1 : [all 1 grams for a.txt]
            #             2 : [all 2 grams for a.txt]
            #             3 : [all 3 grams for a.txt]    
            #            ...    ..............
            #             n : [all n grams for a.txt]
            # }

            fileGrams = dict()             
            # Iterate through each sentence in file 
            for sentence in proc_file_text:
                # Convert sentence into a list for partioning purposes 
                words = sentence.split()
                j = len(words)
                    #Calculate all (1-n) n-grams per sentence
                for i in range(1,n+1):
                    if i not in fileGrams:
                        fileGrams[i] = list()
                    grams = []
                    if words:  
                        output.write("n= {val} \n".format(val=i))
                        for m in range(0, j-i+1):
                            grams.append(' '.join(words[m:m+i]))        # n-grams per sentence level, for printing 
                            fileGrams[i].append(' '.join(words[m:m+i]))
                        output.write("{grams} \n".format(grams=grams))
            res.append( (filename_short, fileGrams) )
    
    return res 






