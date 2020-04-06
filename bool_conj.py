import sys
import numpy as np

#return 1 if h is good for example
def calc_hypothesis(h,assignments):
    for i,x in enumerate(assignments):
        if (x == 1 and (h[0][i] == 0 or h[1][i] == 1)) or (x == 0 and (h[0][i] == 1 or h[1][i] == 0)):
            return 0
    return 1
    
#print the function    
def print_conj(h):
    func = ""
    for i in range(np.shape(h)[1]):
        if h[1][i] == 1:
            func += "not(x" + str(i+1) + "),"
        elif h[0][i] == 1:
            func += "x" + str(i+1) + ","
    print(func[:-1])
    
if __name__ == "__main__":
    file_name = "./data/train.txt"
    data = np.loadtxt(file_name, dtype = int)
    dim = data.shape[1] - 1
    
    #h[0] - positives
    #h[1] - negatives
    h = np.ones((2,dim), dtype = int)
    
    #for each example in the file
    for line in data:
        tag = line[-1]
        assignments = line[:-1]

        #calc hypothesis only for positive tags
        if tag == 1:
            #predictions were wrong. need to fix
            if not calc_hypothesis(h,assignments):
                for i in range(dim):
                    #x is false. remove it from pos hypothesis
                    if assignments[i] == 0:
                        h[0][i] = 0
                    else:
                        h[1][i] = 0

    print_conj(h)
