import numpy as np
shuffeld_kspace = np.load('raw_data/shuffeld_kspace.npy')
schem = np.load('raw_data/schem.npy')
import fastmri
from fastmri.data import transforms

# https://stackoverflow.com/questions/20265229/rearrange-columns-of-numpy-2d-array
# это если у нас указано в какой по индексу элемент переходит данный
def rerange_cols(a, permutation):
    idx = np.empty_like(permutation)
    idx[permutation] = np.arange(len(permutation))
    return a[idx, :]  # in-place modification of a

schem_int = np.array(schem, 'int64')
shuffeld_kspace_rearrange_rows = rerange_cols(shuffeld_kspace, schem_int) # shuffeld_kspace[schem_int, :]
volume_kspace = transforms.to_tensor(shuffeld_kspace_rearrange_rows)
slice_image = fastmri.ifft2c(volume_kspace)        # Apply Inverse Fourier Transform to get the complex image
slice_image_abs = fastmri.complex_abs(slice_image)  # Compute absolute value to get a real image

from matplotlib import pyplot as plt
fig = plt.figure()
plt.imshow(np.abs(slice_image_abs.numpy()), cmap='gray')
plt.savefig(f'output/output.png')