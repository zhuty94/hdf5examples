"""
This example shows how to read and write enumerated datatypes to a dataset.
The program first writes enumerate values to a dataset with a dataspace of DIM0,
then closes the file.  Next, it reopens the file, reads back the data,
and outputs it to the screen.
"""
import numpy as np
import h5py

FILE = "h5ex_t_enum.h5"
DATASET = "DS1"

DIM0 = 4
DIM1 = 7

def run():

    # Create the enum datatype.
    mapping = {'SOLID': 0, 'LIQUID': 1, 'GAS': 2, 'PLASMA': 3}
    dtype = h5py.special_dtype(enum=(np.int16, mapping))

    # Initialize the data.
    wdata = np.zeros((DIM0, DIM1), dtype=np.int32)
    for i in range(DIM0):
        for j in range(DIM1):
            wdata[i][j] = ((i + 1) * j - j) % (mapping['PLASMA'] + 1)

    with h5py.File(FILE, 'w') as f:
        dset = f.create_dataset(DATASET, (DIM0, DIM1), dtype=dtype)
        dset[...] = wdata


    with h5py.File(FILE) as f:
        dset = f[DATASET]
        rdata = dset[...]

    # Make the inverse mapping so that it's easier to interpret the output.
    inv_mapping = {v:k for (k,v) in mapping.items()}
    print("%s:" % DATASET)
    for row in rdata:
        print([inv_mapping[item] for item in row])


if __name__ == "__main__":
    run()        
   

