import imageio.v2 as iio
import scipy.ndimage as ndi
import numpy as np
import matplotlib.pyplot as plt

import imageio.v2 as iio
import matplotlib.pyplot as plt

brainAG_slice = iio.imread('Crane - 6295/3D_T1_16/IM-0001-0001.dcm')
type(brainAG_slice)
print(brainAG_slice._meta)
print(brainAG_slice.shape)
print(brainAG_slice._meta['sampling'])
plt.imshow(brainAG_slice)
plt.imshow(brainAG_slice, cmap='gray')
plt.axis('off')
plt.show()
brainAG_vol = iio.volread('Crane - 6295/3D_T1_16', 'DICOM')
print(brainAG_vol.shape)
plt.imshow(brainAG_vol[150], cmap='bone')
plt.axis('off')
plt.show()
plt.imshow(ndi.rotate(brainAG_vol[:, 150, :], 180), cmap='bone')
plt.axis('off')
plt.show()













