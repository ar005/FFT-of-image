mport cv2
import numpy as np
from matplotlib import pyplot as plt

loc="/home/animesh/htmml_css/signal_and_systems/pics/image1.jpg"
image=cv2.imread(loc)
f=np.fft.fft2(image)
fshift=np.fft.fftshift(f)
magnitude=20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(image,cmap='gray')
plt.title('Input Images'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(magnitude,cmap='gray')
plt.title('Magnitude Spectrum'),plt.xticks([]),plt.yticks([])
plt.show
