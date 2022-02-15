#Libraries
import numpy as np
import fnmatch
import os

def create_files(count):
    #Creating Multiple Files At Once 
        
    for i in range(count):
        fn = "Data/file_" + str((i+1)) +".txt"
        f = open(fn,'w')


def start(query):

    # create_files(10)
    
        

    #Variables & DS needed
    file_count = 10            # file_count to count number of files
    files_dict = {}             # files_dic to store count of every file    
    unique_word_set = set()     # unique_word_set to store all the unique words in a set



    # STORING ALL UNIQUE WORDS FROM FILE IN DS 
    for i in range(file_count):
        f = open("Data/file_"+str(i+1)+".txt",'r',encoding="utf8")
        unique_word_set.update(f.read().upper().split(" "))
        
    # for w in unique_word_set:
    #     print(w)


    #CREATING AND FILLING A TERM DOCUMENT MATRIX
    Term_Matrix = np.zeros((file_count,len(unique_word_set)))

    for i in range(file_count):
        fn = "Data/file_" + str((i+1)) +".txt"
        f = open(fn,'r',encoding="utf8")
        k = 0
        for word in f.readline().upper().split():
            k = 0
            for uw in unique_word_set:
                if word == uw:
                    Term_Matrix[i][k] = 1
                k +=1    

    # for i in Term_Matrix:
    #     print(i)

    Col_Vector = np.zeros((1,len(unique_word_set)))

    i = 0
    for word in query.upper().split(" "):
        i = 0
        for w in unique_word_set:
            if word == w:
                Col_Vector[0][i] = 1
            i=i+1
                
    #print(Col_Vector)

    #FINALLY CHECKING WHICH FILE HAS MOST WORDS OF QUERY 
    flag = True

    result = np.dot(Term_Matrix,np.transpose(Col_Vector))

    #print("RESULTANT VECTOR\n",result)
    #print("Maximum value : ",np.amax(result))

    index = np.where(result == np.amax(result))
    #print("Is at Index : ",str(index[0][0]))

    if np.amax(result) == 0:
        flag = False
        

    if flag == False:
        return -1

    else:    
        filename = "Data/file_" + str(index[0][0]+1) + ".txt"

        #print(filename)

        f = open(filename, 'r')
        return f.read()