import io
import cv2
import matplotlib.pyplot as plt
from skimage import io

origem = "https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png"
img_original = io.imread(origem)
img_cinza = cv2.cvtColor(img_original, cv2.COLOR_RGB2GRAY)
fig, ax = plt.subplots(1, 2, figsize=(10, 6))
fig.tight_layout()

ax[0].imshow(img_original)  # No need for cv2.cvtColor here
ax[0].set_title("Original")

ax[1].imshow(img_cinza, cmap='gray')  # Use 'gray' colormap for grayscale image
ax[1].set_title("Tons de Cinza")

plt.show()
