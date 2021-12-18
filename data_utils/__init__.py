import pathlib
import re 
import sys 
sys.path.append("..")

def read_n_proc(filename):
    with open(filename,'r') as file:
        raw_text = file.read().lower() 

        # Remove punct
        raw_text = re.sub('[^a-zA-Z0-9.?!;]',' ',raw_text)

        #Split Into Sentences 
        sentences = re.split('[;.?!]', raw_text)


        return sentences

def output_csv(name,row, col):

    with open(name, 'w') as output:

        output.write(col + '\n')

        for r in row:
            output.write(r + '\n')

    
    

        