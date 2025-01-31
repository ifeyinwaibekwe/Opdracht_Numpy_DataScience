image = Image.open("Belgium_lion.png")
image = image.resize((250,250))
image_array = np.array(image)

#creating flag with 3 stripes
flag_height =600
flag_width =900
stripe_width = flag_width // 3

#creating base flag array
flag = np.zeros((flag_height,flag_width,3),dtype= np.uint8) #3 colors , each color value is from 0 to 255

#first black stripe
flag[:,0:stripe_width] = [0,0,0]   #no red,no green,no blue

#middle_strip, yellow stripe
flag[:, stripe_width:2*stripe_width] = [255,255,0] #pay attention to the slices

#last red stripe
flag[:, 2*stripe_width:] = [255,0,0]

# to get the lion location on the flag
lion_y = (flag_height - image_array.shape[0]) // 2 #to get how far from up
lion_x = stripe_width + (stripe_width -image_array.shape[1]) // 2

lion_shape = (image_array == 0) # using just the black and white color
#lion_shape = (image_array[:,:,0] < 128) & (image_array[:,:,1] < 128 ) & (image_array[:,:,2] < 128 ) using the middle threshold 128 since 255 is the brightest.anyvalue below 128 is considered black                                                                                                 
flag[lion_y:lion_y + image_array.shape[0],lion_x:lion_x + image_array.shape[1]][lion_shape] = [0,0,0]

plt.figure(figsize=(10,6))
plt.imshow(flag)
plt.axis('off')
plt.title('Belgian Flag with Lion symbol')
plt.show()