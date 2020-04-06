import sys
from pathlib import Path
import random
import numpy as np

#print the function    
def print_conj(h):
    func = ""
    for i in range(len(h)):
        if h[i] == 0:
            func += "not(x" + str(i+1) + "),"
        elif h[i] == 1:
            func += "x" + str(i+1) + ","
    print(func[:-1])

if __name__ == "__main__":
    dir = "./data/"
    file_name = "train.txt"
    dim,num_of_examples = int(sys.argv[1]),int(sys.argv[2])
    
    #dim = 5
    #num_of_examples = 50
    
    # create a dim variables boolean conjunction formula randomly
    # 0 - neg, 1 - pos, 2 - ignore
    bool_conj = [random.randrange(3) for i in range(dim)]
    print_conj(bool_conj)
    examples = []
    for i in range(num_of_examples):
        #decide if current example is pos or neg one
        line = []
        curr_tag = 1
        for curr_x in bool_conj:
            curr_var = random.randrange(2)
            line.append(curr_var)

            #current Xi has wrong tag
            if (curr_x == 0 and curr_var == 1) or (curr_x == 1 and curr_var == 0):
                curr_tag = 0
        
        line.append(curr_tag)
        examples.append(line)
        
    Path(dir).mkdir(parents = True, exist_ok = True)
    np.savetxt(dir + file_name, examples,"%i")
    
