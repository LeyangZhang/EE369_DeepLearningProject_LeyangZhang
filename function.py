#input a 3-D array
import numpy as np

def grid_ohe(arr):
    
    CAND=16
    map_table={2**i:i for i in range(1,CAND)}
    map_table[0]=0
    
    ret=np.zeros(shape=arr.shape+(CAND,),dtype=bool)
    for a in range(arr.shape[0]):
        for b in range(arr.shape[1]):
            for c in range(arr.shape[2]):
                ret[a,b,c,map_table[arr[a,b,c]]]=1
    return ret 