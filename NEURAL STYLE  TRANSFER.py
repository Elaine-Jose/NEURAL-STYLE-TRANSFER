import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
import cv2
from matplotlib import pyplot as plt
print("Loading style transfer model...")
model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
print("Model loaded successfully.\n")
def load_image(path_to_img):
    print(f"Loading image: {path_to_img}")
    img = tf.io.read_file(path_to_img)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]  
    print(f"Image {path_to_img} loaded and preprocessed.\n")
    return img
try:
    content_image = load_image("content.jpg")  
    style_image = load_image("style.jpg")     
except Exception as e:
    print("Error loading images:", e)
    exit()
print("Applying style transfer...")
try:
    stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]
    print("Style transfer completed.\n")
except Exception as e:
    print("Error during style transfer:", e)
    exit()
print("Converting and saving stylized image...")
try:
    output_image = np.squeeze(stylized_image)
    output_image = (output_image * 255).astype(np.uint8)
    output_image_bgr = cv2.cvtColor(output_image, cv2.COLOR_RGB2BGR)  
    cv2.imwrite("stylized_output.jpg", output_image_bgr)
    print("Stylized image saved as 'stylized_output.jpg'\n")
except Exception as e:
    print("Error saving image:", e)
    exit()
try:
    plt.imshow(cv2.cvtColor(output_image_bgr, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.title("Stylized Image")
    plt.show()
except Exception as e:
    print("Error displaying image:", e)
