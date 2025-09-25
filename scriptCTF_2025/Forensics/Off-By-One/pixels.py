from PIL import Image
import numpy as np


    
pixels = list(Image.open("hidden.png").convert('RGB').getdata())[:29**2]

binary_string = "".join(['1' if sum(p) % 2 else '0' for p in pixels])
    

qr_matrix = np.array(list(binary_string), dtype=np.uint8).reshape((29, 29))

scale = 10
scaled_matrix = np.kron(qr_matrix, np.ones((scale, scale), dtype=np.uint8))
image_array = (1 - scaled_matrix) * 255
    
reconstructed_image = Image.fromarray(image_array.astype(np.uint8))
reconstructed_image.save("corrected.png")