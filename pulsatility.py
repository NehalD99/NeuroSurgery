import numpy as np
from scipy.spatial.distance import directed_hausdorff
import os

import pdb

COMP = '/home/lahen/cvpr_code/PULSATILITY/COMP'
DECOMP = '/home/lahen/cvpr_code/PULSATILITY/DECOMP'

def measure_pulsation(dir_path):

    list_paths = os.listdir(dir_path)
    dir_hs = []

    for i,filename in enumerate(list_paths):

        if i < (len(list_paths)-1):
            frame_before = np.load(os.path.join(dir_path, filename))
            frame_after = np.load(os.path.join(dir_path, list_paths[i+1]))
            dir_hs.append( directed_hausdorff(frame_after[0], frame_before[0])[0])


    return sum(dir_hs)/(len(list_paths)-1)




def main(comp_path, decom_path):


    pulsa_comp = measure_pulsation(comp_path)
    pulsa_decomp = measure_pulsation(decom_path)

    print("The pulsation during compression is ",pulsa_comp, "and decompression is ", pulsa_decomp)

if __name__ == '__main__':

    comp_path = COMP
    decom_path = DECOMP
    main(comp_path, decom_path)

