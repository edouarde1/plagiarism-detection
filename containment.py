from data_utils import output_csv

def calcs (fileGrams, n):  # fileGrams = [ (filename, fileGram { 1 :[all 1-grams]
#                                                             2 :[all 2-grams] 
#                                                           ...     ....  
#                                                            n : [all n-grams]   } )]
    rows = []
    for file_a, fileGram_a in fileGrams:
        for file_b, fileGram_b in fileGrams:
            row = file_a + ',' + file_b
            for i in range(1, n+1):
                s_a = fileGram_a[i]
                s_b = fileGram_b[i]
                total_element = len(set(s_b))
                #if file_a == file_b:
                    #print(file_a, file_b, len(set(s_a).intersection(s_b)), len(set(s_a)))
                num_matches = len(set(s_a).intersection(s_b))
                containment_val = num_matches/total_element
                row += ', ' + str(containment_val)
            rows.append(row)

    col = "A,B,\"C_1(A,B)\",\"C_2(A,B)\",\"C_3(A,B)\",\"C_4(A,B)\",\"C_5(A,B)\",\"C_6(A,B)\",\"C_7(A,B)\",\"C_8(A,B)\",\"C_9(A,B)\",\"C_10(A,B)\""

    output_csv("cvals.csv", rows,col)
                



                

