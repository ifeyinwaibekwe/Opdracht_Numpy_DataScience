from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from notebooks.Opdracht_Numpy_DataScience.image_nocolor import create_belgian_flag_with_bw_lion


def create_belgian_flag_with_lion(image_path="Belgium_lion.png",flag_height =600,flag_width = 900):

    # Converting the image to RGB
    image = Image.open(image_path).convert('RGB')
    image = image.resize((250, 250))
    image_array = np.array(image)

    # Creating flag with 3 stripes

    stripe_width = flag_width // 3

    # Creating base flag array
    flag = np.zeros((flag_height, flag_width, 3), dtype=np.uint8)

    # First black stripe
    flag[:, 0:stripe_width] = [0, 0, 0]

    # Middle stripe (yellow)
    flag[:, stripe_width:2*stripe_width] = [255, 255, 0]

    # Last stripe (red)
    flag[:, 2*stripe_width:] = [255, 0, 0]

    # Get the lion location on the flag
    lion_y = (flag_height - image_array.shape[0]) // 2
    lion_x = stripe_width + (stripe_width - image_array.shape[1]) // 2

    # Create lion shape mask
    lion_shape = (image_array[:,:,0] < 128) & (image_array[:,:,1] < 128) & (image_array[:,:,2] < 128)
    flag[lion_y:lion_y + image_array.shape[0], lion_x:lion_x + image_array.shape[1]][lion_shape] = [0, 0, 0]
    return flag

    # Display the flag
def display_flag(flag):
    plt.figure(figsize=(10, 6))
    plt.imshow(flag)
    plt.axis('off')
    plt.title('Belgian Flag with Lion symbol')
    plt.show()

    try:
        flag = create_belgian_flag_with_bw_lion()
        display_flag(flag)
    except Exception as e:
        print(f"Error: {e}")

